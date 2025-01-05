from django.urls import path

from blog.views import index, BlogView, CrearCartaView, ListaCartasView, VerCartaView, EliminarCartaAjaxView, \
    EditarCartaView, PerfilView, profileEdit, ListaPoemasView, CrearPoemaView, EliminarPoemaAjaxView, EditarPoemaView, \
    ObtenerCartaAjaxView, ListaLineaTiemposView, CrearLineaTiempoView

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('panel', BlogView.as_view(), name='panel'),
    path('carta/crear-carta/', CrearCartaView.as_view(), name='crear_carta'),
    path('cartas/', ListaCartasView.as_view(), name='lista_cartas'),
    path('cartas/<int:pk>/', VerCartaView.as_view(), name='ver_carta'),
    path('cartas/eliminar-ajax/<int:pk>/', EliminarCartaAjaxView.as_view(), name='eliminar_carta_ajax'),
    path('carta/editar-carta/<int:pk>/', EditarCartaView.as_view(), name='editar_carta'),
    path('obtener/', ObtenerCartaAjaxView.as_view(), name='obtener_cartas_ajax'),
    path('poema/editar-poema/<int:pk>/', EditarPoemaView.as_view(), name='editar_poema'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('profile/', profileEdit, name='editar_perfil'),
    path('poemas/', ListaPoemasView.as_view(), name='listar_poemas'),
    path('poemas/crear-poema/', CrearPoemaView.as_view(), name='crear_poema'),
    path('poema/eliminar-ajax/<int:pk>/', EliminarPoemaAjaxView.as_view(), name='eliminar_poema_ajax'),
    path('linea-tiempo/', ListaLineaTiemposView.as_view(), name='lista_linea_tiempo'),
    path('linea-tiempo/crear-linea/', CrearLineaTiempoView.as_view(), name='crear_linea_tiempo'),

]
