#!/usr/bin/env bash
# Build script for Render.com deployment
set -o errexit   # exit on first error

echo "==> Installing Python dependencies..."
pip install -r requirements.txt

echo "==> Collecting static files..."
python manage.py collectstatic --no-input

echo "==> Running database migrations..."
python manage.py migrate

echo "==> Creating superadmin account (if not already exists)..."
python manage.py shell -c "
import os
from accounts.models import User

email = os.environ.get('ADMIN_EMAIL', 'admin@qrdine.com')
password = os.environ.get('ADMIN_PASSWORD', '')

if not password:
    print('WARNING: ADMIN_PASSWORD env var not set — skipping superadmin creation.')
elif not User.objects.filter(email=email).exists():
    u = User.objects.create_superuser(username=email, email=email, password=password)
    u.role = 'superadmin'
    u.save()
    print(f'Superadmin created: {email}')
else:
    print(f'Superadmin already exists: {email}')
"

echo "==> Build complete!"
