from .models import Produkt, Opinia
from .serializers import ProduktSerializer, OpiniaSerializer
from rest_framework import generics

class ProduktList(generics.ListAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-list"

class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-detail"

class OpiniaList(generics.ListAPIView):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-list"

class OpiniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-detail"

