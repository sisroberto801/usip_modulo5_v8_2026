from django.urls import path
from . import views

urlpatterns = [
    # Vista HTML para frontend
    path('tasks', views.tareas_view, name='tareas_view'),
    
    # APIs REST - ViewSets
    path('person', views.PersonaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('person/<int:pk>', views.PersonaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    
    path('task-types', views.TipoTareaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('task-types/<int:pk>', views.TipoTareaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    
    # APIs personalizadas
    path('tasks-statistics', views.tareas_estadisticas, name='tareas_estadisticas'),
    path('person/<int:person_id>/tasks', views.tareas_por_persona, name='tareas_por_persona'),
    path('all-tasks', views.todas_tareas, name='todas_tareas'),
]
