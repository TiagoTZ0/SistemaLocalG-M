# Sistema de Mueblería G&M - Versión Local (Sin Frameworks)

Sistema completo de gestión de mueblería con **HTML/CSS/JavaScript vanilla** (sin frameworks) en el frontend y **Python puro** (sin frameworks como Flask/Django) en el backend. 

**Base de datos**: Supabase PostgreSQL en la nube.

## 🎯 Características Principales

✅ Frontend completamente vanilla (HTML/CSS/JS puro)
✅ Backend Python sin frameworks
✅ Base de datos en Supabase PostgreSQL
✅ Ejecución completamente local
✅ API REST integrada
✅ Autenticación con LocalStorage
✅ Sistema de productos, clientes, pedidos y reportes

## 📁 Estructura del Proyecto

```
sistemagmnoframework/
├── .env                   # Variables de entorno (Supabase)
├── requirements.txt       # Dependencias Python
├── start_server.bat      # Script para iniciar (Windows)
│
├── frontend/
│   ├── index.html        # Página principal
│   ├── pages/            # Páginas HTML
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── home.html
│   │   ├── productos.html
│   │   ├── clientes.html
│   │   ├── pedidos.html
│   │   ├── reportes.html
│   │   └── admin.html
│   └── assets/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           ├── app.js
│           ├── router.js
│           └── pages/
│               ├── login.js
│               ├── register.js
│               ├── home.js
│               └── productos.js
│
└── backend/
    ├── server.py              # Servidor HTTP local
    ├── database.py            # Conexión a Supabase
    └── controllers/
        └── producto_controller.py
```

## 🚀 Guía de Inicio Rápido

### Requisitos Previos

- **Python 3.7+** - [Descargar aquí](https://www.python.org/downloads/)
- **Cuenta en Supabase** - [Crear cuenta gratuita](https://supabase.com)
- **Navegador moderno** - Chrome, Firefox, Safari o Edge

### Paso 1: Configurar Supabase

1. Ingresa a [Supabase](https://supabase.com) y crea un proyecto
2. Copia tus credenciales:
   - Host (proyecto.supabase.co)
   - Puerto (5432)
   - Usuario (postgres)
   - Contraseña

### Paso 2: Configurar Variables de Entorno

Edita el archivo `.env` dentro de la carpeta backend del proyecto:

```env
# Configuración de Supabase
SUPABASE_HOST=tu-proyecto.supabase.co
SUPABASE_PORT=5432
SUPABASE_USER=postgres
SUPABASE_PASSWORD=tu-contraseña

# Configuración del servidor local
SERVER_HOST=localhost
SERVER_PORT=8000
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Iniciar el Servidor

#### Opción 1: Ejecutar script (Recomendado para Windows)

```bash
# Haz doble clic en:
start_server.bat
```

#### Opción 2: Desde línea de comandos

```bash
# Abrir CMD o PowerShell en la raíz del proyecto
python backend\server.py
```

### Paso 5: Acceder a la Aplicación

Abre tu navegador y ve a:
```
http://localhost:8000
```

## 📋 Credenciales de Prueba

```
Usuario: admin
Contraseña: admin123
Rol: Admin
```

## 🔌 Endpoints de la API

```
GET  /api/productos          - Obtener todos los productos
POST /api/productos          - Crear nuevo producto
PUT  /api/productos/:id      - Actualizar producto
DEL  /api/productos/:id      - Eliminar producto
```

## 📝 Notas Importantes

### Base de Datos
- **Tipo**: PostgreSQL en Supabase (nube)
- **Requiere**: Conexión a internet para acceder a los datos
- **Ventajas**: 
  - Datos sincronizados entre dispositivos
  - Respaldo automático
  - Sin mantenimiento local

### Servidor
- **Puerto por defecto**: 8000
- **Host**: localhost
- **Dirección**: http://localhost:8000

### Frontend
- **Completamente vanilla**: Sin dependencias NPM
- **LocalStorage**: Mantiene sesión del usuario
- **Responsive**: Adaptado para mobile y desktop

## 🛠️ Solución de Problemas

### "Puerto 8000 ya está en uso"
```bash
# Cambia el puerto en .env
SERVER_PORT=8001
```

### "Error de conexión a Supabase"
- Verifica que el archivo `.env` tenga las credenciales correctas
- Asegúrate que tienes conexión a internet
- Verifica que Supabase esté disponible (revisa el estado en supabase.com)

### "Python no encontrado"
- Reinstala Python desde https://www.python.org
- Durante la instalación, marca la opción "Add Python to PATH"
- Reinicia tu computadora después de instalar

### Limpiar y reintentar
```bash
# Eliminar dependencias y reinstalar
pip uninstall -y psycopg2-binary python-dotenv
pip install -r requirements.txt
```

El servidor se iniciará en `http://localhost:8000`

### 2. Abrir el Frontend

```bash
# Opción 1: Abrir directamente el archivo HTML en el navegador
# Navega a: sistemagmnoframework/frontend/index.html

# Opción 2: Si tienes Python disponible, usa un servidor web simple:
cd sistemagmnoframework/frontend
python -m http.server 3000
# Luego abre http://localhost:3000
```

## Características Implementadas

### Frontend
- ✅ **Autenticación**: Login y registro de usuarios
- ✅ **Navegación**: Router SPA sin librerías
- ✅ **Interfaz**: Sidebar, header y content area (como Angular)
- ✅ **Gestión de Productos**: CRUD completo (Create, Read, Update, Delete)
- ✅ **Alertas**: Sistema de notificaciones flotantes
- ✅ **LocalStorage**: Almacenamiento de sesión en cliente
- ✅ **Diseño Responsive**: Adapta a diferentes tamaños de pantalla
- ✅ **CSS Variables**: Sistema de temas y colores

### Backend
- ✅ **API REST**: Endpoints CRUD para productos
- ✅ **Base de Datos JSON**: Almacenamiento en archivo local
- ✅ **CORS**: Configurado para solicitudes desde frontend
- ✅ **Validación**: Datos validados en servidor
- ✅ **Logging**: Registro de solicitudes HTTP

## Endpoints de la API

### Productos
- `GET /api/productos` - Obtener todos los productos
- `GET /api/productos/{id}` - Obtener un producto específico
- `POST /api/productos` - Crear nuevo producto
- `PUT /api/productos/{id}` - Actualizar producto
- `DELETE /api/productos/{id}` - Eliminar producto

## Credenciales de Ejemplo

**Login:**
- Usuario: `admin`
- Contraseña: `cualquier texto`
- Rol: Selecciona Admin o Vendedor

**Registro:**
- Completa el formulario y se creará una cuenta automáticamente

## Tecnologías Utilizadas

### Frontend
- HTML5 (Semántico)
- CSS3 (Variables, Flexbox, Grid)
- JavaScript ES6+
- LocalStorage API
- Fetch API

### Backend
- Python 3
- Módulo `http.server` (librería estándar)
- JSON (para persistencia)
- UUID (generación de IDs)

## Funcionalidades

### Módulo de Productos (Operativo)
- ✅ Ver lista de productos
- ✅ Agregar nuevo producto
- ✅ Eliminar producto
- ⏳ Editar producto (en desarrollo)

### Otros Módulos (Placeholders)
- 📋 Gestión de Clientes
- 📋 Gestión de Pedidos
- 📋 Reportes
- 📋 Gestión de Usuarios

## Notas de Desarrollo

1. **Sin Frameworks**: No se utilizan Angular, React, Vue, Flask, Django, etc.
2. **Datos Persistentes**: Los datos se guardan en `backend/data/productos.json`
3. **Seguridad**: Este es un prototipo educativo, no use en producción
4. **Logs**: El servidor imprime detalles de cada solicitud en la consola
5. **CORS**: Habilitado para permitir solicitudes desde el frontend local

## Solución de Problemas

### "ERR_FAILED: API Error"
- Asegúrate de que el servidor Python está corriendo en `http://localhost:8000`
- Verifica que no hay otro proceso usando el puerto 8000

### "Conexión rechazada"
- Inicia el servidor backend: `python backend/server.py`
- Espera a ver el mensaje: "🚀 Servidor iniciado en http://localhost:8000"

### "Cross-Origin Request Blocked"
- Asegúrate de que el backend tiene CORS habilitado (está configurado por defecto)
- Verifica que la URL de la API es `http://localhost:8000`

## Estructura de Datos - Producto

```json
{
  "id": "prod001",
  "descripcion": "Cama King Size",
  "sku": "CAMA001",
  "codigoBarras": "7501234567890",
  "categoria": "Muebles",
  "marca": "Ensueño",
  "precio": 1777.50,
  "stockMinimo": 5,
  "stockActual": 12,
  "fechaCreacion": "2025-01-01T10:00:00"
}
```

## Contacto y Soporte

Para reportar bugs o sugerencias, por favor abre un issue en el repositorio.

---

**Creado para aprendizaje y educación**
