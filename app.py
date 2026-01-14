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
