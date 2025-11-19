# 🚀 GUÍA RÁPIDA - ESTRUCTURA DEL PROYECTO ARU

## ✅ Nueva Estructura (Bien Separada)

```
Proyecto ARU/
│
├── 📁 frontend/                    🎨 TODO el código del cliente
│   ├── 📁 html/                   Todas las páginas HTML
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── registro.html
│   │   ├── dashboard.html
│   │   ├── bolsillos.html
│   │   ├── admin.html
│   │   ├── PLANTILLA.html         ← Usar como referencia
│   │   └── NAVEGACION-ARU.html
│   │
│   ├── 📁 css/                    Todos los estilos
│   │   ├── style.css              Estilos principales
│   │   ├── style-aru.css
│   │   └── style-original.css
│   │
│   ├── 📁 js/                     Todo el código JavaScript
│   │   ├── config.js              ⭐ Configuración (IMPORTANTE)
│   │   ├── app.js                 Lógica principal
│   │   └── app-aru.js
│   │
│   └── LEEME.md                   Documentación del frontend
│
│
├── 📁 backend/                     🔧 TODO el servidor
│   ├── app.py                     Aplicación principal
│   ├── db.py                      Base de datos
│   ├── init_db.sql               Inicializar BD
│   ├── requirements.txt           Dependencias
│   │
│   ├── 📁 routes/                 Endpoints de la API
│   │   ├── usuarios.py            Login, registro, pagos
│   │   ├── bolsillos.py           Gestión de bolsillos
│   │   ├── saldo.py               Gestión de saldo
│   │   └── admin.py               Funciones admin
│   │
│   ├── 📁 services/               Lógica de negocio
│   │   └── auth_service.py        Autenticación
│   │
│   └── LEEME.md                   Documentación del backend
│
│
├── ESTRUCTURA.md                   Esta guía visual
├── README.md                       Descripción general
└── ... (otros archivos)
```

---

## 🎯 LO IMPORTANTE

### 1️⃣ Frontend (frontend/)
- **HTML** va en `frontend/html/`
- **CSS** va en `frontend/css/`
- **JS** va en `frontend/js/`

### 2️⃣ Backend (backend/)
- **Python** aquí dentro
- **Rutas** en `backend/routes/`
- **Servicios** en `backend/services/`

### 3️⃣ Rutas Relativas en HTML
```html
<!-- En: frontend/html/index.html -->
<link rel="stylesheet" href="../css/style.css">
<script src="../js/config.js"></script>
<script src="../js/app.js"></script>
```

---

## 🔧 INICIO RÁPIDO

### Terminal 1: Backend
```powershell
cd backend
pip install -r requirements.txt
python app.py
# ✅ Backend en: http://localhost:5000
```

### Terminal 2: Frontend
```powershell
cd frontend
python -m http.server 8000
# ✅ Frontend en: http://localhost:8000
```

---

## 📦 CONFIGURACIÓN

**Cambiar URL del backend:**
```javascript
// Editar: frontend/js/config.js
const CONFIG = {
    API_BASE: "http://localhost:5000",  // ← Aquí
};
```

---

## 🗂️ FLUJO DE DESARROLLO

### Agregar una PÁGINA HTML
1. Crear archivo en `frontend/html/miPagina.html`
2. Importar CSS: `<link rel="stylesheet" href="../css/style.css">`
3. Importar JS: `<script src="../js/app.js"></script>`

### Agregar una FUNCIÓN JavaScript
1. Agregar en `frontend/js/app.js`
2. Usar `fetch()` con `API_BASE` para llamar al backend

### Agregar un ENDPOINT Backend
1. Crear función en `backend/routes/modulo.py`
2. Registrar en `backend/app.py`
3. Llamar desde frontend con `fetch()`

---

## ✅ CHECKLIST

- [ ] Archivos HTML en `frontend/html/`
- [ ] Archivos CSS en `frontend/css/`
- [ ] Archivos JS en `frontend/js/`
- [ ] Backend en `backend/`
- [ ] Rutas relativas correctas en HTML
- [ ] `backend-aru/` NO está siendo usado
- [ ] Config.js tiene la URL correcta del backend

---

## ⚠️ QUÉ NO HACER

❌ No mezclar HTML, CSS y JS en la raíz
❌ No usar rutas absolutas en HTML
❌ No olvidar `../` en las rutas relativas
❌ No usar `backend-aru/` (está deprecado)
❌ No tener el backend en otra carpeta

---

## 📚 DOCUMENTACIÓN

- **Frontend completo:** `frontend/LEEME.md`
- **Backend completo:** `backend/LEEME.md`
- **Proyecto general:** `ESTRUCTURA.md`
