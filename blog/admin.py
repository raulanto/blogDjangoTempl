from django.contrib import admin
from .models import Carta, Poema, Profile,LineaTiempo
# Register your models here.
@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    pass

@admin.register(Poema)
class PoemaAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(LineaTiempo)
class LineaTiempoAdmin(admin.ModelAdmin):
    pass