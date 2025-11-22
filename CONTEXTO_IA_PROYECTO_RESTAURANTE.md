# 🍽️ CONTEXTO PARA IA - SISTEMA DE GESTIÓN DE RESTAURANTE

## 📋 PROMPT DESCRIPTIVO DEL PROYECTO

Este es un **sistema completo de gestión de restaurante** desarrollado con arquitectura de separación frontend/backend. El proyecto consiste en:

### **¿Qué se ha hecho?**

Se ha implementado un sistema web full-stack para la gestión operativa de un restaurante que permite:

1. **Gestión de Platos**: Administrar el menú del restaurante (nombre, descripción, precio)
2. **Gestión de Mesas**: Controlar las mesas disponibles, su capacidad y estado
3. **Gestión de Pedidos**: Crear y gestionar pedidos asociados a mesas con múltiples platos
4. **Gestión de Reservas**: Permitir a los clientes reservar mesas con fecha, hora y cantidad de personas
5. **Gestión de Usuarios**: Registrar y administrar información de clientes (nombre, email, teléfono)

### **Arquitectura Técnica**

- **Backend**: Django 5.2.6 con Django REST Framework
  - API RESTful completa con ViewSets
  - Base de datos PostgreSQL
  - CORS configurado para comunicación con frontend
  - Serializers para validación de datos
  - Acciones personalizadas (ej: cancelar reservas, mesas disponibles)

- **Frontend**: Angular 18 (standalone components)
  - Arquitectura de componentes modulares
  - Servicios HTTP para comunicación con API
  - Routing con lazy loading
  - Interfaces TypeScript para tipado fuerte
  - Componentes reutilizables (Header, Footer)

### **Estado Actual**

El proyecto está en fase de desarrollo funcional con:
- ✅ Modelos de datos completos y migrados
- ✅ API REST completamente funcional
- ✅ Frontend con componentes para cada módulo
- ✅ Integración frontend-backend mediante servicios HTTP
- ✅ CORS configurado para desarrollo local

### **Funcionalidades Implementadas**

- CRUD completo para todas las entidades (Platos, Mesas, Pedidos, Reservas, Usuarios)
- Endpoint personalizado para obtener mesas disponibles
- Endpoint para cancelar reservas
- Limpieza automática de reservas vencidas
- Validación de datos en backend mediante serializers
- Manejo de errores en frontend con observables RxJS

---

## 🗂️ RUTAS MÁS IMPORTANTES PARA CONTEXTO DE IA

### 🔴 BACKEND - Django (proyecto_restaurante/)

#### **1. Configuración Principal**
```
proyecto_restaurante/restaurante_project/settings.py
```
**¿Por qué es importante?**
- Configuración completa de Django
- Base de datos PostgreSQL (restaurante_db)
- CORS habilitado para Angular (localhost:4200)
- Apps instaladas: rest_framework, corsheaders, restaurante
- Configuración de zona horaria (America/Bogota)

#### **2. Modelos de Datos (Core del Sistema)**
```
proyecto_restaurante/restaurante/models.py
```
**¿Por qué es importante?**
- Define la estructura completa de datos del sistema
- 5 modelos principales:
  - `Plato`: nombre, descripcion, precio
  - `Mesa`: numero, capacidad, disponible
  - `Pedido`: mesa (FK), platos (M2M), fecha, entregado
  - `Reserva`: nombre_cliente, mesa (FK), fecha, hora, cantidad_personas
  - `Usuario`: nombre, email, telefono
- Relaciones entre modelos (ForeignKeys, ManyToMany)

#### **3. Lógica de Negocio y Endpoints API**
```
proyecto_restaurante/restaurante/views.py
```
**¿Por qué es importante?**
- Contiene toda la lógica de negocio
- 5 ViewSets que implementan CRUD completo:
  - `MesaViewSet` con acción personalizada `disponibles/`
  - `PlatoViewSet`
  - `PedidoViewSet`
  - `ReservaViewSet` con lógica de limpieza de reservas vencidas y cancelación
  - `UsuarioViewSet`
- Manejo de respuestas HTTP y validaciones

#### **4. Validación de Datos**
```
proyecto_restaurante/restaurante/serializers.py
```
**¿Por qué es importante?**
- Serializers para todos los modelos
- Validación automática de datos entrantes
- Transformación de datos entre JSON y modelos Django

#### **5. Enrutamiento de la API**
```
proyecto_restaurante/restaurante/urls.py
```
**¿Por qué es importante?**
- Router de Django REST Framework
- Define todos los endpoints disponibles:
  - `/api/mesas/`
  - `/api/platos/`
  - `/api/pedidos/`
  - `/api/reservas/`
  - `/api/usuarios/`

#### **6. URLs Raíz del Proyecto**
```
proyecto_restaurante/restaurante_project/urls.py
```
**¿Por qué es importante?**
- Punto de entrada de todas las URLs
- Incluye `/api/` que redirige a las rutas de la app restaurante
- Admin de Django en `/admin/`

#### **7. Admin de Django**
```
proyecto_restaurante/restaurante/admin.py
```
**¿Por qué es importante?**
- Modelos registrados en el panel de administración
- Permite gestión manual de datos

---

### 🟢 FRONTEND - Angular (restaurante-frontend/)

#### **1. Configuración de la Aplicación**
```
restaurante-frontend/src/app/app.config.ts
```
**¿Por qué es importante?**
- Configuración global de Angular
- Providers: Router y HttpClient
- Configuración base para toda la aplicación

#### **2. Rutas de la Aplicación**
```
restaurante-frontend/src/app/app.routes.ts
```
**¿Por qué es importante?**
- Define todas las rutas del frontend:
  - `/home` → HomeComponent
  - `/platos` → PlatosComponent
  - `/reservas` → ReservasComponent
  - `/pedidos` → PedidosComponent
  - `/mesas` → MesasComponent
  - `/usuarios` → UsuariosComponent
- Redirecciones y manejo de rutas no encontradas

#### **3. Configuración de Entorno**
```
restaurante-frontend/src/environments/environment.ts
```
**¿Por qué es importante?**
- URL base de la API: `http://127.0.0.1:8000/api/`
- Configuración de producción/desarrollo

#### **4. Servicios HTTP (Comunicación con Backend)**
```
restaurante-frontend/src/app/services/
```
**¿Por qué es importante?**
- Servicios que encapsulan toda la comunicación con la API:
  - `platos.service.ts` → GET /api/platos/
  - `reservas.service.ts` → GET, POST /api/reservas/ y GET /api/mesas/
  - `mesas.service.ts` → Operaciones con mesas
  - `pedidos.service.ts` → Operaciones con pedidos
  - `usuarios.service.ts` → Operaciones con usuarios
- Uso de Observables RxJS para manejo asíncrono

#### **5. Modelos/Interfaces TypeScript**
```
restaurante-frontend/src/app/models/plato.model.ts
```
**¿Por qué es importante?**
- Define las interfaces TypeScript que corresponden a los modelos del backend
- Tipado fuerte para evitar errores
- Interface `Plato` como ejemplo (id, nombre, descripcion, precio)

#### **6. Componentes de la Aplicación**
```
restaurante-frontend/src/app/components/
```
**¿Por qué es importante?**
- Componentes standalone de Angular para cada módulo:
  - `home/` - Página principal
  - `platos/` - Gestión de platos (ejemplo: carga datos con PlatosService)
  - `reservas/` - Gestión de reservas
  - `pedidos/` - Gestión de pedidos
  - `mesas/` - Gestión de mesas
  - `usuarios/` - Gestión de usuarios
  - `header/` - Encabezado reutilizable
  - `footer/` - Pie de página reutilizable

#### **7. Componente Principal**
```
restaurante-frontend/src/app/app.component.ts
```
**¿Por qué es importante?**
- Componente raíz de la aplicación
- Incluye Header y Footer globales
- Router outlet para renderizar componentes según la ruta

---

## 🔗 ENDPOINTS API COMPLETOS

### Base URL: `http://127.0.0.1:8000/api/`

| Endpoint | Métodos | Descripción |
|----------|---------|-------------|
| `/api/mesas/` | GET, POST | Listar todas las mesas / Crear nueva mesa |
| `/api/mesas/{id}/` | GET, PUT, PATCH, DELETE | Obtener/Actualizar/Eliminar mesa específica |
| `/api/mesas/disponibles/` | GET | Obtener solo mesas disponibles (acción personalizada) |
| `/api/platos/` | GET, POST | Listar todos los platos / Crear nuevo plato |
| `/api/platos/{id}/` | GET, PUT, PATCH, DELETE | Obtener/Actualizar/Eliminar plato específico |
| `/api/pedidos/` | GET, POST | Listar todos los pedidos / Crear nuevo pedido |
| `/api/pedidos/{id}/` | GET, PUT, PATCH, DELETE | Obtener/Actualizar/Eliminar pedido específico |
| `/api/reservas/` | GET, POST | Listar todas las reservas / Crear nueva reserva |
| `/api/reservas/{id}/` | GET, PUT, PATCH, DELETE | Obtener/Actualizar/Eliminar reserva específica |
| `/api/reservas/{id}/cancelar/` | POST | Cancelar una reserva activa (acción personalizada) |
| `/api/usuarios/` | GET, POST | Listar todos los usuarios / Crear nuevo usuario |
| `/api/usuarios/{id}/` | GET, PUT, PATCH, DELETE | Obtener/Actualizar/Eliminar usuario específico |

---

## 📊 ESTRUCTURA DE DATOS (Modelos)

### Plato
```python
{
    "id": int,
    "nombre": str (max 100),
    "descripcion": str,
    "precio": Decimal (max_digits=8, decimal_places=2)
}
```

### Mesa
```python
{
    "id": int,
    "numero": int,
    "capacidad": int,
    "disponible": bool (default=True)
}
```

### Pedido
```python
{
    "id": int,
    "mesa": int (FK a Mesa),
    "platos": [int] (M2M a Plato),
    "fecha": datetime (auto_now_add),
    "entregado": bool (default=False)
}
```

### Reserva
```python
{
    "id": int,
    "nombre_cliente": str (max 100),
    "mesa": int (FK a Mesa),
    "fecha": date,
    "hora": time,
    "cantidad_personas": int
}
```

### Usuario
```python
{
    "id": int,
    "nombre": str (max 100),
    "email": str (unique),
    "telefono": str (max 15, optional)
}
```

---

## 🛠️ STACK TECNOLÓGICO

### Backend
- **Framework**: Django 5.2.6
- **API**: Django REST Framework
- **Base de Datos**: PostgreSQL (restaurante_db)
- **CORS**: django-cors-headers
- **Python**: 3.x

### Frontend
- **Framework**: Angular 18
- **Arquitectura**: Standalone Components
- **HTTP**: HttpClient (Angular)
- **Reactive Programming**: RxJS 7.8
- **UI Libraries**: SweetAlert2
- **TypeScript**: 5.4.0

---

## 🚀 COMANDOS ÚTILES

### Backend (Django)
```bash
# Activar entorno virtual
cd proyecto_restaurante
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
# Servidor en: http://127.0.0.1:8000
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
# Servidor en: http://localhost:4200

# Compilar para producción
npm run build
```

---

## ⚠️ NOTAS IMPORTANTES

1. **CORS**: Configurado para permitir todas las conexiones en desarrollo (`CORS_ALLOW_ALL_ORIGINS = True`)
2. **Base de Datos**: PostgreSQL con nombre `restaurante_db`, usuario `postgres`
3. **Puertos**:
   - Backend Django: `8000`
   - Frontend Angular: `4200`
4. **Autenticación**: No implementada actualmente (solo modelos básicos)
5. **Validaciones**: Implementadas en los serializers de Django REST Framework
6. **Relaciones**: 
   - Pedido tiene ForeignKey a Mesa y ManyToMany a Plato
   - Reserva tiene ForeignKey a Mesa
7. **Acciones Personalizadas**:
   - `MesaViewSet.disponibles()` - Filtra mesas disponibles
   - `ReservaViewSet.cancelar()` - Cancela una reserva activa
   - `ReservaViewSet.list()` - Limpia automáticamente reservas vencidas

---

## 📝 ORDEN DE LECTURA RECOMENDADO PARA IA

Si una IA necesita entender el proyecto, lee en este orden:

1. **settings.py** - Entender configuración general
2. **models.py** - Entender estructura de datos
3. **serializers.py** - Entender validaciones
4. **views.py** - Entender lógica de negocio
5. **urls.py** (restaurante) - Entender endpoints
6. **urls.py** (restaurante_project) - Entender routing raíz
7. **app.routes.ts** - Entender rutas frontend
8. **environment.ts** - Entender configuración API
9. **services/** - Entender comunicación frontend-backend
10. **components/** - Entender interfaz de usuario

---

**Última actualización**: Generado mediante análisis completo del proyecto

