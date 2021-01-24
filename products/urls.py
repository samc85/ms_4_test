from django.urls import path
from . import views
from django.conf import settings
# Import static if not imported
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.products, name='products'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
