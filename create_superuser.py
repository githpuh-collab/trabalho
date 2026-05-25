"""
Script auxiliar para criar o superuser não interativamente.
Uso (na raiz do projeto onde está `manage.py`):
    python create_superuser.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = 'admin'
EMAIL = ''
PASSWORD = '123456'

if User.objects.filter(username=USERNAME).exists():
    print(f"Superuser '{USERNAME}' já existe.")
else:
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superuser '{USERNAME}' criado com senha '{PASSWORD}'.")
