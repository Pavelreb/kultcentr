# backend/medialib/utils.py
"""Компрессия видео и конвертация аудио через ffmpeg (imageio-ffmpeg)."""

import logging
import os
import re
import subprocess

logger = logging.getLogger(__name__)

try:
    import imageio_ffmpeg

    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # pragma: no cover
    FFMPEG = None

_DURATION_RE = re.compile(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)")


def probe_duration(path):
    """Длительность медиафайла в секундах (парсим вывод ffmpeg -i)."""
    if not FFMPEG:
        return None
    try:
        proc = subprocess.run(
            [FFMPEG, "-i", path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
        m = _DURATION_RE.search(proc.stderr or "")
        if m:
            h, mnt, sec = int(m.group(1)), int(m.group(2)), float(m.group(3))
            return int(h * 3600 + mnt * 60 + sec)
    except Exception as exc:
        logger.warning("probe_duration failed for %s: %s", path, exc)
    return None


def _run(cmd, timeout=1800):
    proc = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
        timeout=timeout,
    )
    return proc.returncode == 0


def compress_video(src_path):
    """Сжимает видео в MP4 (H.264, CRF 28, ширина <=1920).

    Возвращает путь к сжатому файлу, если он получился меньше исходника,
    иначе None (оставляем оригинал).
    """
    if not FFMPEG:
        return None
    base, _ = os.path.splitext(src_path)
    dst_path = base + ".compressed.mp4"
    cmd = [
        FFMPEG, "-y", "-i", src_path,
        "-vf", "scale='min(1920,iw)':-2",
        "-c:v", "libx264", "-crf", "28", "-preset", "veryfast",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        dst_path,
    ]
    try:
        if not _run(cmd) or not os.path.exists(dst_path):
            return None
        if os.path.getsize(dst_path) >= os.path.getsize(src_path):
            os.remove(dst_path)
            return None
        return dst_path
    except Exception as exc:
        logger.warning("compress_video failed for %s: %s", src_path, exc)
        if os.path.exists(dst_path):
            try:
                os.remove(dst_path)
            except OSError:
                pass
        return None


def convert_to_mp3(src_path):
    """Конвертирует аудио в MP3 (libmp3lame, 192k).

    Если исходник уже MP3 — возвращает None (не трогаем).
    """
    if not FFMPEG:
        return None
    base, ext = os.path.splitext(src_path)
    if ext.lower() == ".mp3":
        return None
    dst_path = base + ".mp3"
    cmd = [
        FFMPEG, "-y", "-i", src_path,
        "-codec:a", "libmp3lame", "-b:a", "192k",
        dst_path,
    ]
    try:
        if _run(cmd) and os.path.exists(dst_path):
            return dst_path
    except Exception as exc:
        logger.warning("convert_to_mp3 failed for %s: %s", src_path, exc)
    if os.path.exists(dst_path):
        try:
            os.remove(dst_path)
        except OSError:
            pass
    return None


def replace_file_field(instance, new_path):
    """Подменяет файл в FileField на обработанный, удаляя исходник."""
    from django.conf import settings

    old_path = instance.file.path
    rel_new = os.path.relpath(new_path, settings.MEDIA_ROOT).replace(os.sep, "/")
    instance.file.name = rel_new
    if os.path.abspath(old_path) != os.path.abspath(new_path) and os.path.exists(old_path):
        try:
            os.remove(old_path)
        except OSError:
            pass
