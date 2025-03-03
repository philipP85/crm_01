import django_filters
from .models import Kunde

class KundeFilter(django_filters.FilterSet):
    vorname = django_filters.CharFilter(lookup_expr='icontains')
    nachname = django_filters.CharFilter(lookup_expr='icontains')
    #plz = django_filters.CharFilter(lookup_expr='exact')
    auftraege = django_filters.BooleanFilter()
    workshops = django_filters.BooleanFilter()

    class Meta:
        model = Kunde
        fields = ['vorname', 'nachname', 'auftraege', 'workshops']