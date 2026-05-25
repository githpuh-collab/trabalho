<#
Automação de setup (PowerShell)
Execute na raiz do projeto (onde está manage.py):
    .\setup_windows.ps1
#>

Write-Host "1/6 - Criando venv..."
python -m venv venv

Write-Host "2/6 - Ativando venv (tentando Activate.ps1)..."
try {
    .\venv\Scripts\Activate.ps1
} catch {
    Write-Warning "Não foi possível executar Activate.ps1 automaticamente. Se necessário, rode: .\venv\Scripts\Activate.ps1"
}

Write-Host "3/6 - Instalando dependências..."
.\venv\Scripts\pip.exe install -r requirements.txt

Write-Host "4/6 - Aplicando migrações..."
.\venv\Scripts\python.exe manage.py migrate

Write-Host "5/6 - Criando superuser (se não existir)..."
.\venv\Scripts\python.exe create_superuser.py

Write-Host "6/6 - Iniciando servidor em background (Ctrl+C para parar)..."
.\venv\Scripts\python.exe manage.py runserver
