
PRIX_BURGER = 9.99
PRIX_BOISSON = 5.30
PRIX_FRITE = 2.50

print("🍔 --- COMMANDE PIXEL-BURGER ---")

qte_burgers = int(input(f"Combien de Mega Burgers ({PRIX_BURGER} €) ? "))

qte_boissons = int(input(f"Combien de Boissons fraîches ({PRIX_BOISSON} €) ? "))

qte_frites = int(input(f"Combien de Grandes Frites ({PRIX_FRITE} €) ? "))

billet_donner = int(input("avec quel billet compter vous payer ?:"))


total_burgers = qte_burgers * PRIX_BURGER

total_boissons = qte_boissons * PRIX_BOISSON

total_frites = qte_frites * PRIX_FRITE

total_general = total_burgers + total_boissons + total_frites

monnais = billet_donner - total_general

print(" ")
print(" ")

print("========================================")

print(" TICKET DE CAISSE ")

print("========================================")

print(f"• {qte_burgers} x Mega Burger : {total_burgers} €")

print(f"• {qte_boissons} x Boisson : {total_boissons} €")

print(f"• {qte_frites} x Grande Frite : {total_frites} €")

print("-" * 40)

print(f"TOTAL À PAYER : {total_general} €")

print("========================================")

print("Merci pour votre achat et bon appétit")