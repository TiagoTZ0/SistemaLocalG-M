from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import mimetypes
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# 1. IMPORTANTE: Importamos las nuevas funciones del controlador
from controllers.producto_controller import obtener_productos, crear_producto, actualizar_producto, eliminar_producto

# Definimos la ruta base donde están los archivos estáticos del frontend
# Nota: Se calcula desde la carpeta backend hacia la carpeta frontend (padre/frontend)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_BASE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'frontend')

class RequestHandler(BaseHTTPRequestHandler):
    
    # Configuración de cabeceras (CORS) para que el Frontend (HTML) pueda hablar con el Backend
    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    # --- MANEJO DE PETICIONES GET (API y Archivos Estáticos) ---
    def do_GET(self):
        
        # 1. MANEJO DE RUTAS API
        if self.path == '/api/productos':
            self._set_headers()
            productos = obtener_productos()
            self.wfile.write(json.dumps(productos).encode())
            return
            
        # 2. MANEJO DE ARCHIVOS ESTÁTICOS Y RUTA RAÍZ (Frontend)
        
        # Lógica para determinar el archivo solicitado:
        
        # a) Si se solicita la raíz ('/'), servimos index.html
        if self.path == '/':
            requested_file = os.path.join(FRONTEND_BASE_DIR, 'index.html')
        
        # b) Si se solicita cualquier otro archivo (CSS, JS, HTML de pages/):
        else:
            # Quitamos la barra inicial y unimos a la carpeta 'frontend'
            requested_file = os.path.join(FRONTEND_BASE_DIR, self.path.lstrip('/'))

        # Determina el tipo MIME del archivo (text/html, text/css, application/javascript)
        content_type, _ = mimetypes.guess_type(requested_file)
        if content_type is None:
            # Agregar tipos MIME personalizados
            if requested_file.endswith('.svg'):
                content_type = 'image/svg+xml'
            else:
                content_type = 'application/octet-stream' # Tipo por defecto

        try:
            # Abre y sirve el archivo
            with open(requested_file, 'rb') as file:
                self._set_headers(status=200, content_type=content_type)
                self.wfile.write(file.read())
            return

        except FileNotFoundError:
            # Para SPA: Si el router.js está en el archivo estático (index.html),
            # servimos index.html de nuevo en caso de que sea una ruta interna como /home.
            # Esto permite que tu router.js maneje la vista.
            if not self.path.startswith('/assets/'):
                try:
                    requested_file = os.path.join(FRONTEND_BASE_DIR, 'index.html')
                    with open(requested_file, 'rb') as file:
                        self._set_headers(status=200, content_type='text/html')
                        self.wfile.write(file.read())
                    return
                except FileNotFoundError:
                    pass # Si ni siquiera index.html existe, da 404 final

            # Si el archivo estático no se encuentra, devuelve 404
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404: Archivo no encontrado en el servidor")
            return
        
        except Exception as e:
            print(f"Error al servir archivo estático: {e}")
            self.send_response(500)
            self.end_headers()
            return


    # --- CREAR (POST) ---
    def do_POST(self):
        if self.path == '/api/productos':
            try:
                length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(length)
                data = json.loads(post_data)
                
                exito = crear_producto(data)
                
                self._set_headers()
                if exito:
                    response = {"mensaje": "Producto creado correctamente"}
                else:
                    response = {"error": "No se pudo crear el producto"}
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                print(f"Error en POST: {e}")
                self.send_response(500)
                self.end_headers()

    # --- EDITAR (PUT) - NUEVO ---
    def do_PUT(self):
        # Detectar si la URL es del tipo /api/productos/123
        if self.path.startswith('/api/productos/'):
            try:
                # Extraer el ID del final de la URL
                id_producto = self.path.split('/')[-1]
                
                length = int(self.headers['Content-Length'])
                data = json.loads(self.rfile.read(length))
                
                exito = actualizar_producto(id_producto, data)
                
                self._set_headers()
                response = {"success": True} if exito else {"error": "Fallo al actualizar"}
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                print(f"Error en PUT: {e}")
                self.send_response(500)
                self.end_headers()

    # --- ELIMINAR (DELETE) - NUEVO ---
    def do_DELETE(self):
        if self.path.startswith('/api/productos/'):
            try:
                id_producto = self.path.split('/')[-1]
                
                exito = eliminar_producto(id_producto)
                
                self._set_headers()
                response = {"success": True} if exito else {"error": "Fallo al eliminar"}
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                print(f"Error en DELETE: {e}")
                self.send_response(500)
                self.end_headers()

# Configuración de arranque
if __name__ == "__main__":
    # Para desarrollo local: usa localhost:8000
    # Para producción: configura SERVER_HOST y SERVER_PORT en .env
    host = os.environ.get('SERVER_HOST', 'localhost')
    port = int(os.environ.get('SERVER_PORT', 8000))
    
    server_address = (host, port)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print("\n" + "="*60)
    print("🚀 Sistema de Mueblería G&M - SERVIDOR LOCAL")
    print("="*60)
    print(f"✅ Servidor corriendo en: http://{host}:{port}")
    print(f"📋 Frontend: http://{host}:{port}")
    print(f"🔌 API: http://{host}:{port}/api")
    print("📌 Presiona Ctrl+C para detener el servidor")
    print("="*60 + "\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  Servidor detenido por el usuario")
    finally:
        httpd.server_close()
        print("✅ Servidor cerrado correctamente")