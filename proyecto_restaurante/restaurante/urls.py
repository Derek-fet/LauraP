from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MesaViewSet, PlatoViewSet, PedidoViewSet, ReservaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register('mesas', MesaViewSet)
router.register('platos', PlatoViewSet)
router.register('pedidos', PedidoViewSet)
router.register('reservas', ReservaViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
