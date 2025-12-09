@echo off
REM Script para iniciar el servidor de desarrollo local de G&M

echo.
echo ============================================================
echo   SISTEMA DE MUEBLERIA G&M - SERVIDOR LOCAL
echo ============================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH
    echo Por favor instala Python desde: https://www.python.org
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    pause
    exit /b 1
)

REM Cambiar al directorio del backend
cd /d %~dp0backend

REM Verificar que el archivo .env existe
if not exist ..\.env (
    echo [AVISO] No se encontró el archivo .env
    echo Creando archivo .env con valores por defecto...
    echo # Configuración de Supabase > ..\.env
    echo SUPABASE_HOST=your-project.supabase.co >> ..\.env
    echo SUPABASE_PORT=5432 >> ..\.env
    echo SUPABASE_USER=postgres >> ..\.env
    echo SUPABASE_PASSWORD=your-password >> ..\.env
    echo # Configuración local del servidor >> ..\.env
    echo SERVER_HOST=localhost >> ..\.env
    echo SERVER_PORT=8000 >> ..\.env
    echo.
    echo [!] Por favor edita el archivo .env con tus credenciales de Supabase
    echo Ubicación: %~dp0\.env
    echo.
    pause
    exit /b 1
)

REM Instalar/Actualizar dependencias
echo [*] Verificando dependencias...
pip install -q -r ../requirements.txt
if errorlevel 1 (
    echo [ERROR] No se pudieron instalar las dependencias
    pause
    exit /b 1
)

REM Iniciar el servidor
echo.
echo [✓] Iniciando servidor...
echo.
python server.py

pause
