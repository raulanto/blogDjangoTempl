from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from ..forms import LineaTiempoForm
from ..models import LineaTiempo


class CrearLineaTiempoView(LoginRequiredMixin, CreateView):
    model = LineaTiempo
    form_class = LineaTiempoForm
    template_name = 'lineaTiempo/form.html'
    success_url = reverse_lazy('blog:lista_linea_tiempo')



    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ListaLineaTiemposView(LoginRequiredMixin, ListView):
    model = LineaTiempo
    template_name = 'lineaTiempo/listar.html'
    context_object_name = 'lineatiempos'

    def get_queryset(self):
        return LineaTiempo.objects.filter(autor=self.request.user)




# class EliminarLineaTiempoAjaxView(LoginRequiredMixin, View):
#     def post(self, request, pk, *args, **kwargs):
#         try:
#             lineaTiempo = LineaTiempo.objects.get(pk=pk, autor=request.user)
#             lineaTiempo.delete()
#             return JsonResponse({'success': True, 'message': 'LineaTiempo eliminada con éxito'})
#         except LineaTiempo.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'LineaTiempo no encontrada o no tienes permiso'}, status=404)
class EliminarLineaTiempoAjaxView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        try:
            lineaTiempo = LineaTiempo.objects.get(pk=pk, autor=request.user)
            lineaTiempo.delete()

            # Renderizar las lineatiempos restantes como HTML
            lineatiempos = LineaTiempo.objects.filter(autor=request.user)
            rendered_html = render_to_string('lineaTiempo/partials/_list.html', {'lineatiempos': lineatiempos}, request)

            return JsonResponse({'success': True, 'html': rendered_html})
        except LineaTiempo.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'LineaTiempo no encontrada o no tienes permiso'}, status=404)


class EditarLineaTiempoView(LoginRequiredMixin, UpdateView):
    model = LineaTiempo
    form_class = LineaTiempoForm
    template_name = 'lineaTiempo/form.html'
    context_object_name = 'lineaTiempo'

    def get_object(self, queryset=None):
        lineaTiempo = super().get_object(queryset)
        if lineaTiempo.autor != self.request.user:
            raise PermissionDenied("No tienes permiso para editar esta lineaTiempo")
        return lineaTiempo

    def get_success_url(self):
        return reverse_lazy('blog:ver_carta', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



