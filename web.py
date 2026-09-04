import streamlit as st
import anthropic
import os
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Oberfläche
st.title("Dokumenten-Tool")
st.write("Lade ein PDF hoch und stelle Fragen dazu.")

# Upload-Feld
hochgeladene_datei = st.file_uploader("PDF auswählen", type="pdf")

if hochgeladene_datei is not None:
    # PDF aus dem Upload einlesen
    reader = PdfReader(hochgeladene_datei)
    dokument = ""
    for seite in reader.pages:
        dokument += seite.extract_text()

    st.success("PDF geladen! Du kannst jetzt Fragen stellen.")

    frage = st.text_input("Deine Frage:")

    if st.button("Absenden"):
        if frage:
            with st.spinner("Claude denkt nach..."):
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
                st.write(antwort.content[0].text)
        else:
            st.warning("Bitte gib zuerst eine Frage ein.")
else:
    st.info("Bitte lade zuerst ein PDF hoch.")