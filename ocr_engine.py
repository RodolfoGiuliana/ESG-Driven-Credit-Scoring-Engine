import fitz  # PyMuPDF
from openai import OpenAI
import json

client = OpenAI(api_key="LA_TUA_CHIAVE_QUI")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_financial_data_ai(text):
    prompt = f"""
    Sei un esperto analista finanziario. Estrai i seguenti dati dal testo del bilancio fornito.
    Rispondi SOLO con un formato JSON con queste chiavi: 
    fatturato, utile_netto, totale_debiti, patrimonio_netto, ebitda, servizio_debito.
    
    Testo del bilancio:
    {text}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.message.content)
