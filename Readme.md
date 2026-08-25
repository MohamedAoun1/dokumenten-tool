# Dokumenten-Tool

Ein KI-gestütztes Werkzeug, das Fragen zu PDF-Dokumenten in natürlicher Sprache beantwortet. Die Antworten basieren ausschließlich auf dem Inhalt des Dokuments – das Tool erfindet keine Informationen, sondern verweist ehrlich darauf, wenn etwas nicht im Dokument steht.

## Was es kann

- Liest ein PDF-Dokument ein und extrahiert den Text
- Beantwortet Fragen zum Dokument über die Anthropic Claude API
- Antwortet nur auf Basis des Dokuments und kennzeichnet, wenn eine Antwort nicht enthalten ist
- Läuft als interaktiver Chat im Terminal (mehrere Fragen nacheinander)

## Verwendete Technik

- **Python**
- **Anthropic Claude API** für die Sprachverarbeitung
- **pypdf** zum Auslesen von PDF-Dateien
- **python-dotenv** zur sicheren Verwaltung des API-Schlüssels

## Einrichtung

1. Repository klonen und in den Ordner wechseln
2. Virtuelle Umgebung erstellen und aktivieren:
python -m venv venv
.\venv\Scripts\activate
3. Abhängigkeiten installieren:
pip install anthropic pypdf python-dotenv
4. Eine Datei `.env` anlegen und den eigenen API-Schlüssel eintragen:
ANTHROPIC_API_KEY=dein_schluessel_hier
5. Das Tool starten:
python app.py


## Beispiel

Als Testdokument liegt eine erfundene Patienteninformation einer Arztpraxis bei (`praxis_info.pdf`). Beispielhafte Fragen:

- „Wann hat die Praxis samstags geöffnet?"
- „Wer vertritt die Praxis im Urlaub?"
- „Wie bestelle ich ein Folgerezept?"

## Hinweis

Der API-Schlüssel wird über eine `.env`-Datei geladen und ist nicht Teil dieses Repositories.

## Autor

Mohamed Aoun – Wirtschaftsinformatik-Student
