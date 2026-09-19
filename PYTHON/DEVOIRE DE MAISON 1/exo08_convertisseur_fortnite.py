TAUX_CONVERSION = 125.0 

print("🎮 --- CONVERTISSEUR ARGENT DE POCHE ↔ MONNAIE DE JEU ---")

print(" ")

budget_euros = float(input("Combien d'argent de poche as-tu en euros (€) ? "))

prix_skin_vbucks = int(input("Combien coûte le skin de tes rêves en V-Bucks ? "))

vbucks_max = int(budget_euros * TAUX_CONVERSION)

cout_reel_euros = prix_skin_vbucks / TAUX_CONVERSION

argent_restant_euros = budget_euros - cout_reel_euros

print(" ")

print("=============================================")

print("            ANALYSE DE BUDGET                ")

print("=============================================")

print(f"• Avec {budget_euros:.2f} €, tu obtiens : {vbucks_max} VBucks.")

print(f"• Coût réel du skin souhaité : {cout_reel_euros:.2f} €.")

print(f"• Argent de poche restant après achat : {argent_restant_euros:.2f} €.")

print("=============================================")