from django import forms
from django.forms import inlineformset_factory
from .models import Auftrag, Leistung, AuftragLeistung
from datetime import datetime

class LeistungForm(forms.ModelForm):
    class Meta:
        model = Leistung
        fields = ['beschreibung', 'interne_nummer', 'preis_pro_einheit', 'notiz']
        widgets = {
            'notiz': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

class AuftragLeistungForm(forms.ModelForm):
    #leistung = forms.ModelChoiceField(queryset=Leistung.objects.all(), label="Leistung")
    #anzahl = forms.IntegerField(min_value=1, label="Anzahl")

    class Meta:
        model = AuftragLeistung
        fields = ['leistung', 'anzahl']

class AuftragForm(forms.ModelForm):
    ausfuehrungsdatum = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'width: 150px;'})
    )
    class Meta:
        model = Auftrag
        fields = ['kunde', 'kurzbeschreibung', 'ausfuehrungsdatum', 'rechnungsnummer', 'angebotsnummer', 'notiz']
        widgets = {
            'kurzbeschreibung': forms.Textarea(attrs={'rows': 1, 'cols': 40}),
            'notiz': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        aktuelles_jahr = datetime.now().year
        auftraege_dieses_jahr = Auftrag.objects.filter(ausfuehrungsdatum__year=aktuelles_jahr).count()

        if not self.instance.pk:  # Nur für neue Objekte
            #anzahl_auftraege = Auftrag.objects.filter(kunde=self.initial.get('kunde')).count()
            #anzahl_auftraege = Auftrag.objects.all().count()
            s_year = str(aktuelles_jahr)
            self.fields['rechnungsnummer'].initial = f"R{s_year[-2:]}-{auftraege_dieses_jahr+1:04.0f}"



# Formset für AuftragLeistung
AuftragLeistungFormSet = inlineformset_factory(
    Auftrag, AuftragLeistung,  # Parent und Child Model
    form=forms.ModelForm,
    fields=['leistung', 'anzahl'],
    extra=1,  # Wie viele leere Felder standardmäßig angezeigt werden
    can_delete=True  # Falls man eine Leistung entfernen möchte
)