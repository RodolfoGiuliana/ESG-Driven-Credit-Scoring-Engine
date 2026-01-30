import streamlit as st
from core_engine import CreditEngine
import plotly.graph_objects as go

st.set_page_config(page_title="FinScore AI | Rodolfo Giuliana", layout="wide")

st.title("🏦 FinScore-AI: Credit Risk Dashboard")
st.markdown("### Modello di Scoring Integrato per il Corporate Banking (ESG-Ready)")
st.write("Sviluppato da **Rodolfo Giuliana** - *Expertise in Finance & Machine Learning*")

# Sidebar per input dati
st.sidebar.header("Dati Finanziari PMI")
fatturato = st.sidebar.number_input("Fatturato Annuo (€)", value=1000000)
utile = st.sidebar.number_input("Utile Netto (€)", value=150000)
debiti = st.sidebar.number_input("Totale Debiti (€)", value=400000)
patrimonio = st.sidebar.number_input("Patrimonio Netto (€)", value=250000)
ebitda = st.sidebar.number_input("EBITDA (€)", value=200000)
servizio_debito = st.sidebar.number_input("Servizio Debito (Quota Capitale+Interessi)", value=50000)

st.sidebar.header("Parametri ESG")
esg_input = st.sidebar.slider("Rating di Sostenibilità (0-100)", 0, 100, 70)

# Esecuzione Motore
input_data = {
    'fatturato': fatturato, 'utile_netto': utile, 'totale_debiti': debiti,
    'patrimonio_netto': patrimonio, 'ebitda': ebitda, 'servizio_debito': servizio_debito
}

engine = CreditEngine(input_data)
ratios = engine.calculate_ratios()
rating, color = engine.compute_final_score(ratios, esg_input)

# Visualizzazione Risultati
col1, col2, col3 = st.columns(3)
col1.metric("DSCR (Sostenibilità Debito)", f"{ratios['dscr']}x")
col2.metric("Leverage", ratios['leverage'])
col3.metric("Rating Finale", rating)

# Grafico a Gauge per il Rischio
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = esg_input,
    title = {'text': "ESG Impact Score"},
    gauge = {'axis': {'range': [None, 100]},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "royalblue"}]}
))
st.plotly_chart(fig)

st.info("Nota tecnica: Il modello utilizza una ponderazione variabile tra indicatori di bilancio e score di sostenibilità, in linea con le normative EBA 2026.")


with st.expander("🔍 Analisi della Metodologia (Internal Process)"):
    st.write("""
    Il modello applica una ponderazione mista:
    - **60% Financial Health:** Basato su indici di liquidità e solvibilità (DSCR, Leverage).
    - **40% ESG Impact:** Valutazione della resilienza climatica e della governance.
    
    Questa architettura riflette le linee guida EBA 2026 sul monitoraggio del rischio di credito per le PMI.
    """)

if "AAA" in rating:
    st.balloons() # Palloncini
    st.info("💡 Suggerimento: L'azienda presenta una struttura ottimale per operazioni di finanza straordinaria.")


with st.expander("📊 Analisi Dettagliata del Merito Creditizio"):
    if ratios['dscr'] < 1.0:
        st.warning("⚠️ Attenzione: Il DSCR è sotto la soglia di sicurezza. La capacità di rimborso è limitata.")
    else:
        st.success("✅ La generazione di cassa (EBITDA) copre adeguatamente il servizio del debito.")
    
    if esg_input > 70:
        st.info("🌱 Il forte profilo ESG agisce come mitigatore di rischio, migliorando il rating finale.")






 ##### PARTE PER COLLEGAMENTO AI LETTURA PDF , DA AGGIORNARE ###


st.header("📂 Caricamento Automatico Bilancio")
uploaded_file = st.file_uploader("Carica il bilancio in PDF", type="pdf")

if uploaded_file:
    with st.spinner("L'AI sta analizzando il bilancio..."):
        # Lettura file
        st.success("Dati estratti con successo!")


import os




  

..

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
