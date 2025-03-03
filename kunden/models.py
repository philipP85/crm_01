from django.db import models

class Kunde(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    ort = models.CharField(max_length=100, blank=True, null=True)
    strasse = models.CharField(max_length=100, blank=True, null=True)
    hausnummer = models.CharField(max_length=10, blank=True, null=True)
    plz = models.CharField(max_length=10, blank=True, null=True)
    auftraege = models.BooleanField(default=False)
    workshops = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vorname} {self.nachname}"