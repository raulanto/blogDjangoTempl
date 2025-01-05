from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView
from django.contrib import messages
from ..models import Profile, Poema, Carta

from django.shortcuts import render, redirect
from ..forms import UpdateUserForm,UpdateProfileForm
class PerfilView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        # Filtrar poemas y cartas por el usuario autenticado
        total_poemas = Poema.objects.filter(autor=request.user).count()
        total_cartas = Carta.objects.filter(autor=request.user).count()
        perfil=Profile.objects.get(user=request.user)
        # Obtener todos los poemas y cartas
        poemas = Poema.objects.all()
        cartas = Carta.objects.all()

        # Contexto para enviar a la plantilla
        context = {
            'titulo': 'Inicio',
            'texto': 'Este es el texto de la página de inicio',
            'total_poemas': total_poemas,
            'total_cartas': total_cartas,
            'poemas': poemas,
            'cartas': cartas,
            'perfil':perfil
        }

        return render(request, 'perfil/perfil.html', context)


@login_required
def profileEdit(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil Actulizado Correctamente')
            return redirect(to='blog:perfil')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'perfil/editar.html', {'user_form': user_form, 'profile_form': profile_form})
