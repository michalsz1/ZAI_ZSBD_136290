from rest_framework import routers
from django.urls import include, path
from .views import ProduktViewSet, OpiniaViewSet

router = routers.DefaultRouter()
router.register(r'get_produkty', ProduktViewSet)
router.register(r'get_opinia', OpiniaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]