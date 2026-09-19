
print("🏛️ --- DESSINATEUR DE PYRAMIDES GÉOMÉTRIQUES ---")

hauteur = int(input("\n Hauteur de la pyramide (nombre d'étages) : "))

symbole = input("\n Choisis un symbole (ex: *, #, @) : ")

print(f"\nVoici ta pyramide de {hauteur} étages :")

for etape in range( hauteur, 0, -1):

 print(symbole * etape)

print("\n🎉 Pyramide construite avec succès !")
