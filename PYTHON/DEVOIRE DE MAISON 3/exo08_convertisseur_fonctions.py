
def km_vers_miles(km):
 return km * 0.621371

def celsius_vers_fahrenheit(celsius):
 return (celsius * 9/5) + 32

def euro_vers_vbucks(euro) :
 return euro * 125

print("📐 --- MODULE SCIENTIFIQUE DE CONVERSION ---")

dist_km = float(input("Entre une distance en km : "))

temp_c = float(input("Entre une température en °C : "))

euro = float(input("quel somme avez vous ?: "))

dist_miles = km_vers_miles(dist_km)
temp_f = celsius_vers_fahrenheit(temp_c)
vbuks = euro_vers_vbucks(euro)

print("\n" + "=" * 40)

print("RÉSULTATS DES CONVERSIONS :")

print(f"• {dist_km:.2f} km = {dist_miles:.2f} miles")

print(f"• {temp_c:.2f} °C = {temp_f:.2f} °F")

print(f"• {euro:.2f} € = {vbuks:.2f} ")

print("========================================")