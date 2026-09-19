nombres_de_maÏs=input("quel est le nombre de maÏs ?:")
prix_de_un_maÏs=input("quel est le prix d'un mais ?:")

nombres_de_carotte=input("quel est le nombre de carotte ?:")
prix_de_une_carotte=input("quel est le prix d'une carotte ?:")

nombres_de_maÏs_chiffre=int(nombres_de_maÏs)
nombres_de_carotte_chiffre=int(nombres_de_carotte)

prix_maÏs_chiffre=int(prix_de_un_maÏs)
prix_carotte_chiffre=int(prix_de_une_carotte)

prix_Total_mais=nombres_de_maÏs_chiffre * prix_maÏs_chiffre
prix_total_carotte=nombres_de_carotte_chiffre * prix_carotte_chiffre

prix_total = prix_Total_mais + prix_total_carotte
print(prix_total)