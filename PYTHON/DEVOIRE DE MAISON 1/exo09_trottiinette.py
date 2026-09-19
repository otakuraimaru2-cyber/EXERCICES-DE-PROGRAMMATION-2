
print("🛴 --- CALCULATEUR DE TRAJET EN TROTTINETTE / VÉLO ---")

print(" ")
print(" ")

distance_km = float(input("quel est la distance que vous devez parcouru ? (en km) : "))

vitesse_kmh = float(input("quel est votre vitesse moyenne ? (en km/h) : "))

temps_heures = distance_km / vitesse_kmh

temps_minutes = temps_heures * 60

temps_secondes = temps_minutes * 60

temps_total = temps_minutes + 3

temps_total_seconde = temps_total * 60

print(" ")

print("========================================")

print("          FEUILLE DE ROUTE              ")

print("========================================")
print(f"• Distance à parcourir : {distance_km:.2f} km")

print(f"• Vitesse moyenne      : {vitesse_kmh:.2f} km/h")

print(f"• Temps de trajet (en heure)      :  {temps_heures:.2f}heures")

print(f"• Temps de trajet (en minute)     : {temps_minutes:.2f} minutes")

print(f"• Temps de trajet (en seconde)    : {int(temps_secondes)} secondes.")

print(f"• Temps total effectuer           : {temps_total} minutes ({int(temps_total_seconde)} secondes)")

print("========================================")

print(" ")

print("⚠️ N'oublie pas ton casque et respecte le code de la route !")