# 🏦 Proyecto ARU - Gestión de Billeteras Digitales

Sistema web completo de gestión de billeteras digitales con separación clara entre frontend y backend.

## 📋 Estructura del Proyecto

```
proyecto-aru/
├── frontend/                 # Aplicación web (HTML5, CSS3, JS vanilla)
│   ├── html/                # Páginas HTML
│   ├── css/                 # Estilos
│   ├── js/                  # Lógica JavaScript
│   └── LEEME.md            # Documentación frontend
├── backend/                 # API REST (Python Flask)
│   ├── routes/             # Endpoints de la API
│   ├── services/           # Lógica de negocio
│   ├── app.py             # Aplicación Flask
│   ├── db.py              # Funciones de BD
│   ├── requirements.txt    # Dependencias Python
│   └── LEEME.md           # Documentación backend
└── .gitignore             # Archivos ignorados en Git
```

## 🚀 Inicio Rápido

### Backend (Python Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
# API disponible en http://localhost:5000
```

**Requisitos:**
- Python 3.8+
- MySQL con base de datos `contabilidad_db`

**Primeros pasos:**
1. Configurar credenciales en `backend/db.py`
2. Inicializar BD: `mysql -u root -p < backend/init_db.sql`
3. Ejecutar: `python backend/app.py`

### Frontend (Vanilla JavaScript)

```bash
cd frontend
python -m http.server 8000
# Abrir http://localhost:8000 en navegador
```

## 📚 Documentación

- **[LEEME-PRIMERO.md](./LEEME-PRIMERO.md)** - Punto de entrada
- **[GUIA-RAPIDA.md](./GUIA-RAPIDA.md)** - Setup y primeros pasos
- **[ESTRUCTURA.md](./ESTRUCTURA.md)** - Detalles técnicos
- **[frontend/LEEME.md](./frontend/LEEME.md)** - Documentación frontend
- **[backend/LEEME.md](./backend/LEEME.md)** - Documentación backend

## ✨ Características

- ✅ Separación clara frontend/backend
- ✅ API REST con Flask + Blueprints
- ✅ Autenticación con tokens
- ✅ Base de datos MySQL
- ✅ Interfaz responsive
- ✅ Gestión de billeteras y saldos
- ✅ Pagos automáticos

## 🛠️ Tech Stack

**Frontend:**
- HTML5, CSS3
- JavaScript ES6+
- Fetch API para HTTP

**Backend:**
- Python 3.8+
- Flask Framework
- Flask-CORS
- MySQL Database

## 📝 Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/login` | Autenticación |
| POST | `/api/usuarios` | Crear usuario |
| GET | `/api/saldo/<id>` | Obtener saldo |
| PUT | `/api/saldo/<id>` | Actualizar saldo |
| GET | `/api/bolsillos` | Listar billeteras |
| POST | `/api/bolsillos/create` | Crear billetera |
| POST | `/api/pagos_automaticos` | Crear pago automático |

## 🔐 Autenticación

En desarrollo, `/login` devuelve token `"demo"`. 

Headers requeridos para endpoints protegidos:
```
Authorization: Bearer demo
```

## 📦 Dependencias

**Backend (`requirements.txt`):**
- Flask
- Flask-CORS
- mysql-connector-python

**Frontend:**
- Sin dependencias externas (vanilla JS)

## 🏃 Ejecutar Proyecto Completo

Script automático (Windows):
```powershell
.\INICIAR-ARU.ps1
```

Manual:
```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd frontend
python -m http.server 8000
```

## 📝 Licencia

Proyecto personal - ARU 2024
