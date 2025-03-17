from django.db import models
from kunden.models import Kunde

class Material(models.Model):
    EINHEITEN = [
        ('Stk', 'Stück'),
        ('Pkg', 'Packung'),
        ('kg', 'Kilogramm'),
        ('m', 'Meter'),
        ('m²', 'Quadratmeter'),
        ('m³', 'Kubikmeter'),
        ('h', 'Stunde'),
        ('km', 'Kilometer'),
    ]
    beschreibung = models.CharField(max_length=255)
    preis_pro_einheit = models.DecimalField(max_digits=10, decimal_places=2)
    einheit = models.CharField(max_length=10, choices=EINHEITEN, default='Stk')
    notiz = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.beschreibung} ({self.preis_pro_einheit} €)"

class WorkshopMaterial(models.Model):
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    menge = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.menge}x {self.material.beschreibung} für Workshop am {self.workshop.datum}"
    

class WorkshopTeilnehmer(models.Model):
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE)
    teilnehmer = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    bezahlt = models.BooleanField(default=False)
    anmeldedatum = models.DateTimeField(auto_now_add=True, null=True)

class Workshop(models.Model):
    name = models.CharField(max_length=255)
    kurs_ziel = models.TextField()
    datum = models.DateField()
    startzeit = models.TimeField()
    endzeit = models.TimeField()
    teilnehmer = models.ManyToManyField(Kunde, through='WorkshopTeilnehmer', blank=True)
    material = models.ManyToManyField(Material, through='WorkshopMaterial', blank=True)
    fremdresourcen = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Workshop am {self.datum} von {self.startzeit} bis {self.endzeit}"


