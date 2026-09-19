
print("⚔️ --- GÉNÉRATEUR DE CARTE CYBER-HÉROS ---")

print(" ")

pseudo = input("Pseudo du héros                : ")

guilde = input("Nom de ta guilde               : ")

niveau = int(input("Niveau actuel                  : "))

attaque = int(input("Attaque de base (points)       : "))

defense = int(input("Défense de bouclier (points)   : "))

or_total = int(input("Crédits d'or en poche          : "))

print(" ")

PRIX_COFFRE = 80

puissance_ultime = (attaque ** 2) + (niveau * 10) 

ratio_combat = float(attaque / defense)

coffres_achetables = or_total // PRIX_COFFRE 

or_restant = or_total % PRIX_COFFRE 

pv_max = 100 + niveau * 25

rang = (niveau +10) //10



print("" + "╔" + "═" * 54 + "╗")

print("║                CARTE OFFICIELLE DE HÉROS             ║")

print("╠" + "═" * 54 + "╣")

print(f"║ Héros  : {pseudo:<18} Guilde : {guilde:<14}  ║")

print(f"║ Niveau : {niveau:<18} Statut : Actif en ligne  ║")

print(f"║ rang   : {rang:<42}  ║")

print("╠" + "═" * 54 + "╣")

print("║                 STATISTIQUES DE COMBAT               ║")  

print(f"║ • Attaque de base     : {attaque:<24} pts ║")

print(f"║ • pv maximal          : {pv_max:<24} pts ║")

print(f"║ • Défense de bouclier : {defense:<24} pts ║")

print(f"║ • Ratio Attaque/Déf   : {ratio_combat:<28.2f} ║")

print(f"║ • PUISSANCE ULTIME    : {puissance_ultime:<24} pts ║")

print("╠" + "═" * 54 + "╣")

print("║             INVENTAIRE & COFFRES D'ARMES             ║")

print(f"║ • Coffres achetables  : {coffres_achetables:<28} ║")

print(f"║ • Monnaie restante    : {or_restant:<15} crédits d'or ║")

print("╚" + "═" * 54 + "╝")

print(" ")

print("🎉 Félicitations ! votre profil de héros est prêt pour la bataille !")