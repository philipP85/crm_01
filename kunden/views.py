from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django_filters.views import FilterView
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Kunde
from .forms import KundeForm
from .filters import KundeFilter
from .serializers import KundeSerializer

from django.contrib.auth.decorators import login_required

# **1. Kundenübersicht mit Filter**
class KundenListeView(FilterView):
    model = Kunde
    template_name = 'kunden/kunden_liste.html'
    filterset_class = KundeFilter

#@login_required
def kunden_liste(request):
    kunden = Kunde.objects.all()
    filter_set = KundeFilter(request.GET, queryset=kunden)  # Filter auf Queryset anwenden

    return render(request, 'kunden/kunden_liste.html', {'filter': filter_set})

# **2. Kunde erstellen**
def kunde_erstellen(request):
    if request.method == 'POST':
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kunden_liste')
    else:
        form = KundeForm()
    return render(request, 'kunden/kunden_form.html', {'form': form})

# **3. Kunde bearbeiten**
def kunde_bearbeiten(request, pk):
    kunde = get_object_or_404(Kunde, pk=pk)
    if request.method == 'POST':
        form = KundeForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            return redirect('kunden_liste')
    else:
        form = KundeForm(instance=kunde)
    return render(request, 'kunden/kunden_form.html', {'form': form})

# **4. REST API ViewSet**
class KundeViewSet(viewsets.ModelViewSet):
    queryset = Kunde.objects.all()
    serializer_class = KundeSerializer
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['vorname', 'nachname', 'auftraege', 'workshops']
