from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restaurante.urls')),  # SOLO AQUÍ SE PONE /api/
]
