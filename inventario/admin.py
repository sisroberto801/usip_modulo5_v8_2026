from django.contrib import admin

from .models import Categoria, Producto, Persona, TipoTarea, Tarea, TareaAsignada

admin.site.register(Categoria)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'unidades', 'precio')
    ordering = ('precio',)
    search_fields = ('nombre',)
    list_filter = ('unidades',)


admin.site.register(Producto, ProductoAdmin)


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('fecha_nacimiento',)


admin.site.register(Persona, PersonaAdmin)


class TipoTareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'prioridad')
    search_fields = ('nombre',)
    list_filter = ('prioridad',)


admin.site.register(TipoTarea, TipoTareaAdmin)


class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_tarea', 'fecha_inicio', 'fecha_fin', 'completada')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('tipo_tarea', 'completada', 'fecha_inicio')


admin.site.register(Tarea, TareaAdmin)


class TareaAsignadaAdmin(admin.ModelAdmin):
    list_display = ('tarea', 'persona', 'fecha_asignacion', 'completada')
    search_fields = ('tarea__titulo', 'persona__nombre', 'persona__apellido')
    list_filter = ('completada', 'fecha_asignacion')


admin.site.register(TareaAsignada, TareaAsignadaAdmin)
