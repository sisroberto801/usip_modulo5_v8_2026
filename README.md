# Ecoapp

## Datos del Estudiante:

- Roberto Carlos Olguin Ledezma
- Fecha: Marzo 2026

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

## Cargar datos iniciales de Inventario

```sh
python manage.py loaddata dump_inventario.json
```

## API Endpoints Disponibles:

### ViewSets (CRUD Operations):

- `GET/POST /inventario/personas/` - Listar y crear personas
- `GET/PUT/DELETE /inventario/personas/{id}/` - Detalle, actualizar y eliminar persona
- `GET/POST /inventario/tipos-tarea/` - Listar y crear tipos de tarea
- `GET/PUT/DELETE /inventario/tipos-tarea/{id}/` - Detalle, actualizar y eliminar tipo de tarea

### Custom APIs:

- `GET /inventario/tareas-estadisticas/` - Estadísticas de tareas (totales, completadas, por tipo, etc.)
- `GET /inventario/personas/{persona_id}/tareas/` - Todas las tareas asignadas a una persona específica

### Parámetros de búsqueda y ordenamiento:

- **Personas:** `?search=nombre` `?ordering=apellido`
- **Tipos Tarea:** `?ordering=prioridad` `?ordering=nombre`

### Autenticación:

- AllowAny (sin requerir autenticación para desarrollo)
- Session Authentication (para admin de Django)
- Basic Authentication (para desarrollo/testing)

Todos los endpoints tienen acceso público sin requerir autenticación.
