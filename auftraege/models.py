from django.db import models
from kunden.models import Kunde  # Kunde-Modell aus der anderen App importieren

class Leistung(models.Model):
    beschreibung = models.CharField(max_length=255)
    interne_nummer = models.CharField(max_length=50, unique=True)
    preis_pro_einheit = models.DecimalField(max_digits=10, decimal_places=2)
    notiz = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.beschreibung} ({self.preis_pro_einheit} €)"

class Auftrag(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    kurzbeschreibung = models.CharField(max_length=50, blank=True, null=False)    
    ausfuehrungsdatum = models.DateField(blank=True, null=False)
    rechnungsnummer = models.CharField(max_length=50, unique=True, blank=True, null=False)
    angebotsnummer = models.CharField(max_length=50, unique=True, blank=True, null=False)
    notiz = models.TextField(blank=True, null=False)    
    leistungen = models.ManyToManyField(Leistung, through='AuftragLeistung', blank=True, null=False)
    summe = models.FloatField(null=False, blank=True, default=0.0)

    # auto generator for fields
    def save(self, *args, **kwargs):
        if self.summe is None:
            self.summe = 0.0
        if not self.kurzbeschreibung:  # Nur setzen, wenn das Feld leer ist
            anzahl_auftraege = Auftrag.objects.filter(kunde=self.kunde).count()
            self.kurzbeschreibung = f"{str(self.kunde)} {anzahl_auftraege + 1}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Auftrag {self.id} für {self.kunde.vorname} {self.kunde.nachname}"

class AuftragLeistung(models.Model):
    auftrag = models.ForeignKey(Auftrag, on_delete=models.CASCADE)
    leistung = models.ForeignKey(Leistung, on_delete=models.CASCADE)
    anzahl = models.PositiveIntegerField()
    summe = models.FloatField(null=False, blank=True, default=0.0)

    def save(self, *args, **kwargs):
        if self.summe is None:
            self.summe = 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.anzahl}x {self.leistung.beschreibung} für Auftrag {self.auftrag.id}"
