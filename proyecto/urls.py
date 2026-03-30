from django.urls import path
from . import views

urlpatterns = [
    # Vista HTML para frontend
    path('tareas/', views.tareas_view, name='tareas_view'),
    
    # APIs REST - ViewSets
    path('personas', views.PersonaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('personas/<int:pk>/', views.PersonaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    
    path('tipos-tarea/', views.TipoTareaViewSet.as_view({
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
    path('todas-tareas/', views.todas_tareas, name='todas_tareas'),
]
