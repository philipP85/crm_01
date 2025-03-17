from django import forms
from django.forms import inlineformset_factory
from .models import Workshop, WorkshopMaterial, Material, WorkshopTeilnehmer
from kunden.models import Kunde



class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['name', 'kurs_ziel', 'datum', 'startzeit', 'endzeit', 'fremdresourcen']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'width: 150px;'}),
            'startzeit': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'width: 150px;'}),
            'endzeit': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'width: 150px;'}),
            'fremdresourcen': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'kurs_ziel': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['beschreibung', 'preis_pro_einheit', 'einheit', 'notiz']
        widgets = {
            'beschreibung': forms.TextInput(attrs={'class': 'form-control'}),
            'preis_pro_einheit': forms.NumberInput(attrs={'class': 'form-control'}),
            'einheit': forms.Select(attrs={'class': 'form-control'}),
            'notiz': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class WorkshopMaterialForm(forms.ModelForm):
    class Meta:
        model = WorkshopMaterial
        fields = ['material', 'menge']
        widgets = {
            'material': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'menge': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'style': 'width: 100px;'}),
        }

WorkshopMaterialFormSet = forms.inlineformset_factory(
    Workshop, WorkshopMaterial, form=WorkshopMaterialForm, extra=1, can_delete=True
)

# WorkshopTeilnehmerFormSet = forms.inlineformset_factory(
#     Workshop, Kunde, form=WorkshopMaterialForm, extra=1, can_delete=True
# )

# class WorkshopTeilnehmerForm(forms.ModelForm):
#     teilnehmer = forms.ModelMultipleChoiceField(
#         queryset=Workshop.teilnehmer.field.related_model.objects.all(),
#         widget=forms.SelectMultiple(attrs={'class': 'form-control'})
#     )

#     class Meta:
#         model = Workshop
#         fields = ['teilnehmer']

class WorkshopTeilnehmerForm(forms.ModelForm):
    class Meta:
        model = WorkshopTeilnehmer
        fields = ['teilnehmer','bezahlt']

# **Jetzt als Inline-Formset**
WorkshopTeilnehmerFormSet = inlineformset_factory(
    Workshop, WorkshopTeilnehmer, form=WorkshopTeilnehmerForm, extra=1, can_delete=True
)