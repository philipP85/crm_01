from django.urls import path
from . import views

urlpatterns = [
    # Material-URLs
    path('material/', views.material_liste, name='material_liste'),
    path('material/neu/', views.material_neu, name='material_neu'),
    path('material/<int:pk>/bearbeiten/', views.material_bearbeiten, name='material_bearbeiten'),

    # Workshop-URLs
    path('workshop/', views.workshop_liste, name='workshop_liste'),
    path('workshop/neu/', views.workshop_neu, name='workshop_neu'),
    path('workshop/<int:pk>/bearbeiten/', views.workshop_bearbeiten, name='workshop_bearbeiten'),
]
