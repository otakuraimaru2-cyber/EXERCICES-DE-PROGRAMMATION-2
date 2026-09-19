
def article():
    n_chaise = int(input("quel est le nombre de chaises vendue  ?: "))

    n_table = int(input("quel est le nombre de tables vendue ?:"))

    total_article_mois = n_chaise + n_table
    cumule_article = total_article_mois
    
    
    for nombre_de_mois in range(12):
        print (cumule_article)
        if nombre_de_mois >= 12 - 1:
            print("Programme terminee") 
        
        else :
          n_chaise = int(input("quel est le nombre de chaises vendue pour ce mois ci ?: "))
          n_table = int(input("quel est le nombre de tables vendue pour ce mois ci ?:"))
        
          nouveau_total_mois = n_chaise + n_table
        
          cumule_article = cumule_article + nouveau_total_mois
        
article()        
        