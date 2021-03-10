from django.urls import path

from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [

    path('', views.blog, name="blog"),
    path('verblog/<int:post_id>/', views.verblog, name='verblog'),
    path('paginablog/<int:pagina>/', views.paginablog, name='paginablog'),
    path('buscar_blog/', views.buscar_blog, name='buscar_blog'),
]
