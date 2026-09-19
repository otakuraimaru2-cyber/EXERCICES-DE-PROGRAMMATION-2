
CODE_PIN = "7421"

MAX_TENTATIVES = 3

print("🔐 --- SYSTÈME DU COFFRE-FORT NUMÉRIQUE ---")

coffre_verrouille = False

while not coffre_verrouille:
    essais = 0
    trouve = False
    print(f"\nTu as droit à {MAX_TENTATIVES} tentatives au maximum.\n")
    
    
    while essais < MAX_TENTATIVES:
        essais += 1
        saisie = input(f"Tentative {essais}/{MAX_TENTATIVES} — Entre le code PIN : ")
        
        if saisie == CODE_PIN:
            print("\n🟢 ACCÈS AUTORISÉ : Le coffre s'ouvre avec un déclic !")
            print(f"Tu as trouvé le trésor en {essais} tentative(s) 🏆 !")
            trouve = True
            coffre_verrouille = True  
            break
        else:
            restants = MAX_TENTATIVES - essais
            if restants > 0:
                print(f"❌ Code erroné ! Il te reste {restants} essai(s).\n")

    
    if not trouve:
        print("\n🔴 ALARME ACTIVÉE : 3 codes erronés ! Le coffre est verrouillé pour 24h 🚨.")
        
        
        action = input("\nEntrez la clé de réinitialisation : ")
        
        if action == "RESET":
            print("\n🔄 Clé acceptée ! Les tentatives sont réinitialisées.")
        
        else:
            print("❌ Clé invalide. Verrouillage définitif !")
            coffre_verrouille = True  