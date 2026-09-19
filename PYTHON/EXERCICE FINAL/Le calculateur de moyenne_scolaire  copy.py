
eleve = {"NOM" : input("quel est votre nom ? : "),
         "prenom" : input("quel est votre prenom ? : "),
         "classe" : input("quel est votre classe ? : ")
        }

coeficient = {"mathematique" : 3, 
              "francais" : 3,
              "pct" : 3,
              "eps" : 1,
              "histo-geo" : 2,
              "ecm" : 2,
              "svt" : 2,
              "anglais" : 2
             }

matieres = ["mathematique",
            "francais",
            "pct",
            "eps",
            "histo-geo",
            "ecm",
            "svt",
            "anglais"
           ]

def calculer_moyenne_class():
    (note_1_devoire + note_2_devoire + note_1_interrogation + note_2_interrogation) / 4
    return moyenne_classe



def calculer_moyenne_compo():
    (cmoyenne_class + note_composition)/ 2


for matiere in matieres :
    
    
    print(f"donner vos notes de {matiere}")
    note_1_devoire = float(input("quel est votre note du premiers devoir ? : "))
    note_2_devoire =float(input("quel est votre note du second devoir ? : "))
    note_1_interrogation = float(input("quel est votre note de la premiere interrogation ? : "))
    note_2_interrogation = float(input("quel est votre note de la seconde interrogation ? : "))
    moyenne_classe = calculer_moyenne_class()
    note_composition = float(input("quel est votre note de la composition ? : "))
           
    if (note_1_devoire, note_2_devoire, note_1_interrogation,note_2_interrogation,note_composition) >20 or (note_1_devoire, note_2_devoire, note_1_interrogation,note_2_interrogation,note_composition) <0 :
        print ("erreure de saisie")
    print(f"{matiere} : moyenne de classe  note de composition  moyenne de composition")
    print(f"            {moyenne_classe}   {note_composition}    {moyenne_compo}")


    
