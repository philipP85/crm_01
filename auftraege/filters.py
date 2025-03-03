import django_filters
from .models import Auftrag

class AuftragFilter(django_filters.FilterSet):
    kunde = django_filters.CharFilter(field_name='kunde__nachname', lookup_expr='icontains', label="Kunde")
    datum = django_filters.DateFilter(field_name='ausfuehrungsdatum', lookup_expr='exact', label="Datum")

    class Meta:
        model = Auftrag
        fields = ['kunde', 'datum']
