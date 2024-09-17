from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer
from rest_framework.response import Response

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductoSerializer(queryset, many=True)

        return Response({"productos": serializer.data})