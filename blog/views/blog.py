from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from ..models import Poema, Carta

@method_decorator(login_required, name='dispatch')
class BlogView(View):
    def get(self, request):
        # Filtrar poemas y cartas por el usuario autenticado
        total_poemas = Poema.objects.filter(autor=request.user).count()
        total_cartas = Carta.objects.filter(autor=request.user).count()

        # Obtener todos los poemas y cartas
        poemas = Poema.objects.select_related('autor', 'autor__profile').all()


        # Contexto para enviar a la plantilla
        context = {
            'titulo': 'Inicio',
            'texto': 'Este es el texto de la página de inicio',
            'total_poemas': total_poemas,
            'total_cartas': total_cartas,
            'poemas': poemas,
        }

        return render(request, 'blog/index.html', context)
