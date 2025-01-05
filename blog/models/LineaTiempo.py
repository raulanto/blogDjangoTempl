from django.db import models
from django.contrib.auth.models import User
class LineaTiempo(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='linea', )
    contenido = models.TextField()
    fecha=models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación")