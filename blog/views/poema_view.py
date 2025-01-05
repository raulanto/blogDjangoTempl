from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from ..forms import PoemaForm
from ..models import Poema
from django.contrib import messages
from django.template.loader import render_to_string

class CrearPoemaView(LoginRequiredMixin, CreateView):
    model = Poema
    form_class = PoemaForm
    template_name = 'poema/form.html'
    success_url = reverse_lazy('blog:listar_poemas')
    extra_context = {'titulo': 'Crear poema'}


    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "El poema se ha creao correctamente.")
        return super().form_valid(form)


class ListaPoemasView(LoginRequiredMixin, ListView):
    model = Poema
    template_name = 'poema/listar.html'
    context_object_name = 'poemas'

    def get_queryset(self):
        return Poema.objects.filter(autor=self.request.user)


# class EliminarPoemaAjaxView(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         try:
#             poema = Poema.objects.get(pk=pk, autor=request.user)
#             poema.delete()
#             return JsonResponse({'success': True, 'message': 'Poema eliminada con éxito'})
#         except Poema.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'Poema no encontrada o no tienes permiso'}, status=404)


class EliminarPoemaAjaxView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        try:
            poema = Poema.objects.get(pk=pk, autor=request.user)
            poema.delete()

            # Renderizar las poemas restantes como HTML
            poemas = Poema.objects.filter(autor=request.user)
            rendered_html = render_to_string('poema/partials/_list.html', {'poemas': poemas}, request)

            return JsonResponse({'success': True, 'html': rendered_html})
        except Poema.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Poema no encontrada o no tienes permiso'}, status=404)

class EditarPoemaView(LoginRequiredMixin, UpdateView):
    model = Poema
    form_class = PoemaForm
    template_name = 'poema/form.html'
    context_object_name = 'poema'
    extra_context = {'titulo': 'Editar Poema'}

    def get_object(self, queryset=None):
        poema = super().get_object(queryset)
        if poema.autor != self.request.user:
            raise PermissionDenied("No tienes permiso para editar esta poema")
        return poema

    def form_valid(self, form):
        # Agregar mensaje de éxito
        messages.success(self.request, "El poema se ha editado correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:listar_poemas')


