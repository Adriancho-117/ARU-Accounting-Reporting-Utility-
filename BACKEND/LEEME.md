# Backend - ARU (Sistema de Gestión Financiera)

## 📁 Estructura

```
backend/
├── app.py                 # Aplicación principal Flask
├── db.py                  # Funciones de base de datos
├── init_db.sql           # Script para inicializar BD
├── requirements.txt      # Dependencias Python
├── routes/               # Rutas/endpoints de la API
│   ├── __init__.py
│   ├── usuarios.py       # Endpoints de autenticación
│   ├── bolsillos.py      # Endpoints de bolsillos
│   ├── saldo.py          # Endpoints de saldo
│   └── admin.py          # Endpoints administrativos
├── services/             # Servicios/lógica de negocio
│   ├── __init__.py
│   └── auth_service.py   # Funciones de autenticación
└── LEEME.md              # Este archivo
```

## 🚀 Instalación y Setup

### 1. Requisitos
- Python 3.8+
- SQLite (incluido en Python)

### 2. Instalar dependencias
```bash
cd backend
pip install -r requirements.txt
```

### 3. Inicializar base de datos
```bash
sqlite3 < init_db.sql
```

### 4. Ejecutar el servidor
```bash
python app.py
```
El servidor estará disponible en: `http://localhost:5000`

## 📋 Dependencias

Ver `requirements.txt` para la lista completa:
- **Flask**: Framework web
- **Flask-CORS**: Soporte para CORS
- **PyJWT**: Autenticación con JWT
- **SQLite3**: Base de datos

## 🔌 API Endpoints

### Autenticación (usuarios.py)
- `POST /registro` - Registrar nuevo usuario
- `POST /login` - Iniciar sesión
- `POST /login/admin` - Iniciar sesión como admin

### Bolsillos (bolsillos.py)
- `GET /api/bolsillos` - Listar bolsillos del usuario
- `POST /api/bolsillos/create` - Crear nuevo bolsillo
- `PUT /api/bolsillos/<id>` - Actualizar bolsillo
- `DELETE /api/bolsillos/<id>` - Eliminar bolsillo

### Saldo (saldo.py)
- `GET /saldo/<usuario_id>` - Obtener saldo del usuario
- `POST /saldo/add` - Agregar dinero
- `POST /saldo/subtract` - Restar dinero

### Pagos Automáticos (usuarios.py)
- `GET /pagos_automaticos/<usuario_id>` - Listar pagos
- `POST /pagos_automaticos` - Crear pago automático
- `DELETE /pagos_automaticos/<id>` - Eliminar pago

### Admin (admin.py)
- `GET /admin/users` - Listar todos los usuarios
- `DELETE /admin/users/<id>` - Eliminar usuario
- `GET /admin/reports` - Reportes del sistema

## 🔐 Autenticación

El sistema usa **JWT (JSON Web Tokens)**:

1. El usuario se registra/inicia sesión
2. El servidor retorna un `token` JWT
3. El frontend almacena el token en `localStorage`
4. En cada petición al backend, se envía el token en el header:
   ```
   Authorization: Bearer <token>
   ```
5. El backend valida el token antes de procesar la petición

## 🗄️ Base de Datos

### Tablas principales

**usuarios**
- `id`: Identificador único
- `email`: Email del usuario
- `contraseña`: Hash de la contraseña
- `nombre`: Nombre del usuario
- `rol`: 'usuario' o 'admin'
- `created_at`: Fecha de creación

**bolsillos**
- `id`: Identificador único
- `usuario_id`: ID del usuario propietario
- `nombre`: Nombre del bolsillo
- `saldo`: Cantidad de dinero
- `fecha`: Fecha de desembolso
- `created_at`: Fecha de creación

**pagos_automaticos**
- `id`: Identificador único
- `usuario_id`: ID del usuario
- `nombre`: Nombre del pago
- `monto`: Cantidad
- `fecha`: Fecha del pago
- `created_at`: Fecha de creación

## 🛠️ Desarrollo

### Agregar nuevo endpoint

1. Crear función en el archivo de rutas correspondiente:
```python
# routes/ejemplo.py
from flask import Blueprint, request

ejemplo_bp = Blueprint('ejemplo', __name__)

@ejemplo_bp.route('/ejemplo', methods=['GET'])
def get_ejemplo():
    return {'mensaje': 'Hola'}
```

2. Registrar el blueprint en `app.py`:
```python
from routes.ejemplo import ejemplo_bp
app_aru.register_blueprint(ejemplo_bp)
```

### Agregar nueva tabla

1. Crear la tabla en `init_db.sql`
2. Crear funciones de acceso en `db.py` si es necesario
3. Usar en las rutas según sea necesario

## 🔍 Debugging

- Revisa la consola de Python para logs del servidor
- Usa `print()` o `app_aru.logger.info()` para debugging
- Verifica los requests/responses en Network Tab del frontend

## 🚨 Seguridad (Nota para Producción)

- ⚠️ La contraseña debe ser hasheada (usar `werkzeug.security`)
- ⚠️ CORS solo está habilitado para desarrollo
- ⚠️ El JWT secret key debe ser más seguro
- ⚠️ Validar y sanitizar todas las entradas del usuario
- ⚠️ No guardar datos sensibles en localStorage en producción

## 📝 Configuración

Editar en `app.py`:
```python
app_aru = Flask(__name__)
app_aru.config['SECRET_KEY'] = 'tu-clave-secreta-aqui'  # Cambiar en producción
```

## 🤝 Integración con Frontend

El frontend en la carpeta `frontend/` se conecta a los endpoints aquí definidos usando `fetch()` API.

URL base configurada: `http://localhost:5000`
