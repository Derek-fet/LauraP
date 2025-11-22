# 🗄️ GUÍA COMPLETA: CREAR BASE DE DATOS Y CONFIGURAR PROYECTO

## 📋 INFORMACIÓN DE CONFIGURACIÓN

**Base de Datos:** PostgreSQL  
**Nombre:** `restaurante_db`  
**Usuario:** `postgres`  
**Contraseña:** `laura1076502740` (según settings.py)  
**Host:** `localhost`  
**Puerto:** `5432`

---

## 🔧 PASO 1: CREAR LA BASE DE DATOS EN POSTGRESQL

### Opción A: Usando psql (Línea de comandos)

```bash
# Conectar a PostgreSQL como superusuario
psql -U postgres

# Una vez dentro de psql, ejecutar:
CREATE DATABASE restaurante_db;

# Verificar que se creó
\l

# Salir de psql
\q
```

### Opción B: Usando pgAdmin (Interfaz gráfica)

1. Abre pgAdmin
2. Conecta al servidor PostgreSQL
3. Click derecho en "Databases" → "Create" → "Database"
4. Nombre: `restaurante_db`
5. Owner: `postgres`
6. Click en "Save"

### Opción C: Desde PowerShell (Windows)

```powershell
# Conectar y crear la base de datos en una sola línea
psql -U postgres -c "CREATE DATABASE restaurante_db;"
```

**Si te pide contraseña:** Ingresa `laura1076502740` (o la contraseña que tengas configurada para postgres)

---

## 🐍 PASO 2: ACTIVAR ENTORNO VIRTUAL Y VERIFICAR DEPENDENCIAS

```powershell
# Navegar al directorio del proyecto
cd "C:\Users\derek\OneDrive\Documentos\uni\5 semestre\LauraP\proyecto_restaurante"

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Verificar que psycopg2 está instalado (necesario para PostgreSQL)
pip list | findstr psycopg

# Si NO está instalado, instalar:
pip install psycopg2-binary
```

---

## 🔄 PASO 3: CREAR Y APLICAR MIGRACIONES

```powershell
# Asegúrate de estar en el directorio del proyecto con venv activado
cd "C:\Users\derek\OneDrive\Documentos\uni\5 semestre\LauraP\proyecto_restaurante"
.\venv\Scripts\Activate.ps1

# Crear migraciones (si hay cambios en modelos)
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Verificar que las migraciones se aplicaron correctamente
python manage.py showmigrations
```

---

## 👤 PASO 4: CREAR SUPERUSUARIO (OPCIONAL PERO RECOMENDADO)

```powershell
# Crear usuario administrador para acceder al admin de Django
python manage.py createsuperuser

# Te pedirá:
# - Username: (ingresa un nombre, ej: admin)
# - Email: (ingresa un email, ej: admin@restaurante.com)
# - Password: (ingresa una contraseña segura)
# - Password (again): (confirma la contraseña)
```

---

## ✅ PASO 5: VERIFICAR QUE TODO FUNCIONA

```powershell
# Verificar conexión a la base de datos
python manage.py check --database default

# Verificar que el servidor inicia correctamente
python manage.py runserver

# Si todo está bien, verás:
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
```

---

## 🚀 PASO 6: INICIAR EL SERVIDOR

```powershell
# Con el entorno virtual activado
python manage.py runserver

# El servidor estará disponible en:
# http://127.0.0.1:8000/
# http://localhost:8000/

# Admin de Django:
# http://127.0.0.1:8000/admin/
```

---

## 🔍 COMANDOS ÚTILES ADICIONALES

### Ver todas las tablas creadas
```powershell
python manage.py dbshell
# Dentro de psql:
\dt
# Para salir:
\q
```

### Ver el estado de las migraciones
```powershell
python manage.py showmigrations
```

### Resetear la base de datos (CUIDADO: borra todos los datos)
```powershell
# Eliminar todas las tablas y recrearlas
python manage.py flush

# O eliminar y recrear desde cero:
# 1. Eliminar la base de datos en PostgreSQL
# 2. Crearla de nuevo
# 3. Ejecutar: python manage.py migrate
```

### Cargar datos iniciales (si tienes fixtures)
```powershell
python manage.py loaddata nombre_del_fixture.json
```

---

## ⚠️ SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "password authentication failed"
**Solución:** Verifica que la contraseña en `settings.py` coincida con la de PostgreSQL
```python
# En settings.py, línea 102
'PASSWORD': 'laura1076502740',  # Cambia esta si es necesario
```

### Error: "database does not exist"
**Solución:** Crea la base de datos primero (Paso 1)

### Error: "ModuleNotFoundError: No module named 'psycopg2'"
**Solución:** 
```powershell
pip install psycopg2-binary
```

### Error: "connection refused"
**Solución:** Verifica que PostgreSQL esté corriendo
```powershell
# En Windows, verificar servicio:
Get-Service -Name postgresql*
```

---

## 📝 RESUMEN DE COMANDOS COMPLETOS (COPIA Y PEGA)

```powershell
# 1. Crear base de datos (en psql o pgAdmin)
psql -U postgres -c "CREATE DATABASE restaurante_db;"

# 2. Activar entorno virtual
cd "C:\Users\derek\OneDrive\Documentos\uni\5 semestre\LauraP\proyecto_restaurante"
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias (si falta algo)
pip install psycopg2-binary

# 4. Crear migraciones
python manage.py makemigrations

# 5. Aplicar migraciones
python manage.py migrate

# 6. Crear superusuario (opcional)
python manage.py createsuperuser

# 7. Iniciar servidor
python manage.py runserver
```

---

## ✅ CHECKLIST FINAL

- [ ] Base de datos `restaurante_db` creada en PostgreSQL
- [ ] Entorno virtual activado
- [ ] `psycopg2-binary` instalado
- [ ] Migraciones creadas (`makemigrations`)
- [ ] Migraciones aplicadas (`migrate`)
- [ ] Superusuario creado (opcional)
- [ ] Servidor Django corriendo sin errores
- [ ] Puedes acceder a http://127.0.0.1:8000/admin/

---

**¡Listo! Tu proyecto debería estar funcionando correctamente con PostgreSQL.**

