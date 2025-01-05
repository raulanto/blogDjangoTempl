from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from blog.forms import LoginForm
from blog.views import CustomLoginView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls')),
                  path('login/',
                       CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login/index.html',
                                               authentication_form=LoginForm), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),  # Incluye las rutas de CKEditor
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
