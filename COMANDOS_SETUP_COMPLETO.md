# 🚀 COMANDOS COMPLETOS PARA CONFIGURAR EL PROYECTO

## ⚠️ IMPORTANTE: VERIFICAR CONTRASEÑA DE POSTGRESQL

Antes de continuar, **verifica la contraseña correcta** de PostgreSQL. El error indica que la contraseña en `settings.py` no coincide.

---

## 📋 PASO A PASO COMPLETO

### 1️⃣ CREAR LA BASE DE DATOS (Elige una opción)

#### **Opción A: Usando pgAdmin (MÁS FÁCIL)**
1. Abre **pgAdmin**
2. Conecta al servidor PostgreSQL (ingresa tu contraseña real de postgres)
3. Click derecho en **"Databases"** → **"Create"** → **"Database"**
4. Nombre: `restaurante_db`
5. Owner: `postgres`
6. Click en **"Save"**

#### **Opción B: Usando línea de comandos**
Busca la ruta de PostgreSQL (normalmente está en):
```
C:\Program Files\PostgreSQL\[VERSION]\bin\psql.exe
```

Luego ejecuta:
```powershell
# Reemplaza [VERSION] con tu versión de PostgreSQL (ej: 15, 16, 17)
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres

# Dentro de psql:
CREATE DATABASE restaurante_db;
\q
```

---

### 2️⃣ ACTUALIZAR CONTRASEÑA EN SETTINGS.PY

**Abre el archivo:**
```
proyecto_restaurante/restaurante_project/settings.py
```

**Línea 102, cambia la contraseña por la correcta:**
```python
'PASSWORD': 'TU_CONTRASEÑA_REAL_DE_POSTGRES',  # Cambia esto
```

---

### 3️⃣ ACTIVAR ENTORNO VIRTUAL E INSTALAR DEPENDENCIAS

```powershell
# Navegar al proyecto
cd "C:\Users\derek\OneDrive\Documentos\uni\5 semestre\LauraP\proyecto_restaurante"

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Instalar psycopg2 (si no está instalado)
pip install psycopg2-binary
```

---

### 4️⃣ CREAR Y APLICAR MIGRACIONES

```powershell
# Asegúrate de estar en el directorio con venv activado
cd "C:\Users\derek\OneDrive\Documentos\uni\5 semestre\LauraP\proyecto_restaurante"
.\venv\Scripts\Activate.ps1

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones (crea las tablas en la base de datos)
python manage.py migrate
```

**Si funciona correctamente, verás:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, restaurante, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

---

### 5️⃣ CREAR SUPERUSUARIO (OPCIONAL)

```powershell
python manage.py createsuperuser
```

**Ingresa:**
- Username: `admin` (o el que prefieras)
- Email: `admin@restaurante.com` (o el que prefieras)
- Password: (ingresa una contraseña segura)
- Password (again): (confirma)

---

### 6️⃣ INICIAR EL SERVIDOR

```powershell
python manage.py runserver
```

**Deberías ver:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Abre en el navegador:**
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/ (para el admin de Django)

---

## 📝 COMANDOS COMPLETOS (COPIA Y PEGA TODO)

```powershell
# 1. Navegar al proyecto
cd "C:\Users\derek\OneDrive\Documentos\uni\5 semestre\LauraP\proyecto_restaurante"

# 2. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias (si falta)
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

## ✅ VERIFICACIÓN FINAL

Después de ejecutar los comandos, verifica:

1. **Base de datos creada:** Abre pgAdmin y verifica que `restaurante_db` existe
2. **Tablas creadas:** Ejecuta `python manage.py showmigrations` y todas deben tener `[X]`
3. **Servidor funcionando:** http://127.0.0.1:8000/ debe responder
4. **Admin accesible:** http://127.0.0.1:8000/admin/ debe mostrar login

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Error: "password authentication failed"
**Solución:** 
1. Abre `settings.py`
2. Cambia la contraseña en la línea 102 por la contraseña real de PostgreSQL
3. Guarda el archivo
4. Vuelve a ejecutar `python manage.py migrate`

### Error: "database does not exist"
**Solución:** 
1. Crea la base de datos primero (Paso 1)
2. Verifica que se llamó `restaurante_db` exactamente

### Error: "ModuleNotFoundError: No module named 'psycopg2'"
**Solución:**
```powershell
pip install psycopg2-binary
```

### Error: "connection refused"
**Solución:** 
1. Verifica que PostgreSQL esté corriendo
2. En Windows: Abre "Servicios" y busca "postgresql" - debe estar "En ejecución"

---

## 🎯 RESUMEN RÁPIDO

1. ✅ Crear base de datos `restaurante_db` en PostgreSQL (pgAdmin o psql)
2. ✅ Actualizar contraseña en `settings.py` línea 102
3. ✅ Activar venv: `.\venv\Scripts\Activate.ps1`
4. ✅ Instalar: `pip install psycopg2-binary`
5. ✅ Migrar: `python manage.py migrate`
6. ✅ Crear admin: `python manage.py createsuperuser`
7. ✅ Iniciar: `python manage.py runserver`

---

**¡Listo! Tu proyecto debería estar funcionando.**

