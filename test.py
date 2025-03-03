import requests

url = "http://127.0.0.1:8000/api/kunden/"
response = requests.get(url)

# Prüfen, ob die Anfrage erfolgreich war (Statuscode 200)
if response.status_code == 200:
    print("✅ Erfolgreich!")
    print(response.json())  # JSON-Antwort ausgeben
else:
    print(f"❌ Fehler: {response.status_code}")
    print(response.text)  # Fehlerdetails ausgeben