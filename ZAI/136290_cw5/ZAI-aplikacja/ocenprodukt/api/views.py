from .models import Produkt, Opinia
from .serializers import ProduktSerializer, OpiniaSerializer
from rest_framework import generics, permissions

class ProduktList(generics.ListAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-list"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych


class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-detail"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych


class OpiniaList(generics.ListAPIView):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-list"
    permission_classes = [permissions.IsAdminUser]  # tylko dla admina

class OpiniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-detail"
    permission_classes = [permissions.IsAdminUser]  # tylko dla admina

