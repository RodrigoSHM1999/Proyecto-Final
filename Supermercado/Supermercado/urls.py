
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import GeneratePDF
urlpatterns = [
    path('', include('market.urls')),
    path('admin/', admin.site.urls),
    url(r'^pdf/$', GeneratePDF.as_view()),
]
