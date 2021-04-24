from .models import Produkt, Opinia, Sklep
from .serializers import ProduktSerializer, OpiniaSerializer, SklepSerializer
from rest_framework import generics, permissions
from rest_framework import viewsets
from .custompermission import IsCurrentUserOwnerOrReadOnly
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class ProduktList(generics.ListCreateAPIView): # ListAPIView
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-list"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych
    filterset_fields = ['nazwa']
    search_fields = ['nazwa']
    ordering_fields = ['nazwa']

class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    view_name="produkt-detail"
    permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych

class OpiniaFilter(FilterSet):
    from_data_dodania = DateTimeFilter(field_name='data_dodania', lookup_expr='gte')
    to_data_dodania = DateTimeFilter(field_name='data_dodania', lookup_expr='lte')

    class Meta:
        model = Opinia
        fields = ['from_data_dodania','to_data_dodania']

class OpiniaList(generics.ListCreateAPIView): # ListAPIView
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-list"
    #permission_classes = [permissions.IsAdminUser]  # tylko dla admina
    filter_class = OpiniaFilter
    ordering_fields = ['autor', 'data_dodania']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class OpiniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opinia.objects.all()
    serializer_class = OpiniaSerializer
    view_name="opinia-detail"
    #permission_classes = [permissions.IsAdminUser]  # tylko dla admina
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)


class SklepList(generics.ListCreateAPIView): # ListAPIView
    queryset = Sklep.objects.all()
    serializer_class = SklepSerializer
    view_name="sklep-list"
    #permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych
    filterset_fields = ['nazwa_sklepu']
    search_fields = ['nazwa_sklepu']
    ordering_fields = ['nazwa_sklepu']

class SklepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sklep.objects.all()
    serializer_class = SklepSerializer
    view_name="sklep-detail"
    #permission_classes = [permissions.IsAuthenticated] # tylko dla zarejestrowanych



class ApiRoot(generics.GenericAPIView):
    view_name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'produkt-list': reverse(ProduktList.view_name, request=request),
                         'opinia-list': reverse(OpiniaList.view_name, request=request),
                         'sklep-list': reverse(SklepList.view_name, request=request)
                         })