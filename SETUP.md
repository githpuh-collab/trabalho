# Setup Rapido

Execute os comandos abaixo na pasta que contem `manage.py`.

## 1. Ambiente virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativacao:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 2. Dependencias

```powershell
pip install -r requirements.txt
```

## 3. Banco de dados

```powershell
python manage.py migrate
```

## 4. Usuario administrador

Opcao automatica:

```powershell
python create_superuser.py
```

Opcao manual:

```powershell
python manage.py createsuperuser
```

## 5. Dados de exemplo

Opcional, para testar rapidamente:

```powershell
python create_sample_data.py
```

## 6. Servidor

```powershell
python manage.py runserver
```

## 7. Testes

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Script opcional incluido no projeto: `setup_windows.ps1`.
