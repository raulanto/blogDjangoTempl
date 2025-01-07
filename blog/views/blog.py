from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from ..models import Poema, Carta, LineaTiempo


@method_decorator(login_required, name='dispatch')
class BlogView(View):
    def get(self, request):
        # Filtrar poemas y cartas por el usuario autenticado
        total_poemas = Poema.objects.filter(autor=request.user).count()
        total_cartas = Carta.objects.filter(autor=request.user).count()
        total_diaz = LineaTiempo.objects.filter(autor=request.user).count()

        # Obtener todos los poemas y cartas
        poemas = Poema.objects.select_related('autor', 'autor__profile').all()

        # Contexto para enviar a la plantilla
        context = {
            'titulo': 'Inicio',
            'texto': 'Este es el texto de la página de inicio',
            'total_poemas': total_poemas,
            'total_cartas': total_cartas,
            'total_dias': total_diaz,
            'poemas': poemas,
        }

        return render(request, 'blog/index.html', context)


@method_decorator(login_required, name='dispatch')
class BuzonView(View):
    def get(self, request):
        total_cartas = Carta.objects.filter(destinatario=request.user).count()
        cartas = Carta.objects.select_related('autor', 'autor__profile').filter(destinatario=request.user)

        context = {
            'total_cartas': total_cartas,
            'cartas': cartas,
        }

        return render(request, 'blog/buzon.html', context)
