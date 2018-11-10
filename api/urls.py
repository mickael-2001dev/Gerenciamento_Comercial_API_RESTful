from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import MarcaViewSet, CarroViewSet
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'carros', CarroViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('carros', TemplateView.as_view(template_name='index.html')),
]
