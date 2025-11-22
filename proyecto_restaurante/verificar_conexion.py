#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para verificar la conexión a PostgreSQL y crear la base de datos
"""
import sys
import psycopg2

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Contraseñas comunes a probar
contraseñas = [
    'laura1076502740',
    'laura12345',
    'postgres',
    'admin',
    '123456',
    '',  # Sin contraseña
]

print("=" * 60)
print("VERIFICACION DE CONEXION A POSTGRESQL")
print("=" * 60)
print()

# Intentar con cada contraseña
for password in contraseñas:
    try:
        print(f"Probando contraseña: {'(vacía)' if not password else '***'}")
        conn = psycopg2.connect(
            host='localhost',
            port='5432',
            user='postgres',
            password=password
        )
        
        print(f"¡EXITO! Contraseña correcta: {'(vacía)' if not password else password}")
        print()
        
        # Verificar si la base de datos existe
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'restaurante_db'")
        existe = cursor.fetchone()
        
        if existe:
            print("La base de datos 'restaurante_db' YA EXISTE.")
        else:
            print("Creando base de datos 'restaurante_db'...")
            conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cursor.execute('CREATE DATABASE restaurante_db')
            print("¡Base de datos 'restaurante_db' creada exitosamente!")
        
        cursor.close()
        conn.close()
        
        print()
        print("=" * 60)
        print("CONTRASEÑA CORRECTA ENCONTRADA!")
        print(f"Actualiza settings.py con: 'PASSWORD': '{password}',")
        print("=" * 60)
        break
        
    except psycopg2.OperationalError as e:
        if 'password' in str(e).lower() or 'autentificaci' in str(e).lower():
            print("  -> Contraseña incorrecta")
        else:
            print(f"  -> Error de conexion: {e}")
        continue
    except Exception as e:
        print(f"  -> Error: {e}")
        continue
else:
    print()
    print("=" * 60)
    print("NO SE PUDO CONECTAR CON NINGUNA CONTRASEÑA")
    print("=" * 60)
    print()
    print("Por favor:")
    print("1. Abre pgAdmin")
    print("2. Conecta a PostgreSQL (ingresa tu contraseña)")
    print("3. Verifica cuál es tu contraseña real")
    print("4. Actualiza settings.py con la contraseña correcta")
    print()
    print("O crea la base de datos manualmente:")
    print("  - Abre pgAdmin")
    print("  - Click derecho en 'Databases' -> 'Create' -> 'Database'")
    print("  - Nombre: restaurante_db")

