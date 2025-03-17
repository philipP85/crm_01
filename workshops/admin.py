from django.contrib import admin

from .models import Material, Workshop, WorkshopMaterial, WorkshopTeilnehmer

admin.site.register(Material)
admin.site.register(Workshop)
admin.site.register(WorkshopMaterial)
admin.site.register(WorkshopTeilnehmer)
