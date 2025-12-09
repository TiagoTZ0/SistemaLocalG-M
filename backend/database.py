import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
    Conecta a la base de datos Supabase PostgreSQL
    Asegúrate de configurar las variables en el archivo .env
    """
    try:
        host = os.environ.get("SUPABASE_HOST")
        user = os.environ.get("SUPABASE_USER")
        password = os.environ.get("SUPABASE_PASSWORD")
        port = os.environ.get("SUPABASE_PORT", "5432")
        
        if not all([host, user, password]):
            raise ValueError("Variables de entorno incompletas. Configura SUPABASE_HOST, SUPABASE_USER, SUPABASE_PASSWORD en .env")
        
        print(f"[BD] Conectando a Supabase: {host}")
        
        conn = psycopg2.connect(
            host=host,
            database="postgres",
            user=user,
            password=password,
            port=port,
            sslmode='require'  # Supabase requiere SSL
        )
        print("[BD] Conexión exitosa a Supabase")
        return conn
    except Exception as e:
        print(f"[ERROR BD] No se pudo conectar a Supabase: {e}")
        print("[AVISO] Asegúrate de:")
        print("  1. Configurar las credenciales en el archivo .env")
        print("  2. Que la base de datos en Supabase esté disponible")
        print("  3. Que tu conexión a internet funcione")
        return None