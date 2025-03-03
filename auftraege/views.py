from django.shortcuts import render, get_object_or_404, redirect
from .models import Auftrag, AuftragLeistung, Leistung
from .forms import AuftragForm, AuftragLeistungForm, LeistungForm, AuftragLeistungFormSet
from kunden.models import Kunde
from .filters import AuftragFilter


def auftrag_liste(request):
    auftraege = Auftrag.objects.all()
    auftrag_filter = AuftragFilter(request.GET, queryset=auftraege)

    return render(request, 'auftraege/auftrag_liste.html', {
        'filter': auftrag_filter
    })

def auftrag_erstellen(request):
    if request.method == "POST":
        auftrag_form = AuftragForm(request.POST)
        #leistung_form = AuftragLeistungForm(request.POST)
        leistung_formset = AuftragLeistungFormSet(request.POST)

        if auftrag_form.is_valid() and leistung_formset.is_valid():
            auftrag = auftrag_form.save()  # Auftrag speichern
            # Leistung-Formset noch nicht in die Datenbank speichern
            auftrag_leistungen = leistung_formset.save(commit=False)
            
            tmp_new_sum = 0
            for leistung in auftrag_leistungen:

                leistung.summe = leistung.anzahl * leistung.leistung.preis_pro_einheit
                tmp_new_sum += leistung.summe 
                leistung.auftrag = auftrag  # Auftrag-Referenz setzen
                leistung.save()  # Jede Leistung einzeln speichern

            auftrag.summe = tmp_new_sum
            auftrag = auftrag_form.save()  # Auftrag speichern

            return redirect('auftrag_liste')  # Zur Liste der Aufträge umleiten
    else:
        #form = AuftragForm()
        auftrag_form = AuftragForm()
        leistung_formset = AuftragLeistungFormSet()

    return render(request, 'auftraege/auftrag_form.html',  {#'form': form})
        'auftrag_form': auftrag_form,
        'leistung_formset': leistung_formset
    })

def auftrag_bearbeiten(request, pk):
    auftrag = get_object_or_404(Auftrag, pk = pk)

    if request.method == 'POST':

        auftrag_form = AuftragForm(request.POST, instance=auftrag)
        leistung_formset = AuftragLeistungFormSet(request.POST, instance=auftrag)

        if auftrag_form.is_valid() and leistung_formset.is_valid():
            auftrag = auftrag_form.save()
            
            leistungen  = leistung_formset.save(commit=False)

            for leistung in leistung_formset.deleted_objects:
                leistung.delete()

            for leistung in leistungen:
                leistung.summe = leistung.anzahl * leistung.leistung.preis_pro_einheit
                leistung.auftrag = auftrag
                leistung.save()

            #auftrag.summe = sum(al.anzahl * al.leistung.preis_pro_einheit for al in auftrag.auftragleistung_set.all())
            auftrag.summe = sum(al.summe for al in auftrag.auftragleistung_set.all())
            auftrag.save()

            return redirect('auftrag_liste')
    else:
        auftrag_form = AuftragForm(instance=auftrag)
        leistung_formset = AuftragLeistungFormSet(instance=auftrag)

    return render(request, 'auftraege/auftrag_form.html', {
        'auftrag_form': auftrag_form,
        'leistung_formset': leistung_formset
        #'bearbeiten': True  # Diese Variable kann in der Vorlage verwendet werden
    })
    #return render(request, 'auftraege/auftrag_form.html', {'auftrag_form': auftrag_form})


def leistung_liste(request):
    leistungen = Leistung.objects.all()
    return render(request, 'auftraege/leistung_liste.html', {'leistungen': leistungen})

def leistung_erstellen(request):
    if request.method == "POST":
        form = LeistungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leistung_neu')  # Bleibt auf der Seite nach dem Speichern
    else:
        form = LeistungForm()

    return render(request, 'auftraege/leistung_form.html', {'form': form})

def leistung_bearbeiten(request, pk):
    leistung = get_object_or_404(Leistung, pk = pk)
    if request.method == 'POST':
        form = LeistungForm(request.Post, instance=leistung)
        if form.is_valid():
            form.save()
            return redirect('leistung_liste')
    else:
        form = LeistungForm(instance=leistung)
    return render(request, 'auftraege/leistung_form.html', {'form': form})