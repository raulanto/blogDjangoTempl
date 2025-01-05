from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
class Poema(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poemas', help_text="Usuario que creó el poema")
    contenido = QuillField()
    creado_en = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación")
    actualizado_en = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última actualización")
    imagen = models.URLField(blank=True, null=True,default="https://i.pinimg.com/736x/65/74/65/657465bbe8aeaee85e0a4b73ca557731.jpg")

    class Meta:
        verbose_name = "Poema"
        verbose_name_plural = "Poemas"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"
