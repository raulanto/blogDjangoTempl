from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField


class Carta(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas')
    titulo = models.CharField(max_length=255,unique=True)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas_recibidas')
    imagen = models.URLField(blank=True, null=True,default='https://i.pinimg.com/736x/9d/de/85/9dde859d52011fbb9f157516b1c77925.jpg')
    contenido = QuillField()
    posdata = models.TextField(blank=True, null=True)
    iframe = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.titulo
