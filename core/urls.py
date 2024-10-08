from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', include('cliente.urls')),
    path('conta/', include('cliente.urls')),
    path('operacoes/', include('operacoes.urls')),
    path('transacoes/', include('transacoes.urls')),
    path('credit_card/', include('cartaocredito.urls')),
] + debug_toolbar_urls()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
