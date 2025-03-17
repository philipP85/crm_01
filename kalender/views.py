from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from itertools import chain

from auftraege.models import Auftrag
from auftraege.serializers import AuftragSerializer
from workshops.models import Workshop
from workshops.serailizers import WorkshopSerializer
from rest_framework import viewsets, filters

@api_view(['GET'])
def kalender_events(request):
    auftraege = Auftrag.objects.all()  # Holt alle Aufträge
    serializer = AuftragSerializer(auftraege, many=True)  # Konvertiert sie in JSON
    return Response(serializer.data)

def kalender_test_view(request):
    return render(request, 'kalender/kalender_test.html')


#class AuftragKalenderSet(viewsets.ModelViewSet):
class AuftragKalenderSet(viewsets.ReadOnlyModelViewSet):
    queryset = Auftrag.objects.all()
    serializer_class = AuftragSerializer

class KalenderEventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API-Endpoint für Kalender-Events (Aufträge + Workshops)
    """

    serializer_class = None  # Serializer dynamisch festlegen

    def get_queryset(self):
        auftraege = Auftrag.objects.all()
        workshops = Workshop.objects.all()

        # Kombiniere die Querysets
        return list(chain(auftraege, workshops))

    # def get_serializer_class(self):
    #     """
    #     Wählt je nach Event-Typ den passenden Serializer.
    #     """

    #     if self.request.query_params.get("type") == "workshop":
    #         return WorkshopSerializer
    #     elif self.request.query_params.get("type") == "auftrag":
    #         return AuftragSerializer
    #     return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        """
        Überschreibt die `list`-Methode, um beide Event-Typen mit passenden Serializern zu verarbeiten.
        """
        auftraege = Auftrag.objects.all()
        workshops = Workshop.objects.all()

        auftrag_serializer = AuftragSerializer(auftraege, many=True)
        workshop_serializer = WorkshopSerializer(workshops, many=True)

        return Response(auftrag_serializer.data + workshop_serializer.data)