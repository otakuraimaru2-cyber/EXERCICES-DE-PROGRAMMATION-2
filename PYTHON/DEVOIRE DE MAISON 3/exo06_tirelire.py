
OBJECTIF = float(input("quel est le prix votre objec"))
 
solde = 0.0 
 
semaine = 0 
 
 
print("💰 --- SUIVI DE LA TIRELIRE ÉPARGNE ---") 
 
print(f"Objectif d'achat de la console : {OBJECTIF:.2f} €\n") 
 
 
while solde < OBJECTIF: 
 
    semaine += 1 
 
    depot = float(input(f"Semaine {semaine} — Combien ajoutes-tu (€) ? ")) 
 
    solde += depot 
 
     
 
    if solde < OBJECTIF: 
 
        manque = OBJECTIF - solde 
 
        print(f"-> Solde actuel : {solde:.2f} €, il vous manque encore {manque:.2f} € à économiser\n") 
 
    else: 
 
        surplus = solde - OBJECTIF 
 
        print(f"-> Solde actuel : {solde:.2f} €, vous avez depasser votre objectif de {surplus:.2f} € !\n") 
 
 
print(f"🎉 BRAVO ! Objectif atteint en {semaine} semaine(s) ! Tu peux acheter ta console 🎮 !")