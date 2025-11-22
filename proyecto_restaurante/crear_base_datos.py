#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para crear la base de datos restaurante_db en PostgreSQL
"""
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Configuración de conexión
config = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'laura1076502740'
}

nombre_db = 'restaurante_db'

try:
    # Conectar a PostgreSQL (sin especificar base de datos)
    print("Conectando a PostgreSQL...")
    conn = psycopg2.connect(**config)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    cursor = conn.cursor()
    
    # Verificar si la base de datos ya existe
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (nombre_db,))
    existe = cursor.fetchone()
    
    if existe:
        print(f"La base de datos '{nombre_db}' ya existe.")
    else:
        # Crear la base de datos
        print(f"Creando base de datos '{nombre_db}'...")
        cursor.execute(f'CREATE DATABASE {nombre_db}')
        print(f"Base de datos '{nombre_db}' creada exitosamente!")
    
    cursor.close()
    conn.close()
    
except psycopg2.OperationalError as e:
    print(f"Error de conexion: {e}")
    print("\nPosibles soluciones:")
    print("1. Verifica que PostgreSQL este corriendo")
    print("2. Verifica que la contrasena sea correcta")
    print("3. Verifica que el usuario 'postgres' exista")
except Exception as e:
    print(f"Error: {e}")

