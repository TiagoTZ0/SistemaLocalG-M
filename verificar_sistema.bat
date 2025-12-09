@echo off
REM Script de verificación del sistema - Sistema G&M Local

echo.
echo ============================================================
echo   VERIFICADOR DE CONFIGURACION - SISTEMA G&M
echo ============================================================
echo.

setlocal enabledelayedexpansion

set "verificaciones_ok=0"
set "verificaciones_total=0"

REM Verificar Python
set /a verificaciones_total+=1
echo [*] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python no encontrado
) else (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do set "python_version=%%i"
    echo [OK] !python_version!
    set /a verificaciones_ok+=1
)

REM Verificar archivo .env
set /a verificaciones_total+=1
echo [*] Verificando archivo .env...
if not exist .env (
    echo [X] Archivo .env no encontrado
) else (
    echo [OK] Archivo .env presente
    set /a verificaciones_ok+=1
)

REM Verificar requirements.txt
set /a verificaciones_total+=1
echo [*] Verificando requirements.txt...
if not exist requirements.txt (
    echo [X] Archivo requirements.txt no encontrado
) else (
    echo [OK] Archivo requirements.txt presente
    set /a verificaciones_ok+=1
)

REM Verificar backend/server.py
set /a verificaciones_total+=1
echo [*] Verificando backend/server.py...
if not exist backend\server.py (
    echo [X] Archivo backend/server.py no encontrado
) else (
    echo [OK] Archivo backend/server.py presente
    set /a verificaciones_ok+=1
)

REM Verificar frontend/index.html
set /a verificaciones_total+=1
echo [*] Verificando frontend/index.html...
if not exist frontend\index.html (
    echo [X] Archivo frontend/index.html no encontrado
) else (
    echo [OK] Archivo frontend/index.html presente
    set /a verificaciones_ok+=1
)

REM Verificar psycopg2
set /a verificaciones_total+=1
echo [*] Verificando psycopg2-binary...
pip show psycopg2-binary >nul 2>&1
if errorlevel 1 (
    echo [?] No instalado (se instalará al iniciar)
) else (
    echo [OK] Instalado
    set /a verificaciones_ok+=1
)

echo.
echo ============================================================
echo   RESUMEN: !verificaciones_ok! de !verificaciones_total! verificaciones completadas
echo ============================================================
echo.

if !verificaciones_ok! equ !verificaciones_total! (
    echo [✓] Sistema listo para usar
    echo.
    echo Próximos pasos:
    echo 1. Edita el archivo .env con tus credenciales de Supabase
    echo 2. Ejecuta: start_server.bat
    echo 3. Abre: http://localhost:8000
    echo.
) else (
    echo [!] Hay problemas con la configuración
    echo.
    echo Por favor:
    echo 1. Verifica que Python esté instalado
    echo 2. Verifica que tengas todos los archivos necesarios
    echo 3. Lee el archivo CONFIGURACION_LOCAL.md
    echo.
)

pause
