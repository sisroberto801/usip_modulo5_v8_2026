from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def clean(self):
        if self.fecha_nacimiento and self.fecha_nacimiento > timezone.now().date():
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro")


class TipoTarea(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    prioridad = models.IntegerField(default=1)
    
    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.prioridad < 1 or self.prioridad > 10:
            raise ValidationError("La prioridad debe estar entre 1 y 10")


class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_tarea = models.ForeignKey(TipoTarea, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    def clean(self):
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin < self.fecha_inicio:
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio")


class TareaAsignada(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.tarea.titulo} - {self.persona.nombre}"
    
    class Meta:
        unique_together = ('tarea', 'persona')
