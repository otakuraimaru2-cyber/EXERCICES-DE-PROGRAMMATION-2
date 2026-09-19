a = int(input("quelle table voulez vous ?:"))
c = input("quelle operation voulez vous ?:")

if c == "soustraction":
    signe = "-"
elif c == "addition":
   signe = "+" 
elif c == "multiplication":
    signe = "*"
elif c == "division":         
    signe = "/"
    
def operations(b):
    resultat=0
    if c == "soustraction": 
        resultat = b - a
        
    elif c == "addition":
        resultat = b + a 
    elif c == "multiplication":
        resultat = b * a
    elif c == "division": 
         resultat = b // a
    else:
        print("Erreur de signe ou de table")
        
    return resultat

for nombre in range (13):
    print(f"{nombre} {signe} {a} = {operations(nombre)}")
    

        
     