# backend/config/media_serve.py
"""Раздача медиафайлов с поддержкой HTTP Range (нужна перемотка видео/аудио).

В DEBUG-режиме заменяет django.conf.urls.static.static для MEDIA_URL:
стандартная раздача игнорирует заголовок Range, из-за чего браузер
не может перематывать видео и аудио.
"""

import mimetypes
import os
import re

from django.conf import settings
from django.http import FileResponse, Http404, StreamingHttpResponse

_RANGE_RE = re.compile(r"bytes=(\d*)-(\d*)")
_CHUNK = 64 * 1024


def _file_iter(fh, remaining):
    try:
        while True:
            data = fh.read(min(_CHUNK, remaining))
            if not data:
                break
            remaining -= len(data)
            yield data
    finally:
        fh.close()


def serve_media_range(request, path):
    media_root = os.path.normpath(settings.MEDIA_ROOT)
    full_path = os.path.normpath(os.path.join(media_root, path))

    # Защита от выхода за пределы MEDIA_ROOT
    if not full_path.startswith(media_root + os.sep) or not os.path.isfile(full_path):
        raise Http404

    size = os.path.getsize(full_path)
    content_type = mimetypes.guess_type(full_path)[0] or "application/octet-stream"

    range_header = request.headers.get("Range", "")
    m = _RANGE_RE.match(range_header.strip())

    if m and (m.group(1) or m.group(2)):
        if m.group(1):
            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else size - 1
        else:
            # bytes=-N — последние N байт
            start = max(0, size - int(m.group(2)))
            end = size - 1
        end = min(end, size - 1)
        if start > end:
            raise Http404

        fh = open(full_path, "rb")
        fh.seek(start)
        length = end - start + 1
        response = StreamingHttpResponse(
            _file_iter(fh, length), status=206, content_type=content_type
        )
        response["Content-Range"] = f"bytes {start}-{end}/{size}"
        response["Content-Length"] = str(length)
        response["Accept-Ranges"] = "bytes"
        return response

    response = FileResponse(open(full_path, "rb"), content_type=content_type)
    response["Content-Length"] = str(size)
    response["Accept-Ranges"] = "bytes"
    return response
