# 🏦 ARU - Sistema de Gestión Financiera

## 📋 Descripción General

ARU es un sistema web para la gestión de bolsillos de ahorro y pagos automáticos. Permite a los usuarios crear múltiples bolsillos de ahorro, gestionar saldos y automatizar pagos.

---

## 📁 Estructura del Proyecto

```
Proyecto ARU/
├── frontend/                  # 🎨 INTERFAZ DE USUARIO
│   ├── html/                 # Páginas HTML
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── registro.html
│   │   ├── dashboard.html
│   │   ├── bolsillos.html
│   │   ├── admin.html
│   │   └── NAVEGACION-ARU.html
│   ├── css/                  # Estilos CSS
│   │   ├── style.css         # Estilos principales
│   │   ├── style-aru.css     # Estilos alternativos
│   │   └── style-original.css
│   ├── js/                   # Scripts JavaScript
│   │   ├── app.js            # Lógica principal
│   │   └── app-aru.js        # Script alternativo
│   └── LEEME.md              # Documentación del frontend
│
├── backend/                   # 🔧 SERVIDOR Y API
│   ├── app.py                # Aplicación principal Flask
│   ├── db.py                 # Funciones de BD
│   ├── init_db.sql          # Script para inicializar BD
│   ├── requirements.txt      # Dependencias Python
│   ├── routes/               # Endpoints de la API
│   │   ├── usuarios.py       # Autenticación y pagos
│   │   ├── bolsillos.py      # Gestión de bolsillos
│   │   ├── saldo.py          # Gestión de saldo
│   │   └── admin.py          # Funciones administrativas
│   ├── services/             # Lógica de negocio
│   │   └── auth_service.py   # Servicio de autenticación
│   ├── LEEME.md              # Documentación del backend
│   └── __pycache__/          # Cache Python
│
├── backend-aru/              # ⚠️ DEPRECADO (usar /backend)
│
├── README.md                 # Este archivo
├── RESUMEN-FINAL.md         # Resumen del proyecto
├── CAMBIOS-ARU.md           # Historial de cambios
└── INICIO-ARU.ps1           # Script de inicio
```

---

## 🚀 Inicio Rápido

### 1️⃣ Configurar el Backend

```bash
# Navegar a la carpeta backend
cd backend

# Instalar dependencias
pip install -r requirements.txt

# Inicializar base de datos
sqlite3 < init_db.sql

# Ejecutar el servidor
python app.py
```

El backend estará disponible en: **`http://localhost:5000`**

### 2️⃣ Servir el Frontend

**Opción A: Python**
```bash
cd frontend
python -m http.server 8000
```

**Opción B: Node.js**
```bash
npx http-server frontend -p 8000
```

**Opción C: Live Server en VS Code**
- Instala la extensión "Live Server"
- Click derecho en `frontend/html/index.html` → "Open with Live Server"

El frontend estará disponible en: **`http://localhost:8000`** (o el puerto que uses)

---

## 🏗️ Arquitectura

### Frontend (Separación clara)
- **HTML**: Páginas en `frontend/html/`
- **CSS**: Estilos en `frontend/css/`
- **JavaScript**: Lógica en `frontend/js/`

### Backend (API REST)
- **Rutas**: Endpoints organizados por módulo en `backend/routes/`
- **Servicios**: Lógica de negocio en `backend/services/`
- **Base de Datos**: SQLite con esquema en `backend/init_db.sql`

### Comunicación
- Frontend hace llamadas `fetch()` a los endpoints del backend
- Autenticación con **JWT** tokens
- Respuestas en **JSON**

---

## 🔌 Endpoints Principales

### Autenticación
- `POST /registro` - Registrar usuario
- `POST /login` - Iniciar sesión
- `POST /login/admin` - Iniciar sesión como admin

### Bolsillos
- `GET /api/bolsillos` - Listar bolsillos
- `POST /api/bolsillos/create` - Crear bolsillo
- `PUT /api/bolsillos/<id>` - Actualizar bolsillo
- `DELETE /api/bolsillos/<id>` - Eliminar bolsillo

### Saldo
- `GET /saldo/<usuario_id>` - Obtener saldo
- `POST /saldo/add` - Agregar dinero
- `POST /saldo/subtract` - Restar dinero

### Pagos Automáticos
- `GET /pagos_automaticos/<usuario_id>` - Listar pagos
- `POST /pagos_automaticos` - Crear pago
- `DELETE /pagos_automaticos/<id>` - Eliminar pago

### Admin
- `GET /admin/users` - Listar usuarios
- `DELETE /admin/users/<id>` - Eliminar usuario
- `GET /admin/reports` - Ver reportes

---

## 🔐 Autenticación

El sistema usa **JWT (JSON Web Tokens)**:

1. Usuario se registra o inicia sesión
2. Servidor retorna un `token`
3. Frontend almacena el token en `localStorage`
4. En cada petición se envía: `Authorization: Bearer <token>`
5. Backend valida el token

---

## 💾 Base de Datos

### Tabla: usuarios
- `id`, `email`, `contraseña`, `nombre`, `rol`, `created_at`

### Tabla: bolsillos
- `id`, `usuario_id`, `nombre`, `saldo`, `fecha`, `created_at`

### Tabla: pagos_automaticos
- `id`, `usuario_id`, `nombre`, `monto`, `fecha`, `created_at`

---

## 📖 Documentación Detallada

- **[Frontend - LEEME.md](./frontend/LEEME.md)** - Guía completa del frontend
- **[Backend - LEEME.md](./backend/LEEME.md)** - Guía completa del backend

---

## 🛠️ Desarrollo

### Agregar un nuevo endpoint

1. Crear la función en `backend/routes/<modulo>.py`
2. Registrar el blueprint en `backend/app.py`
3. Implementar la lógica en el frontend `frontend/js/app.js`

### Agregar una nueva tabla

1. Agregar la tabla en `backend/init_db.sql`
2. Crear funciones de acceso en `backend/db.py` si es necesario
3. Crear endpoints para acceder a la tabla

---

## 🚨 Notas Importantes

- ⚠️ **backend-aru/** está DEPRECADO → Usar **backend/** en su lugar
- ⚠️ Los archivos HTML debe estar en `frontend/html/`
- ⚠️ Los archivos CSS deben estar en `frontend/css/`
- ⚠️ Los archivos JS deben estar en `frontend/js/`
- ⚠️ CORS solo está habilitado para desarrollo local

---

## 🔧 Requisitos

- **Python** 3.8+
- **Node.js** (opcional, solo si usas http-server)
- **Navegador moderno** (Chrome, Firefox, Safari, Edge)

---

## 📝 Historial

Ver **[CAMBIOS-ARU.md](./CAMBIOS-ARU.md)** para el historial completo de cambios.

---

## 👤 Contacto

Para preguntas o reportes de bugs, contacta al equipo de desarrollo.

---

## 📄 Licencia

© 2025 ARU - Sistema de Gestión Financiera. Todos los derechos reservados.
