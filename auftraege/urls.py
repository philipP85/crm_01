from django.urls import path
from .views import auftrag_erstellen, leistung_erstellen, auftrag_liste, leistung_liste, leistung_bearbeiten, auftrag_bearbeiten

urlpatterns = [
    path('', auftrag_liste, name='auftrag_liste'),
    path('neu/', auftrag_erstellen, name='auftrag_neu'),
    path('leistung/neu/', leistung_erstellen, name='leistung_neu'),
    path('leistungen/', leistung_liste, name='leistung_liste'),
    #path('<int:pk>/bearbeiten/', auftrag_bearbeiten, name='auftrag_bearbeiten'),
    path('auftrag/<int:pk>/bearbeiten/', auftrag_bearbeiten, name='auftrag_bearbeiten'),
    path('leistungen/<int:pk>/bearbeiten/', leistung_bearbeiten, name='leistung_bearbeiten'),
]
