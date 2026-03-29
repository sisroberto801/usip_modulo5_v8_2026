from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact),
    path('categorias', views.categorias, name='categorias'),
    path('productos', views.productoFormView),
    path('clase8', views.index),
    
    # APIs REST - ViewSets sin Router
    path('personas', views.PersonaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('personas/<int:pk>/', views.PersonaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    
    path('tipos-tarea', views.TipoTareaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('tipos-tarea/<int:pk>/', views.TipoTareaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    
    # APIs personalizadas
    path('tareas-estadisticas/', views.tareas_estadisticas, name='tareas_estadisticas'),
    path('personas/<int:persona_id>/tareas/', views.tareas_por_persona, name='tareas_por_persona'),
]

