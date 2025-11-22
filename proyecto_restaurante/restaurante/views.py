from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

from .models import Mesa, Plato, Pedido, Reserva, Usuario
from .serializers import (
    MesaSerializer, PlatoSerializer, PedidoSerializer,
    ReservaSerializer, UsuarioSerializer
)

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

    @action(detail=False, methods=["get"])
    def disponibles(self, request):
        disponibles = Mesa.objects.filter(estado="Disponible")
        serializer = self.get_serializer(disponibles, many=True)
        return Response(serializer.data)

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    # 🧹 Limpia reservas vencidas (opcional pero recomendado)
    def list(self, request, *args, **kwargs):
        now = timezone.now()

        vencidas = Reserva.objects.filter(
            estado="activa",
            fecha__lt=now.date()
        )
        for r in vencidas:
            r.estado = "vencida"
            r.save()

        return super().list(request, *args, **kwargs)

    # ✔ Validación ya está en el serializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 🔥 NUEVO: Cancelar reserva
    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        reserva = self.get_object()
        
        if reserva.estado != "activa":
            return Response({"error": "Esta reserva no está activa."},
                            status=status.HTTP_400_BAD_REQUEST)

        reserva.estado = "cancelada"
        reserva.save()

        return Response(
            {"mensaje": "Reserva cancelada correctamente."},
            status=status.HTTP_200_OK
        )


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
