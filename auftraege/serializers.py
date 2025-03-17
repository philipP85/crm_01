from rest_framework import serializers
from .models import Auftrag
from datetime import datetime
import pytz  # Zeitzonen-Unterstützung

class AuftragSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()  # Berechnetes Feld für FullCalendar
    #start = serializers.DateTimeField(source='ausfuehrungsdatum')
    title = serializers.CharField(source='kurzbeschreibung')  
    color = serializers.SerializerMethodField()  # Farbe für Events  
    url = serializers.SerializerMethodField()
    class Meta:
        model = Auftrag
        #fields = ['id', 'title', 'start', 'end']  # FullCalendar erwartet genau diese Felder
        fields = ['id', 'title', 'start', 'color','url']  # FullCalendar erwartet genau diese Felder

    def get_start(self, obj):
        """ Fügt einfach '00:00:00' an das Datum an """
        return f"{obj.ausfuehrungsdatum}T00:00:00"
    
    def get_color(self, obj):
        return "#fc037f"
    
    def get_url(self, obj):
        return f"/auftraege/auftrag/{obj.id}/bearbeiten/"