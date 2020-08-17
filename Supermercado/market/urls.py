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
    url(r'^crear_compra/',CreateCompra.as_view(), name = "crear_compra"),
    url(r'^listar_compra/',ListCompra.as_view(), name = "listar_compra"),
    url(r'^editar_compra/(?P<pk>\d+)/$',UpdateCompra.as_view(), name = "editar_compra"),
    url(r'^eliminar_compra/(?P<pk>\d+)/$',DeleteCompra.as_view(), name = "eliminar_compra"),
    url(r'^crear_client/',CreateCliente.as_view(), name = "crear_client"),
    url(r'^listar_client/',ListCliente.as_view(), name = "listar_client"),
    url(r'^editar_client/(?P<pk>\d+)/$',UpdateCliente.as_view(), name = "editar_client"),
    url(r'^eliminar_client/(?P<pk>\d+)/$',DeleteCliente.as_view(), name = "eliminar_client"),
    #path('', views.client, name='client'),
    path("market/compra", views.compra, name='compra'),
    path("market/cliente", views.cliente, name='cliente'),
    path("market/producto", views.producto, name='producto'),
    path('', views.index, name='index'),
    ]