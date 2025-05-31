from django.urls import path
from .views import (
    UsuarioListCreateView,
    UsuarioRetrieveUpdateDestroyView,
    CultivoListCreateView,
    CultivoRetrieveUpdateDestroyView,
    ZonaRiegoListCreateView,
    ZonaRiegoRetrieveUpdateDestroyView,
    SensorHumedadListCreateView,
    SensorHumedadRetrieveUpdateDestroyView,
    LecturaHumedadListCreateView,
    LecturaHumedadRetrieveUpdateDestroyView,
    RiegoListCreateView,
    RiegoRetrieveUpdateDestroyView,
    PronosticoClimaListCreateView,
    PronosticoClimaRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('cultivos/', CultivoListCreateView.as_view(), name='cultivo-list-create'),
    path('cultivos/<int:pk>/', CultivoRetrieveUpdateDestroyView.as_view(), name='cultivo-detail'),
    path('zonas-riego/', ZonaRiegoListCreateView.as_view(), name='zona-riego-list-create'),
    path('zonas-riego/<int:pk>/', ZonaRiegoRetrieveUpdateDestroyView.as_view(), name='zona-riego-detail'),
    path('sensores-humedad/', SensorHumedadListCreateView.as_view(), name='sensor-humedad-list-create'),
    path('sensores-humedad/<int:pk>/', SensorHumedadRetrieveUpdateDestroyView.as_view(), name='sensor-humedad-detail'),
    path('lecturas-humedad/', LecturaHumedadListCreateView.as_view(), name='lectura-humedad-list-create'),
    path('lecturas-humedad/<int:pk>/', LecturaHumedadRetrieveUpdateDestroyView.as_view(), name='lectura-humedad-detail'),
    path('riegos/', RiegoListCreateView.as_view(), name='riego-list-create'),
    path('riegos/<int:pk>/', RiegoRetrieveUpdateDestroyView.as_view(), name='riego-detail'),
    path('pronosticos-clima/', PronosticoClimaListCreateView.as_view(), name='pronostico-clima-list-create'),
    path('pronosticos-clima/<int:pk>/', PronosticoClimaRetrieveUpdateDestroyView.as_view(), name='pronostico-clima-detail'),
]
