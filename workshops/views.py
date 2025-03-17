from django.shortcuts import render, get_object_or_404, redirect
from .models import Material, Workshop, WorkshopMaterial
from .forms import MaterialForm, WorkshopForm, WorkshopMaterialFormSet, WorkshopTeilnehmerFormSet, WorkshopTeilnehmer

# Material-Liste
def material_liste(request):
    materialien = Material.objects.all()
    return render(request, 'material_liste.html', {'materialien': materialien})

# Material erstellen
def material_neu(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_liste')
    else:
        form = MaterialForm()
    return render(request, 'material_form.html', {'form': form})

# Material bearbeiten
def material_bearbeiten(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_liste')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material_form.html', {'form': form, 'material': material})

# Workshop-Liste
def workshop_liste(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshop_liste.html', {'workshops': workshops})

# Workshop erstellen
def workshop_neu(request):
    if request.method == "POST":
        form = WorkshopForm(request.POST)
        material_formset = WorkshopMaterialFormSet(request.POST)
        teilnehmer_formset = WorkshopTeilnehmerFormSet(request.POST)

        if form.is_valid() and material_formset.is_valid() and teilnehmer_formset.is_valid():
            workshop = form.save()
            materials = material_formset.save(commit=False)
            teilnehmer_p = teilnehmer_formset.save(commit=False)

            for teilnehmer in teilnehmer_p:
                teilnehmer.workshop = workshop
                teilnehmer.save()
            
            for material in materials:
                material.workshop = workshop
                material.save()
                
            return redirect('workshop_liste')
    else:
        
        form = WorkshopForm()
        material_formset = WorkshopMaterialFormSet()
        teilnehmer_formset = WorkshopTeilnehmerFormSet()
        


    return render(request, 'workshop_form.html', {'form': form, 'material_formset': material_formset, 'teilnehmer_formset': teilnehmer_formset})




# Workshop bearbeiten
def workshop_bearbeiten(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)

    if request.method == "POST":
        form = WorkshopForm(request.POST, instance=workshop)
        material_formset = WorkshopMaterialFormSet(request.POST, instance=workshop)
        teilnehmer_formset = WorkshopTeilnehmerFormSet(request.POST, instance=workshop)
        #teilnehmer_formset = WorkshopTeilnehmerFormSet(request.POST, queryset=WorkshopTeilnehmer.objects.filter(workshop=workshop))

        if form.is_valid() and material_formset.is_valid() and teilnehmer_formset.is_valid():
            workshop = form.save()
            
            # Teilnehmer speichern
            teilnehmer_p = teilnehmer_formset.save(commit=False)
            for teilnehmer in teilnehmer_p:
                teilnehmer.workshop = workshop
                teilnehmer.save()
            # Teilnehmer löschen
            for deleted_teilnehmer in teilnehmer_formset.deleted_objects:
                deleted_teilnehmer.delete()
            teilnehmer_formset.save_m2m()
            
            # Material speichern
            materials = material_formset.save(commit=False)
            for material in materials:
                material.workshop = workshop
                material.save()
            # Materail löschen
            for deleted_material in material_formset.deleted_objects:
                deleted_material.delete()
            material_formset.save_m2m()
                
            return redirect('workshop_liste')
    else:
        print('in else workshop bearbeiten')
        form = WorkshopForm(instance=workshop)
        material_formset = WorkshopMaterialFormSet(instance=workshop)
        #teilnehmer_formset = WorkshopTeilnehmerFormSet(queryset=WorkshopTeilnehmer.objects.filter(workshop=workshop))
        teilnehmer_formset = WorkshopTeilnehmerFormSet(instance=workshop)
        print('in end else workshop bearbeiten')

    return render(request, 'workshop_form.html', {
        'form': form,
        'material_formset': material_formset,
        'teilnehmer_formset': teilnehmer_formset,
        'workshop': workshop
    })


# # Workshop bearbeiten
# def workshop_bearbeiten(request, pk):
#     workshop = get_object_or_404(Workshop, pk=pk)

#     if request.method == "POST":
#         form = WorkshopForm(request.POST, instance=workshop)
#         material_formset = WorkshopMaterialFormSet(request.POST, instance=workshop)

#         if form.is_valid() and material_formset.is_valid():
#             form.save()
#             material_formset.save()
#             return redirect('workshop_liste')
#     else:
#         form = WorkshopForm(instance=workshop)
#         material_formset = WorkshopMaterialFormSet(instance=workshop)

#     return render(request, 'workshop_form.html', {'form': form, 'material_formset': material_formset, 'workshop': workshop})

