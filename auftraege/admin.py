from django.contrib import admin

from .models import Auftrag, AuftragLeistung, Leistung

admin.site.register(Auftrag)
admin.site.register(AuftragLeistung)
admin.site.register(Leistung)
