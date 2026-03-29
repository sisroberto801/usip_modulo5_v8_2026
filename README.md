# Ecoapp

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
- `GET/POST /api/categorias/` - Listar y crear categorías
- `GET/PUT/DELETE /api/categorias/{id}/` - Detalle, actualizar y eliminar categoría
- `GET/POST /api/productos/` - Listar y crear productos
- `GET/PUT/DELETE /api/productos/{id}/` - Detalle, actualizar y eliminar producto
- `GET/POST /api/personas/` - Listar y crear personas
- `GET/PUT/DELETE /api/personas/{id}/` - Detalle, actualizar y eliminar persona
- `GET/POST /api/tipos-tarea/` - Listar y crear tipos de tarea
- `GET/PUT/DELETE /api/tipos-tarea/{id}/` - Detalle, actualizar y eliminar tipo de tarea

### Custom APIs:
- `GET /api/tareas-estadisticas/` - Estadísticas de tareas (totales, completadas, por tipo, etc.)
- `GET /api/personas/{persona_id}/tareas/` - Todas las tareas asignadas a una persona específica

### Parámetros de búsqueda y ordenamiento:
- **Productos:** `?search=nombre` `?ordering=precio` `?ordering=-created_at`
- **Personas:** `?search=nombre` `?ordering=apellido` 
- **Tipos Tarea:** `?ordering=prioridad` `?ordering=nombre`

### Autenticación:
- Session Authentication (para admin de Django)
- user: admin
- password: admin
- Basic Authentication (para desarrollo/testing)

Todos los endpoints tienen permisos de lectura pública y requieren autenticación para operaciones de escritura.
