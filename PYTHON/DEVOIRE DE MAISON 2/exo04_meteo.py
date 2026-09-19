
print("🌡️ --- STATION MÉTÉO CONNECTÉE ---")

print("-" * 45)


temperature = float(input("Quelle est la température extérieure actuelle (°C) ? "))
print(" " + "=" * 40)
print(f"Température relevée : {temperature:.2f} °C")

if temperature >= 28.0:

 print("☀️ CONSEIL : Chaleur estivale !")
 print("T-shirt, short, casquette et eau fraîche obligatoires.")

elif temperature >= 18.0:

 print("⛅ CONSEIL : Temps doux et agréable !")
 print("Un t-shirt ou un sweat léger est parfaitement adapté.")

elif temperature >= 10.0:

 print("🍂 CONSEIL : Temps frais d'automne !")
 print("Prévois un pull chaud ou un blouson pour ne pas attraper froid.")

elif temperature >= 10.0:

 print("❄️ CONSEIL : Grand froid hivernal !")
 print("Manteau épais, écharpe, bonnet et gants de rigueur !")

else:

 print("🌨️ CONSEIL : Conditions extrêmes !")
 print("Reste bien au chaud à l'intérieur et évite de sortir.") 
 
print("=" * 40)