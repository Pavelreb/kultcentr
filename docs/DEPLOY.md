# Деплой на VPS (Ubuntu) — пошаговая инструкция

Развёртывание «Центра Культуры» на чистом сервере в РФ. Подходит как для демо-сайта, так и для установки клиенту «под ключ».

**Что понадобится:**
- VPS с Ubuntu 22.04/24.04 (минимум 1 CPU / 2 ГБ RAM / 20 ГБ диск)
- Домен с A-записью на IP сервера
- SSH-доступ (логин/пароль или ключ)

---

## 1. Подключение и базовая настройка сервера

```bash
ssh root@IP-СЕРВЕРА

apt update && apt upgrade -y
apt install -y python3.12 python3.12-venv python3-pip nodejs npm nginx git ufw

# Брандмауэр
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable   # ответить y

# Свежая LTS-версия Node.js (в репозитории Ubuntu часто старая)
npm install -g n
n lts
```

## 2. Пользователь и код проекта

```bash
adduser kultura          # придумайте пароль
usermod -aG sudo kultura
su - kultura

git clone https://github.com/Pavelreb/kultcentr.git
cd kultcentr
```

## 3. Бэкенд

```bash
cd backend
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Конфигурация
cp .env.example .env
nano .env
```

Заполнить `.env`:

```env
SECRET_KEY=<сгенерировать: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())">
DEBUG=False
ALLOWED_HOSTS=ваш-домен.ru,www.ваш-домен.ru,IP-сервера
CORS_ALLOWED_ORIGINS=https://ваш-домен.ru
CSRF_TRUSTED_ORIGINS=https://ваш-домен.ru
```

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## 4. Перенос демо-контента (БД + медиа)

База и медиа не хранятся в git — их копируем с локальной машины.
**На локальном компьютере** (Git Bash / WSL), не на сервере:

```bash
cd /c/Users/pavel/Documents/kulturaweb/kultcentr/backend

# Архив с контентом
tar -czvf ~/demo_content.tar.gz db.sqlite3 media/

# Загрузка на сервер (ввести пароль пользователя kultura)
scp ~/demo_content.tar.gz kultura@IP-СЕРВЕРА:/home/kultura/
```

**На сервере:**

```bash
cd /home/kultura/kultcentr/backend
tar -xzvf /home/kultura/demo_content.tar.gz   # развернёт db.sqlite3 и media/ поверх
rm /home/kultura/demo_content.tar.gz
```

## 5. Фронтенд

```bash
cd /home/kultura/kultcentr/frontend
npm install

# Адрес API для продакшена — через домен (Nginx проксирует на Django)
NUXT_PUBLIC_API_BASE=https://ваш-домен.ru/api npm run build
```

## 6. Сервисы systemd (автозапуск)

```bash
sudo nano /etc/systemd/system/kultura-backend.service
```

```ini
[Unit]
Description=Kultcentr Django (Gunicorn)
After=network.target

[Service]
User=kultura
WorkingDirectory=/home/kultura/kultcentr/backend
ExecStart=/home/kultura/kultcentr/backend/venv/bin/gunicorn config.wsgi:application \
    --bind 127.0.0.1:8000 --workers 3
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo nano /etc/systemd/system/kultura-frontend.service
```

```ini
[Unit]
Description=Kultcentr Nuxt
After=network.target

[Service]
User=kultura
WorkingDirectory=/home/kultura/kultcentr/frontend
Environment=NUXT_PUBLIC_API_BASE=https://ваш-домен.ru/api
Environment=PORT=3000
ExecStart=/usr/bin/node .output/server/index.mjs
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now kultura-backend kultura-frontend
sudo systemctl status kultura-backend kultura-frontend   # оба active (running)
```

## 7. Nginx

```bash
sudo nano /etc/nginx/sites-available/kultura
```

```nginx
server {
    listen 80;
    server_name ваш-домен.ru www.ваш-домен.ru;

    client_max_body_size 100M;   # загрузка видео через сайт

    # API Django
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Админка Django
    location /admin/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Статика Django (админка)
    location /static/ {
        alias /home/kultura/kultcentr/backend/staticfiles/;
    }

    # Медиафайлы (Range — для перемотки видео)
    location /media/ {
        alias /home/kultura/kultcentr/backend/media/;
        add_header Accept-Ranges bytes;
    }

    # Фронтенд Nuxt
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/kultura /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## 8. HTTPS (бесплатный сертификат)

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d ваш-домен.ru -d www.ваш-домен.ru
# согласиться на редирект HTTP → HTTPS
```

Сертификат обновляется автоматически.

## 9. Проверка

- `https://ваш-домен.ru` — сайт со всем демо-контентом
- `https://ваш-домен.ru/admin/` — админка
- `https://ваш-домен.ru/api/` — API

---

## Обновление сайта (после доработок)

```bash
cd /home/kultura/kultcentr
git pull
cd backend && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
cd ../frontend
NUXT_PUBLIC_API_BASE=https://ваш-домен.ru/api npm run build
sudo systemctl restart kultura-backend kultura-frontend
```

## Бэкап (раз в сутки, cron)

```bash
crontab -e
```

```cron
0 3 * * * cd /home/kultura/kultcentr/backend && tar -czf /home/kultura/backups/backup-$(date +\%Y\%m\%d).tar.gz db.sqlite3 media/ && find /home/kultura/backups -mtime +14 -delete
```

(предварительно `mkdir -p /home/kultura/backups`)

## Возможные проблемы

| Симптом | Решение |
|---------|---------|
| 502 Bad Gateway | Сервис не запущен: `sudo systemctl status kultura-backend` |
| Ошибка CORS в консоли | Проверить `CORS_ALLOWED_ORIGINS` в `.env` — должен быть `https://...` без слеша в конце |
| Не пускает в админку | Проверить `CSRF_TRUSTED_ORIGINS` в `.env` |
| Не грузятся большие видео | `client_max_body_size` в Nginx |
| Изменения .env не применились | `sudo systemctl restart kultura-backend` |
