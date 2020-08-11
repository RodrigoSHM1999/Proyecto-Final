
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import GeneratePDF
urlpatterns = [
    path('', include('market.urls')),
    path('admin/', admin.site.urls),
    url(r'^pdf/$', GeneratePDF.as_view()),
    path('accounts/', include('accounts.urls')),
    url(r'^market/', include('market.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)