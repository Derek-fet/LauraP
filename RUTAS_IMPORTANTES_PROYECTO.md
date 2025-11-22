# 📋 RUTAS IMPORTANTES DEL PROYECTO RESTAURANTE

## 🎯 RESUMEN DEL PROYECTO
Sistema de gestión de restaurante con:
- **Backend**: Django REST Framework (Python)
- **Frontend**: Angular 18 (TypeScript)
- **Base de Datos**: PostgreSQL
- **Arquitectura**: API REST con CORS habilitado

---

## 🔴 BACKEND - DJANGO (Rutas Críticas)

### 1. **Configuración Principal**
```
proyecto_restaurante/restaurante_project/settings.py
```
- Configuración de Django
- Base de datos PostgreSQL
- CORS configurado para Angular (localhost:4200)
- Apps instaladas: `rest_framework`, `corsheaders`, `restaurante`

### 2. **URLs Principales**
```
proyecto_restaurante/restaurante_project/urls.py
```
- Ruta base: `/api/` → incluye las rutas de la app `restaurante`

### 3. **Modelos de Datos**
```
proyecto_restaurante/restaurante/models.py
```
**Modelos principales:**
- `Plato`: nombre, descripcion, precio
- `Mesa`: numero, capacidad, disponible
- `Pedido`: mesa (FK), platos (M2M), fecha, entregado
- `Reserva`: nombre_cliente, mesa (FK), fecha, hora, cantidad_personas
- `Usuario`: nombre, email, telefono

### 4. **Vistas/ViewSets (API Endpoints)**
```
proyecto_restaurante/restaurante/views.py
```
**ViewSets disponibles:**
- `MesaViewSet` → `/api/mesas/`
  - Acción personalizada: `disponibles/` (GET)
- `PlatoViewSet` → `/api/platos/`
- `PedidoViewSet` → `/api/pedidos/`
- `ReservaViewSet` → `/api/reservas/`
  - Acciones: `list()`, `create()`, `cancelar/` (POST)
- `UsuarioViewSet` → `/api/usuarios/`

### 5. **Serializers (Validación de Datos)**
```
proyecto_restaurante/restaurante/serializers.py
```
- Serializers para todos los modelos (Mesa, Plato, Pedido, Reserva, Usuario)

### 6. **URLs de la App**
```
proyecto_restaurante/restaurante/urls.py
```
- Router de Django REST Framework
- Endpoints registrados: mesas, platos, pedidos, reservas, usuarios

### 7. **Admin de Django**
```
proyecto_restaurante/restaurante/admin.py
```
- Modelos registrados en el admin: Plato, Mesa, Pedido

### 8. **Migrations (Esquema de BD)**
```
proyecto_restaurante/restaurante/migrations/
```
- `0001_initial.py` - Migración inicial
- `0002_reserva.py` - Modelo Reserva
- `0003_usuario.py` - Modelo Usuario
- `0004_mesa_disponible_alter_mesa_capacidad_and_more.py` - Cambios en Mesa

### 9. **Archivo de Gestión**
```
proyecto_restaurante/manage.py
```
- Punto de entrada para comandos Django

---

## 🟢 FRONTEND - ANGULAR (Rutas Críticas)

### 1. **Configuración Principal**
```
restaurante-frontend/src/app/app.config.ts
```
- Configuración de la aplicación Angular
- Providers: Router, HttpClient

### 2. **Rutas de la Aplicación**
```
restaurante-frontend/src/app/app.routes.ts
```
**Rutas definidas:**
- `/` → redirige a `home`
- `/home` → HomeComponent
- `/platos` → PlatosComponent
- `/reservas` → ReservasComponent
- `/pedidos` → PedidosComponent
- `/mesas` → MesasComponent
- `/usuarios` → UsuariosComponent
- `/**` → redirige a `home` (404)

### 3. **Componente Principal**
```
restaurante-frontend/src/app/app.component.ts
```
- Componente raíz con Header y Footer

### 4. **Servicios (Comunicación con API)**
```
restaurante-frontend/src/app/services/
```
**Servicios disponibles:**
- `platos.service.ts` → `http://127.0.0.1:8000/api/platos/`
- `reservas.service.ts` → `http://127.0.0.1:8000/api/reservas/`
- `mesas.service.ts` → `http://127.0.0.1:8000/api/mesas/`
- `pedidos.service.ts` → `http://127.0.0.1:8000/api/pedidos/`
- `usuarios.service.ts` → `http://127.0.0.1:8000/api/usuarios/`

### 5. **Modelos/Interfaces TypeScript**
```
restaurante-frontend/src/app/models/plato.model.ts
```
- Interface `Plato` con: id, nombre, descripcion, precio

### 6. **Componentes**
```
restaurante-frontend/src/app/components/
```
**Componentes disponibles:**
- `home/` - Página principal
- `platos/` - Gestión de platos
- `reservas/` - Gestión de reservas
- `pedidos/` - Gestión de pedidos
- `mesas/` - Gestión de mesas
- `usuarios/` - Gestión de usuarios
- `header/` - Encabezado
- `footer/` - Pie de página

### 7. **Configuración de Entorno**
```
restaurante-frontend/src/environments/environment.ts
```
- `apiUrl: 'http://127.0.0.1:8000/api/'`

### 8. **Configuración del Proyecto**
```
restaurante-frontend/package.json
```
- Dependencias: Angular 18, RxJS, SweetAlert2
- Scripts: start, build, test

---

## 🔗 ENDPOINTS API COMPLETOS

### Base URL: `http://127.0.0.1:8000/api/`

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/api/mesas/` | GET, POST | Listar/Crear mesas |
| `/api/mesas/{id}/` | GET, PUT, PATCH, DELETE | Operaciones CRUD de mesa |
| `/api/mesas/disponibles/` | GET | Mesas disponibles |
| `/api/platos/` | GET, POST | Listar/Crear platos |
| `/api/platos/{id}/` | GET, PUT, PATCH, DELETE | Operaciones CRUD de plato |
| `/api/pedidos/` | GET, POST | Listar/Crear pedidos |
| `/api/pedidos/{id}/` | GET, PUT, PATCH, DELETE | Operaciones CRUD de pedido |
| `/api/reservas/` | GET, POST | Listar/Crear reservas |
| `/api/reservas/{id}/` | GET, PUT, PATCH, DELETE | Operaciones CRUD de reserva |
| `/api/reservas/{id}/cancelar/` | POST | Cancelar reserva |
| `/api/usuarios/` | GET, POST | Listar/Crear usuarios |
| `/api/usuarios/{id}/` | GET, PUT, PATCH, DELETE | Operaciones CRUD de usuario |

---

## 📊 ESTRUCTURA DE DATOS

### Plato
```typescript
{
  id: number;
  nombre: string;
  descripcion: string;
  precio: number;
}
```

### Mesa
```typescript
{
  id: number;
  numero: number;
  capacidad: number;
  disponible: boolean;
}
```

### Pedido
```typescript
{
  id: number;
  mesa: number; // FK
  platos: number[]; // M2M
  fecha: string; // DateTime
  entregado: boolean;
}
```

### Reserva
```typescript
{
  id: number;
  nombre_cliente: string;
  mesa: number; // FK
  fecha: string; // Date
  hora: string; // Time
  cantidad_personas: number;
}
```

### Usuario
```typescript
{
  id: number;
  nombre: string;
  email: string;
  telefono?: string;
}
```

---

## 🚀 COMANDOS ÚTILES

### Backend (Django)
```bash
# Activar entorno virtual
cd proyecto_restaurante
venv\Scripts\activate  # Windows

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### Frontend (Angular)
```bash
# Instalar dependencias
cd restaurante-frontend
npm install

# Ejecutar servidor de desarrollo
npm start
# o
ng serve

# Compilar para producción
npm run build
```

---

## ⚠️ NOTAS IMPORTANTES

1. **CORS**: Configurado para permitir todas las conexiones en desarrollo (`CORS_ALLOW_ALL_ORIGINS = True`)
2. **Base de Datos**: PostgreSQL con nombre `restaurante_db`
3. **Puertos**:
   - Backend: `8000` (Django)
   - Frontend: `4200` (Angular)
4. **Autenticación**: No implementada actualmente (solo modelos básicos)
5. **Validaciones**: Implementadas en los serializers de Django

---

## 📝 ARCHIVOS ADICIONALES

- `baserestaurante.sql` - Script SQL de la base de datos (si existe)
- `restaurante-frontend/src/app/imagenes/` - Recursos estáticos

---

**Última actualización**: Generado automáticamente mediante escaneo del proyecto

