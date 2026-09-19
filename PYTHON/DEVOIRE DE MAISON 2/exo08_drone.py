
print("🛸 --- ORDINATEUR DE BORD DU DRONE CYBER-WING ---")

print("-" * 50)

rep_batterie = input("La batterie est-elle faible (oui/non) ? ").lower()

rep_obstacle = input("Un obstacle est-il détecté à moins de 2 mètres (oui/non) ? ").lower()

rep_vent = input("y a-t'il des vent violent dans la zone (oui/non) ?: ")

batterie_faible = (rep_batterie == "oui")

obstacle_detecte = (rep_obstacle == "oui")

vent_violent = (rep_vent == "oui")

print(" " + "=" * 45)

if not batterie_faible and not obstacle_detecte and not vent_violent :

 print("🟢 TOUS LES VOYANTS SONT AU VERT !")

 print("• Niveau de batterie : OPTIMAL")

 print("• Zone d'envol : TOTALEMENT DÉGAGÉE")

 print("🚁 DÉCOLLAGE IMMÉDIAT : Les moteurs s'allument à 100% !")

else:

 print("🔴 PROCÉDURE DE VOL ANNULÉE — DÉCOLLAGE INTERDIT !")

 if batterie_faible:

  print("⚠️ Alerte capteur : Niveau de batterie critique, recharge nécessaire.")

 if obstacle_detecte:
    
  print("⚠️ Alerte capteur : Obstacle détecté dans le champ des hélices.")

if vent_violent :
    print("⚠️ Alerte capteur : vent violent détecté sur la tracjectoire .")


print("=" * 45)