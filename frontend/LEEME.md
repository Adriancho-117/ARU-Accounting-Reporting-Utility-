# Frontend - ARU (Sistema de Gestión Financiera)

## 📁 Estructura

```
frontend/
├── html/                  # Archivos HTML (páginas)
│   ├── index.html        # Página principal
│   ├── login.html        # Página de inicio de sesión
│   ├── registro.html     # Página de registro
│   ├── dashboard.html    # Panel principal del usuario
│   ├── bolsillos.html    # Gestión de bolsillos
│   └── admin.html        # Panel de administrador
├── css/                   # Estilos CSS
│   └── style.css         # Estilos principales
├── js/                    # Scripts JavaScript
│   └── app.js            # Lógica principal de la aplicación
└── LEEME.md              # Este archivo
```

## 🚀 Cómo usar

### 1. Servir los archivos frontend

Los archivos HTML deben servirse desde un servidor web local o remoto. Opciones:

**Opción A: Python (recomendado)**
```bash
cd frontend
python -m http.server 8000
```
Luego accede a: `http://localhost:8000`

**Opción B: Node.js (http-server)**
```bash
npx http-server frontend -p 8000
```

**Opción C: Live Server en VS Code**
- Instala la extensión "Live Server"
- Click derecho en un archivo HTML → "Open with Live Server"

### 2. Asegurate que el backend esté corriendo
```bash
cd backend-aru
python app.py
```
El backend debe estar en `http://localhost:5000`

## 📄 Archivos HTML

Todos los archivos HTML deben ir en la carpeta `html/` y deben importar:

```html
<link rel="stylesheet" href="../css/style.css">
<script src="../js/app.js"></script>
```

## 🎨 Estilos CSS

- El archivo `css/style.css` contiene todos los estilos
- Usa las variables CSS definidas en `:root` para colores, espaciado, etc.
- Las clases de utilidad están disponibles (`.btn`, `.card`, `.alert`, etc.)

## 💻 Scripts JavaScript

- El archivo `js/app.js` contiene toda la lógica del frontend
- Define funciones para:
  - Comunicación con el backend (fetch)
  - Gestión de autenticación (token, usuario_id)
  - Operaciones de bolsillos, pagos, saldo
  - Actualizaciones de UI (badges, modales)

## 🔗 Configuración de la API

La URL base del backend está definida en `js/app.js`:

```javascript
const API_BASE = "http://localhost:5000";
```

Si deseas cambiarla, solo edita esta línea.

## 📱 Características

- ✅ Autenticación con JWT
- ✅ Gestión de bolsillos de ahorro
- ✅ Pagos automáticos
- ✅ Visualización de saldo
- ✅ Panel de administrador
- ✅ Sincronización entre pestañas
- ✅ Diseño responsivo

## 🐛 Debugging

- Abre las herramientas de desarrollador (F12)
- Revisa la consola para errores
- Revisa la pestaña "Network" para ver llamadas a la API
- Verifica que localStorage tiene `token` y `usuario_id`

## 📝 Notas

- Los datos se almacenan en `localStorage` (no usar para datos sensibles en producción)
- El backend debe estar corriendo y accesible desde el frontend
- CORS está habilitado en el backend para desarrollo local
