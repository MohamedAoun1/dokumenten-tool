import anthropic
import os
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# PDF einlesen und den Text aller Seiten zusammensammeln
reader = PdfReader("praxis_info.pdf")
dokument = ""
for seite in reader.pages:
    dokument += seite.extract_text()

print("Frag etwas zum PDF. Tippe 'ende' zum Beenden.")
print()

while True:
    frage = input("Du: ")

    if frage.lower() == "ende":
        print("Beendet. Bis bald!")
        break

    antwort = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"Hier ist ein Dokument:\n\n{dokument}\n\nBeantworte diese Frage NUR anhand des Dokuments. Wenn die Antwort nicht im Dokument steht, sage das ehrlich.\n\nFrage: {frage}"
            }
        ]
    )

    print()
    print("Claude:", antwort.content[0].text)
    print()