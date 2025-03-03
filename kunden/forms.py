from django import forms
from .models import Kunde

class KundeForm(forms.ModelForm):
    class Meta:
        model = Kunde
        fields = '__all__'