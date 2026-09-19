import os
import random
import sys
import pygame

pygame.init()

LARGEUR, HAUTEUR = 800, 400
ECRAN = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Dinosaure Pro")
HORLOGE = pygame.time.Clock()

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (200, 0, 0)

# Déterminer le dossier où se trouve le script Python
DOSSIER_COURANT = os.path.dirname(os.path.abspath(__file__))

# Chargement sécurisé des images
try:
    chemin_dino = os.path.join(DOSSIER_COURANT, "dino.png")
    chemin_cactus = os.path.join(DOSSIER_COURANT, "cactus.png")
    chemin_ptero = os.path.join(DOSSIER_COURANT, "pterodactyle.png")

    IMG_DINO = pygame.image.load(chemin_dino)
    IMG_DINO = pygame.transform.scale(IMG_DINO, (50, 50))
    
    IMG_CACTUS = pygame.image.load(chemin_cactus)
    IMG_CACTUS = pygame.transform.scale(IMG_CACTUS, (30, 50))
    
    IMG_PTERO = pygame.image.load(chemin_ptero)
    IMG_PTERO = pygame.transform.scale(IMG_PTERO, (40, 30))
    
    AVEC_IMAGES = True
    print("🟢 Toutes les images ont été chargées avec succès !")
except Exception as e:
    AVEC_IMAGES = False
    print(f"⚠️ Impossible de charger les images : {e}")
    print("-> Le jeu utilisera les formes géométriques par défaut.")

class Dinosaure:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.largeur = 50
        self.hauteur = 50
        self.saut = False
        self.vitesse_y = 0
        self.gravite = 0.8

    def afficher(self):
        if AVEC_IMAGES:
            ECRAN.blit(IMG_DINO, (self.x, self.y))
        else:
            pygame.draw.rect(ECRAN, NOIR, (self.x, self.y, self.largeur, self.hauteur))

    def mettre_a_jour(self):
        if self.saut:
            self.y += self.vitesse_y
            self.vitesse_y += self.gravite
            if self.y >= 300:
                self.y = 300
                self.saut = False

    def sauter(self):
        if not self.saut:
            self.saut = True
            self.vitesse_y = -14

class CactusGroupe:
    def __init__(self):
        self.nombre = random.randint(1, 3)
        self.largeur_unitaire = 25
        self.largeur = self.nombre * self.largeur_unitaire
        self.hauteur = random.choice([40, 50, 60])
        self.x = LARGEUR
        self.y = 350 - self.hauteur
        self.vitesse = 8

    def afficher(self):
        for i in range(self.nombre):
            pos_x = self.x + (i * self.largeur_unitaire)
            if AVEC_IMAGES:
                img_redim = pygame.transform.scale(IMG_CACTUS, (self.largeur_unitaire, self.hauteur))
                ECRAN.blit(img_redim, (pos_x, self.y))
            else:
                pygame.draw.rect(ECRAN, NOIR, (pos_x, self.y, self.largeur_unitaire, self.hauteur))

    def mettre_a_jour(self):
        self.x -= self.vitesse

class Pterodactyle:
    def __init__(self):
        self.x = LARGEUR
        self.y = random.choice([250, 290])
        self.largeur = 40
        self.hauteur = 30
        self.vitesse = 10

    def afficher(self):
        if AVEC_IMAGES:
            ECRAN.blit(IMG_PTERO, (self.x, self.y))
        else:
            pygame.draw.rect(ECRAN, ROUGE, (self.x, self.y, self.largeur, self.hauteur))
            
    def mettre_a_jour(self):
        self.x -= self.vitesse

def jouer(meilleur_score):
    dino = Dinosaure()
    obstacles = []
    prochain_espacement = random.randint(250, 500)
    score = 0
    font = pygame.font.Font(None, 36)
    en_cours = True

    while en_cours:
        ECRAN.fill(BLANC)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.sauter()

        dino.mettre_a_jour()
        dino.afficher()

        if len(obstacles) == 0 or (LARGEUR - obstacles[-1].x) >= prochain_espacement:
            if random.random() < 0.3 and score > 5:
                obstacles.append(Pterodactyle())
            else:
                obstacles.append(CactusGroupe())
            
            prochain_espacement = random.randint(250, 550)

        for obstacle in list(obstacles):
            obstacle.mettre_a_jour()
            obstacle.afficher()

            rect_dino = pygame.Rect(dino.x, dino.y, dino.largeur, dino.hauteur)
            rect_obs = pygame.Rect(obstacle.x, obstacle.y, obstacle.largeur, obstacle.hauteur)

            if rect_dino.colliderect(rect_obs):
                en_cours = False

            if obstacle.x < -obstacle.largeur:
                obstacles.remove(obstacle)
                score += 1

        pygame.draw.line(ECRAN, NOIR, (0, 350), (LARGEUR, 350), 2)
        
        texte_score = font.render(f"HI: {meilleur_score}   Score: {score}", True, NOIR)
        ECRAN.blit(texte_score, (LARGEUR - 250, 20))

        pygame.display.flip()
        HORLOGE.tick(60)

    # Écran Game Over
    font_go = pygame.font.Font(None, 60)
    texte_go = font_go.render("GAME OVER", True, ROUGE)
    rect_go = texte_go.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 20))
    ECRAN.blit(texte_go, rect_go)

    font_relance = pygame.font.Font(None, 30)
    texte_relance = font_relance.render("Appuyez sur ESPACE pour recommencer", True, NOIR)
    rect_relance = texte_relance.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 + 30))
    ECRAN.blit(texte_relance, rect_relance)

    pygame.display.flip()

    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                attente = False

    return score

if __name__ == "__main__":
    record = 0
    while True:
        score_de_la_partie = jouer(record)
        if score_de_la_partie > record:
            record = score_de_la_partie