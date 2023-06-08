from django.urls import path
from . import views
from .views import ValidatedResultList

urlpatterns = [
    path('port_scan/', views.port_scan, name='port_scan'),
    path('api/results/', ValidatedResultList.as_view(),
         name='validated_result_list'),
]
