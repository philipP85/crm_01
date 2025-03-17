# 📝 Auftrags- & Kundenverwaltung

Ein Django-Projekt zur Verwaltung von Kunden, Aufträgen und Leistungen.

## 🚀 Features

- Kundenverwaltung mit Kontaktinformationen  
- Auftragsmanagement mit Leistungen & automatischer Berechnung der Gesamtsumme  
- Filterbare Listen für Kunden & Aufträge  
- Dynamische UI mit ausklappbaren Leistungsdetails  
- Automatische Generierung der Kurzbeschreibung für neue Aufträge  

## 🔧 Installation & Setup

1. **Projekt klonen:**
   ```sh
   git clone https://github.com/deinusername/auftragsverwaltung.git
   cd auftragsverwaltung

## 7. Zugriff auf das Projekt
- Frontend: http://127.0.0.1:8000/
- Admin-Panel: http://127.0.0.1:8000/admin/

## Work in Progress / To-Do

- [x] login für ganze seite!?
- [x] autologout
- [x] leistungs-unit hinzufügen
- [ ] leistungs preis auf aktuell und zum Angebotszeitpunkt ändern
- [x] markiere pflichtfelder
- [x] Auftragsnummer automatisch vorschlagen
- [ ] Rechnungsnummer automatisch vergeben erst wenn Rechnung gestellt wird
- [ ] Filter-Feature erweitern: Auftragsliste und Workshops nach Kunden filtern
- [x] Summenberechnung optimieren: Automatische Berechnung im Backend
- [ ] Testfälle schreiben: Unit-Tests für Models & Views hinzufügen
- [x] python-anywhere - Deploy vorbereiten: Hosting-Setup für Produktion einrichten
- [ ] UX/Forms verbessern: Buttons & Tabellen anpassen
- [ ] Einheit anzeigen bei Leistung-form und Material-form
- [x] hinzufügen der richtigen urls für die event in das Serializer Objekt oder in das model
- [x] kosten bei Workshop - Teilnehmerpreis, Einnahme durch bestätigte Teilnahme*Einzelpreis, Summer der Materialkosten