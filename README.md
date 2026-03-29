# PROYECTO MÓDULO V - DJANGO

## Datos del Estudiante:

- Roberto Carlos Olguin Ledezma
- Fecha: Marzo 2026

## 1. Propósito:

Demostrar los conocimientos adquiridos en la creación de un proyecto en Django.

## 2. Requerimientos:

- Cree un Proyecto en Django con al menos una Aplicación
- Su Aplicación debe tener al menos 4 Models (Modelos o Tablas)
- Sus Models deben contener al menos 2 validaciones personalizadas
- Su Administrador de Django debe tener al menos 2 Models registrados
- Utilice Django Rest Framework para crear al menos 3 ModelViewSet o GenericAPIView
- Utilice Django Rest Framework para crear al menos 1 Custom API
- Debe incluir el archivo requirements.txt en la raíz del repositorio

## 3. Implementación:

✅ **Proyecto Django:** `ecoapp` con aplicación `proyecto`  
✅ **4 Models:** `Persona`, `TipoTarea`, `Tarea`, `TareaAsignada` en app `proyecto`  
✅ **Validaciones personalizadas:** Fecha de nacimiento futura, rango de prioridad, fechas de tarea, email único  
✅ **Admin Django:** 4 models registrados con configuraciones personalizadas  
✅ **DRF ViewSets:** `PersonaViewSet`, `TipoTareaViewSet` en app `proyecto`  
✅ **Custom APIs:** `tareas_estadisticas`, `tareas_por_persona` en app `proyecto`  
✅ **requirements.txt:** Incluido con todas las dependencias necesarias

## Instalar dependencias

- Se recomienda utilizar un entorno virtual (virtualenv)

```sh
pip install -r requirements.txt
```

## Ejecutar servidor de desarrollo

```sh
python manage.py runserver
```

## Crear SuperAdministrador

```sh
python manage.py createsuperuser
```

## API Endpoints Disponibles:

### ViewSets (CRUD Operations):

- `GET/POST /proyecto/personas` - Listar y crear personas
- `GET/PUT/DELETE /proyecto/personas/{id}/` - Detalle, actualizar y eliminar persona
- `GET/POST /proyecto/tipos-tarea` - Listar y crear tipos de tarea
- `GET/PUT/DELETE /proyecto/tipos-tarea/{id}/` - Detalle, actualizar y eliminar tipo de tarea

### Custom APIs:

- `GET /proyecto/tareas-estadisticas` - Estadísticas de tareas (totales, completadas, por tipo, etc.)
- `GET /proyecto/personas/{persona_id}/tareas` - Todas las tareas asignadas a una persona específica

### Parámetros de búsqueda y ordenamiento:

- **Personas:** `?search=nombre` `?ordering=apellido`
- **Tipos Tarea:** `?ordering=prioridad` `?ordering=nombre`

### Autenticación:

- AllowAny (sin requerir autenticación para desarrollo)
- Session Authentication (para admin de Django es user:admin / pass:admin)

Todos los endpoints tienen acceso público sin requerir autenticación.
