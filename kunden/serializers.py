from rest_framework import serializers
from .models import Kunde

class KundeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kunde
        fields = '__all__'