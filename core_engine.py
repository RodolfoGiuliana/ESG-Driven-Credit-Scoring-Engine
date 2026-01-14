import numpy as np

class CreditEngine:
    def __init__(self, data):
        self.data = data

    def calculate_ratios(self):
        """Calcola i KPI finanziari fondamentali."""
        try:
            leverage = self.data['totale_debiti'] / self.data['patrimonio_netto']
            # DSCR (Debt Service Coverage Ratio)
            dscr = self.data['ebitda'] / self.data['servizio_debito']
            ros = (self.data['utile_netto'] / self.data['fatturato']) * 100
            
            return {
                'leverage': round(leverage, 2),
                'dscr': round(dscr, 2),
                'ros': round(ros, 2)
            }
        except ZeroDivisionError:
            return {'leverage': 0, 'dscr': 0, 'ros': 0}

    def compute_final_score(self, ratios, esg_score):
        """
        Algoritmo di Scoring Integrato.
        Logica: 60% Finanziario, 40% ESG (Risk Mitigation).
        """
        # Score Finanziario (0-100)
        # Un DSCR > 1.2 è positivo, un Leverage < 3 è positivo
        fin_score = 0
        if ratios['dscr'] > 1.2: fin_score += 50
        if ratios['leverage'] < 3: fin_score += 50
        
        # Integrazione ESG
        # Un alto ESG score riduce la probabilità di default
        total_score = (fin_score * 0.6) + (esg_score * 0.4)
        
        if total_score > 80: return "AAA - Eccellente", "green"
        if total_score > 60: return "BBB - Investment Grade", "yellow"
        if total_score > 40: return "BB - Monitoraggio", "orange"
        return "D - High Risk", "red"
