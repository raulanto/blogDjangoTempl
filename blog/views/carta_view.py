from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from ..forms import CartaForm
from ..models import Carta


class CrearCartaView(LoginRequiredMixin, CreateView):
    model = Carta
    form_class = CartaForm
    template_name = 'carta/form.html'
    success_url = reverse_lazy('blog:lista_cartas')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ListaCartasView(LoginRequiredMixin, ListView):
    model = Carta
    template_name = 'carta/listar.html'
    context_object_name = 'cartas'

    def get_queryset(self):
        return Carta.objects.filter(autor=self.request.user)


class VerCartaView(LoginRequiredMixin, DetailView):
    model = Carta
    template_name = 'carta/carta.html'
    context_object_name = 'carta'




# class EliminarCartaAjaxView(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         try:
#             carta = Carta.objects.get(pk=pk, autor=request.user)
#             carta.delete()
#             return JsonResponse({'success': True, 'message': 'Carta eliminada con éxito'})
#         except Carta.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'Carta no encontrada o no tienes permiso'}, status=404)
class EliminarCartaAjaxView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        try:
            carta = Carta.objects.get(pk=pk, autor=request.user)
            carta.delete()

            # Renderizar las cartas restantes como HTML
            cartas = Carta.objects.filter(autor=request.user)
            rendered_html = render_to_string('carta/partials/_list.html', {'cartas': cartas}, request)

            return JsonResponse({'success': True, 'html': rendered_html})
        except Carta.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Carta no encontrada o no tienes permiso'}, status=404)




class EditarCartaView(LoginRequiredMixin, UpdateView):
    model = Carta
    form_class = CartaForm
    template_name = 'carta/form.html'
    context_object_name = 'carta'

    def get_object(self, queryset=None):
        carta = super().get_object(queryset)
        if carta.autor != self.request.user:
            raise PermissionDenied("No tienes permiso para editar esta carta")
        return carta

    def get_success_url(self):
        return reverse_lazy('blog:ver_carta', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ObtenerCartaAjaxView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        carta = Carta.objects.filter(autor=request.user)
        return JsonResponse({'success': True, 'cartas': carta})
