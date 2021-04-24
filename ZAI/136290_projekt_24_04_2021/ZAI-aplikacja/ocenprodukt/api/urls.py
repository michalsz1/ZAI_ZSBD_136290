from django.urls import path, include
from .views import ProduktList, ProduktDetail, OpiniaList, OpiniaDetail, SklepList, SklepDetail, ApiRoot
urlpatterns = [
    path('produkty', ProduktList.as_view(), name=ProduktList.view_name),
    path('produkty/<int:pk>', ProduktDetail.as_view(), name=ProduktDetail.view_name),
    path('opinie', OpiniaList.as_view(), name=OpiniaList.view_name),
    path('opinie/<int:pk>', OpiniaDetail.as_view(), name=OpiniaDetail.view_name),
    path('sklepy', SklepList.as_view(), name=SklepList.view_name),
    path('sklepy/<int:pk>', SklepDetail.as_view(), name=SklepDetail.view_name),
    path('api-auth', include('rest_framework.urls')),
    path('', ApiRoot.as_view(), name=ApiRoot.view_name),
]