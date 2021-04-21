from .models import Produkt, Opinia, Sklep
from .serializers import ProduktSerializer, OpiniaSerializer, SklepSerializer
from rest_framework import generics, permissions
from rest_framework import viewsets

class ProduktList(generics.ListCreateAPIView): # ListAPIView
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-list"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych


class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-detail"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych


class OpiniaList(generics.ListCreateAPIView): # ListAPIView
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-list"
    permission_classes = [permissions.IsAdminUser]  # tylko dla admina

class OpiniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-detail"
    permission_classes = [permissions.IsAdminUser]  # tylko dla admina

class SklepList(generics.ListCreateAPIView): # ListAPIView
    queryset = Sklep.objects.all()
    serializer_class = SklepSerializer
    view_name="sklep-list"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych

class SklepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sklep.objects.all()
    serializer_class = SklepSerializer
    view_name="sklep-detail"
    permission_classes = [permissions.IsAdminUser]  # tylko dla zarejestrowanych