# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import KundenListeView, kunde_erstellen, kunde_bearbeiten, KundeViewSet

# router = DefaultRouter()
# #router.register(r'api/kunden', KundeViewSet)
# router.register(r'kunden', KundeViewSet)

# urlpatterns = [
#     path('', KundenListeView.as_view(), name='kunden_liste'),
#     path('neu/', kunde_erstellen, name='kunde_erstellen'),
#     path('<int:pk>/bearbeiten/', kunde_bearbeiten, name='kunde_bearbeiten'),
#     path('', include(router.urls)),  # API-URLs automatisch registrieren
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import kalender_events, kalender_test_view, AuftragKalenderSet, KalenderEventViewSet

router = DefaultRouter()
#router.register(r'events', AuftragKalenderSet)
router.register(r'events', KalenderEventViewSet, basename='kalender-event')

urlpatterns = [
    #path('kalender-test/', kalender_test_view, name='kalender-test'),
    path('', kalender_test_view, name='kalender_test'),
    #path('api/events/', kalender_events, name='kalender-events'),
    path('api/', include(router.urls)),  # API-URLs automatisch registrieren
]