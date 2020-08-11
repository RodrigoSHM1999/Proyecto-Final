from django.urls import path, include
from django.conf.urls  import url
from .  import views
from .views import *
urlpatterns = [
    #url(r'^$', home, name = "index2"),
    
    url(r'^crear_product/',CreateProducto.as_view(), name = "crear_product"),
    url(r'^listar_product/',ListProducto.as_view(), name = "listar_product"),
    url(r'^editar_product/(?P<pk>\d+)/$',UpdateProducto.as_view(), name = "editar_product"),
    url(r'^eliminar_product/(?P<pk>\d+)/$',DeleteProducto.as_view(), name = "eliminar_product"),
    path('', views.index, name='index'),
    ]