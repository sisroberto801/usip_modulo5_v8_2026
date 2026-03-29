from rest_framework import serializers
from .models import Categoria, Producto, Persona, TipoTarea, Tarea, TareaAsignada


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class TipoTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTarea
        fields = '__all__'


class TareaSerializer(serializers.ModelSerializer):
    tipo_tarea_nombre = serializers.CharField(source='tipo_tarea.nombre', read_only=True)
    
    class Meta:
        model = Tarea
        fields = '__all__'


class TareaAsignadaSerializer(serializers.ModelSerializer):
    tarea_titulo = serializers.CharField(source='tarea.titulo', read_only=True)
    persona_nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = TareaAsignada
        fields = '__all__'
    
    def get_persona_nombre_completo(self, obj):
        return f"{obj.persona.nombre} {obj.persona.apellido}"
