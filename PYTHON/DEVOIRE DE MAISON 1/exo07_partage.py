
print("🍬 --- RÉPARTITEUR ÉQUITABLE DE BONBONS ---")

total_bonbons = int(input("Nombre total de bonbons dans le paquet : "))     

nb_amis = int(input("Nombre d'amis qui partagent : "))

part_par_personne = total_bonbons // nb_amis 

reste_boite = total_bonbons % nb_amis

part_exacte = total_bonbons / nb_amis 

print("=" * 40)

print("         RÉSULTAT DU PARTAGE ")       

print("========================================")

print(f"• Chaque personne reçoit équitablement : {part_par_personne} bonbons.")

print(f"• Il reste dans la boîte pour demain : {reste_boite} bonbon(s).")

print(f"• Part décimale mathématique exacte : {part_exacte} bonbons/pers.")

print("========================================")               