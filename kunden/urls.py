from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KundenListeView, kunde_erstellen, kunde_bearbeiten, KundeViewSet

router = DefaultRouter()
#router.register(r'api/kunden', KundeViewSet)
router.register(r'kunden', KundeViewSet)

urlpatterns = [
    path('', KundenListeView.as_view(), name='kunden_liste'),
    path('neu/', kunde_erstellen, name='kunde_erstellen'),
    path('<int:pk>/bearbeiten/', kunde_bearbeiten, name='kunde_bearbeiten'),
    path('', include(router.urls)),  # API-URLs automatisch registrieren
]