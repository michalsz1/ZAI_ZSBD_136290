from .models import Produkt, Opinia
from rest_framework import viewsets
from .serializers import ProduktSerializer, OpiniaSerializer

class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer

class OpiniaViewSet(viewsets.ModelViewSet):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer


