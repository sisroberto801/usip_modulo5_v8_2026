from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Persona, TipoTarea, Tarea, TareaAsignada
from .serializers import (
    PersonaSerializer, TipoTareaSerializer, TareaSerializer, TareaAsignadaSerializer
)


def tareas_view(request):
    """
    Vista para mostrar el template de tareas con frontend JavaScript
    """
    return render(request, 'tareas/base.html')


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    search_fields = ['nombre', 'apellido', 'email']
    ordering_fields = ['nombre', 'apellido']


class TipoTareaViewSet(viewsets.ModelViewSet):
    queryset = TipoTarea.objects.all()
    serializer_class = TipoTareaSerializer
    ordering_fields = ['prioridad', 'nombre']


@api_view(['GET'])
def tareas_estadisticas(request):
    """
    API personalizada que devuelve estadísticas de tareas
    """
    total_tareas = TareaAsignada.objects.count()
    tareas_completadas = TareaAsignada.objects.filter(completada=True).count()
    tareas_pendientes = total_tareas - tareas_completadas
    
    tareas_por_tipo = Tarea.objects.values('tipo_tarea__nombre').annotate(
        count=Count('id')
    ).order_by('-count')
    
    asignaciones_por_persona = TareaAsignada.objects.values('persona__nombre', 'persona__apellido').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    data = {
        'total_tareas': total_tareas,
        'tareas_completadas': tareas_completadas,
        'tareas_pendientes': tareas_pendientes,
        'porcentaje_completado': round((tareas_completadas / total_tareas * 100) if total_tareas > 0 else 0, 2),
        'tareas_por_tipo': list(tareas_por_tipo),
        'top_personas_asignadas': list(asignaciones_por_persona)
    }
    
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def tareas_por_persona(request, persona_id):
    """
    API personalizada que devuelve todas las tareas asignadas a una persona específica
    """
    try:
        persona = Persona.objects.get(id=persona_id)
        tareas_asignadas = TareaAsignada.objects.filter(persona=persona).select_related('tarea', 'tarea__tipo_tarea')
        
        data = []
        for asignacion in tareas_asignadas:
            data.append({
                'id': asignacion.id,
                'tarea': {
                    'id': asignacion.tarea.id,
                    'titulo': asignacion.tarea.titulo,
                    'descripcion': asignacion.tarea.descripcion,
                    'tipo_tarea': asignacion.tarea.tipo_tarea.nombre,
                    'fecha_inicio': asignacion.tarea.fecha_inicio,
                    'fecha_fin': asignacion.tarea.fecha_fin,
                    'completada': asignacion.tarea.completada
                },
                'fecha_asignacion': asignacion.fecha_asignacion,
                'completada': asignacion.completada
            })
        
        return Response({
            'persona': {
                'id': persona.id,
                'nombre': persona.nombre,
                'apellido': persona.apellido,
                'email': persona.email
            },
            'tareas_asignadas': data,
            'total_tareas': len(data),
            'tareas_completadas': len([t for t in data if t['completada']])
        }, status=status.HTTP_200_OK)
        
    except Persona.DoesNotExist:
        return Response({'error': 'Persona no encontrada'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def todas_tareas(request):
    """
    API personalizada que devuelve todas las tareas asignadas del sistema
    """
    tareas_asignadas = TareaAsignada.objects.all().select_related('persona', 'tarea', 'tarea__tipo_tarea')
    
    data = []
    for asignacion in tareas_asignadas:
        data.append({
            'id': asignacion.id,
            'tarea': {
                'id': asignacion.tarea.id,
                'titulo': asignacion.tarea.titulo,
                'descripcion': asignacion.tarea.descripcion,
                'tipo_tarea': asignacion.tarea.tipo_tarea.nombre,
                'fecha_inicio': asignacion.tarea.fecha_inicio,
                'fecha_fin': asignacion.tarea.fecha_fin,
                'completada': asignacion.tarea.completada
            },
            'persona': {
                'id': asignacion.persona.id,
                'nombre': asignacion.persona.nombre,
                'apellido': asignacion.persona.apellido,
                'email': asignacion.persona.email
            },
            'fecha_asignacion': asignacion.fecha_asignacion,
            'completada': asignacion.completada
        })
    
    return Response({
        'tareas_asignadas': data,
        'total_tareas': len(data),
        'tareas_completadas': len([t for t in data if t['completada']]),
        'tareas_pendientes': len([t for t in data if not t['completada']])
    }, status=status.HTTP_200_OK)
