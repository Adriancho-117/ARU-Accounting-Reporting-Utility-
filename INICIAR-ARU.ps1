# ============================================
# ARU - Script de Inicio Completo
# Inicia el backend y frontend automáticamente
# ============================================

$projectPath = Get-Location
$backendPath = Join-Path $projectPath "backend"
$frontendPath = Join-Path $projectPath "frontend"

Write-Host "===========================================`n" -ForegroundColor Cyan
Write-Host "🚀 ARU - SISTEMA DE GESTIÓN FINANCIERA" -ForegroundColor Green -BackgroundColor Black
Write-Host "===========================================`n" -ForegroundColor Cyan

# Verificar que estamos en la carpeta correcta
if (-not (Test-Path $backendPath)) {
    Write-Host "❌ ERROR: No se encontró la carpeta 'backend/'" -ForegroundColor Red
    Write-Host "Asegúrate de ejecutar este script desde la raíz del proyecto." -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

if (-not (Test-Path $frontendPath)) {
    Write-Host "❌ ERROR: No se encontró la carpeta 'frontend/'" -ForegroundColor Red
    Write-Host "Asegúrate de ejecutar este script desde la raíz del proyecto." -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "📁 Proyecto encontrado en: $projectPath`n" -ForegroundColor Green

# Menú de opciones
Write-Host "Selecciona qué deseas hacer:`n" -ForegroundColor Cyan
Write-Host "1. Instalar dependencias del backend" -ForegroundColor Yellow
Write-Host "2. Inicializar base de datos" -ForegroundColor Yellow
Write-Host "3. Iniciar solo el backend" -ForegroundColor Yellow
Write-Host "4. Iniciar solo el frontend" -ForegroundColor Yellow
Write-Host "5. Iniciar backend y frontend" -ForegroundColor Yellow
Write-Host "6. Salir" -ForegroundColor Yellow
Write-Host ""

$choice = Read-Host "Ingresa el número de tu opción"

switch ($choice) {
    "1" {
        Write-Host "`n📦 Instalando dependencias del backend..." -ForegroundColor Cyan
        Set-Location $backendPath
        pip install -r requirements.txt
        Write-Host "`n✅ Dependencias instaladas correctamente." -ForegroundColor Green
        Write-Host "Ahora puedes usar las opciones 2, 3 o 5." -ForegroundColor Yellow
    }
    
    "2" {
        Write-Host "`n🗄️ Inicializando base de datos..." -ForegroundColor Cyan
        Set-Location $backendPath
        if (Test-Path "init_db.sql") {
            sqlite3 < init_db.sql
            Write-Host "`n✅ Base de datos inicializada." -ForegroundColor Green
        } else {
            Write-Host "`n❌ No se encontró init_db.sql" -ForegroundColor Red
        }
    }
    
    "3" {
        Write-Host "`n🔧 Iniciando BACKEND..." -ForegroundColor Cyan
        Set-Location $backendPath
        Write-Host "`n📍 Backend en: http://localhost:5000" -ForegroundColor Green
        Write-Host "⚠️  Presiona Ctrl+C para detener el servidor`n" -ForegroundColor Yellow
        python app.py
    }
    
    "4" {
        Write-Host "`n🎨 Iniciando FRONTEND..." -ForegroundColor Cyan
        Set-Location $frontendPath
        Write-Host "`n📍 Frontend en: http://localhost:8000" -ForegroundColor Green
        Write-Host "📄 Accede a: http://localhost:8000/html/index.html" -ForegroundColor Green
        Write-Host "⚠️  Presiona Ctrl+C para detener el servidor`n" -ForegroundColor Yellow
        python -m http.server 8000
    }
    
    "5" {
        Write-Host "`n🚀 Iniciando BACKEND y FRONTEND..." -ForegroundColor Cyan
        
        # Iniciar backend en una nueva ventana
        Write-Host "`n1. Abriendo backend en una nueva ventana..." -ForegroundColor Green
        Start-Process powershell.exe -ArgumentList "-NoExit -Command `"cd '$backendPath'; python app.py`""
        Start-Sleep -Seconds 3
        
        # Iniciar frontend en otra ventana
        Write-Host "2. Abriendo frontend en una nueva ventana..." -ForegroundColor Green
        Start-Process powershell.exe -ArgumentList "-NoExit -Command `"cd '$frontendPath'; python -m http.server 8000`""
        Start-Sleep -Seconds 2
        
        Write-Host "`n✅ Servidores iniciados en nuevas ventanas:" -ForegroundColor Green
        Write-Host "   📍 Backend:  http://localhost:5000" -ForegroundColor Cyan
        Write-Host "   📍 Frontend: http://localhost:8000" -ForegroundColor Cyan
        Write-Host "   📄 Acceso:   http://localhost:8000/html/index.html`n" -ForegroundColor Cyan
    }
    
    "6" {
        Write-Host "`n👋 ¡Hasta pronto!" -ForegroundColor Green
    }
    
    default {
        Write-Host "`n❌ Opción no válida." -ForegroundColor Red
    }
}

Set-Location $projectPath
Write-Host "`n===========================================`n" -ForegroundColor Cyan
