from rest_framework import serializers
from .models import Workshop

class WorkshopSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(source='name')
    start = serializers.SerializerMethodField()  # Startzeit
    end = serializers.SerializerMethodField()  # Endzeit
    color = serializers.SerializerMethodField()  # Farbe für Events
    url = serializers.SerializerMethodField()
    class Meta:
        model = Workshop
        #fields = ['id', 'title', 'start', 'end']  # FullCalendar erwartet genau diese Felder
        fields = ['id','title', 'start', 'end', 'color', 'url']  # FullCalendar erwartet genau diese Felder

    def get_start(self, obj):
        return f"{obj.datum}T{obj.startzeit}"

    def get_end(self, obj):
        return f"{obj.datum}T{obj.endzeit}"

    def get_color(self, obj):
        #return "#337AFF"
        return "#00FF00"
    
    def get_url(self, obj):
        return f"/workshops/workshop/{obj.id}/bearbeiten/"