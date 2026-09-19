import os
import random
import sys
import pygame

pygame.init()

# Configuration de la fenêtre
LARGEUR, HAUTEUR = 600, 600
TAILLE_BLOC = 20
ECRAN = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Serpent (Snake)")
HORLOGE = pygame.time.Clock()

# Couleurs
VERT = (0, 200, 0)
ROUGE = (200, 0, 0)
GRIS_CLAIR = (230, 230, 230)
NOIR = (0, 0, 0)

# Charger les images avec un chemin absolu sécurisé
DOSSIER_COURANT = os.path.dirname(os.path.abspath(__file__))
PATH_SERPENT = os.path.join(DOSSIER_COURANT, "serpent.png")
PATH_POMME = os.path.join(DOSSIER_COURANT, "pomme.png")

AVEC_IMAGES = False
try:
    IMG_SERPENT = pygame.image.load(PATH_SERPENT).convert_alpha()
    IMG_SERPENT = pygame.transform.scale(IMG_SERPENT, (TAILLE_BLOC, TAILLE_BLOC))

    IMG_POMME = pygame.image.load(PATH_POMME).convert_alpha()
    IMG_POMME = pygame.transform.scale(IMG_POMME, (TAILLE_BLOC, TAILLE_BLOC))

    AVEC_IMAGES = True
    print("Images chargées avec succès !")
except Exception as e:
    print(
        f"Images non trouvées ou invalides ({e}), utilisation des formes géométriques."
    )
    AVEC_IMAGES = False


class Serpent:
    def __init__(self):
        self.corps = [(300, 300), (280, 300), (260, 300)]
        self.direction = (TAILLE_BLOC, 0)

    def changer_direction(self, nouvelle_dir):
        # Empêche le serpent de faire un demi-tour direct sur lui-même
        if (nouvelle_dir[0] * -1, nouvelle_dir[1] * -1) != self.direction:
            self.direction = nouvelle_dir

    def deplacer(self):
        tete_x, tete_y = self.corps[0]
        dir_x, dir_y = self.direction
        nouvelle_tete = (tete_x + dir_x, tete_y + dir_y)
        self.corps.insert(0, nouvelle_tete)

    def reduire(self):
        self.corps.pop()

    def afficher(self):
        for segment in self.corps:
            if AVEC_IMAGES:
                ECRAN.blit(IMG_SERPENT, segment)
            else:
                pygame.draw.rect(
                    ECRAN, VERT, (segment[0], segment[1], TAILLE_BLOC, TAILLE_BLOC)
                )
                pygame.draw.rect(
                    ECRAN, NOIR, (segment[0], segment[1], TAILLE_BLOC, TAILLE_BLOC), 1
                )


class Pomme:
    def __init__(self):
        self.position = (0, 0)

    def generer_nouvelle_position(self, corps_serpent):
        while True:
            x = random.randint(0, (LARGEUR // TAILLE_BLOC) - 1) * TAILLE_BLOC
            y = random.randint(0, (HAUTEUR // TAILLE_BLOC) - 1) * TAILLE_BLOC
            self.position = (x, y)
            if self.position not in corps_serpent:
                break

    def afficher(self):
        if AVEC_IMAGES:
            ECRAN.blit(IMG_POMME, self.position)
        else:
            pygame.draw.rect(
                ECRAN,
                ROUGE,
                (self.position[0], self.position[1], TAILLE_BLOC, TAILLE_BLOC),
            )


def afficher_ecran_game_over(score, meilleur_score):
    """Affiche le menu de défaite et attend qu'une touche soit pressée pour relancer."""
    font_titre = pygame.font.Font(None, 50)
    font_texte = pygame.font.Font(None, 32)

    ECRAN.fill(GRIS_CLAIR)

    txt_game_over = font_titre.render("GAME OVER", True, ROUGE)
    txt_score = font_texte.render(f"Score : {score}", True, NOIR)
    txt_meilleur = font_texte.render(f"Meilleur Score : {meilleur_score}", True, NOIR)
    txt_rejouer = font_texte.render("Appuyez sur une touche pour rejouer", True, NOIR)

    ECRAN.blit(txt_game_over, (LARGEUR // 2 - txt_game_over.get_width() // 2, 180))
    ECRAN.blit(txt_score, (LARGEUR // 2 - txt_score.get_width() // 2, 260))
    ECRAN.blit(txt_meilleur, (LARGEUR // 2 - txt_meilleur.get_width() // 2, 300))
    ECRAN.blit(txt_rejouer, (LARGEUR // 2 - txt_rejouer.get_width() // 2, 380))

    pygame.display.flip()

    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                attente = False


def jouer_une_partie(meilleur_score):
    serpent = Serpent()
    pomme = Pomme()
    pomme.generer_nouvelle_position(serpent.corps)

    score = 0
    font = pygame.font.Font(None, 30)
    en_cours = True

    while en_cours:
        ECRAN.fill(GRIS_CLAIR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    serpent.changer_direction((0, -TAILLE_BLOC))
                elif event.key == pygame.K_DOWN:
                    serpent.changer_direction((0, TAILLE_BLOC))
                elif event.key == pygame.K_LEFT:
                    serpent.changer_direction((-TAILLE_BLOC, 0))
                elif event.key == pygame.K_RIGHT:
                    serpent.changer_direction((TAILLE_BLOC, 0))

        # Déplacement du serpent
        serpent.deplacer()

        # Vérification si le serpent mange la pomme
        if serpent.corps[0] == pomme.position:
            score += 1
            pomme.generer_nouvelle_position(serpent.corps)
        else:
            serpent.reduire()

        # Collisions avec les murs
        tete_x, tete_y = serpent.corps[0]
        if (
            tete_x < 0
            or tete_x >= LARGEUR
            or tete_y < 0
            or tete_y >= HAUTEUR
        ):
            en_cours = False

        # Collision avec son propre corps
        if serpent.corps[0] in serpent.corps[1:]:
            en_cours = False

        # Affichage des éléments
        pomme.afficher()
        serpent.afficher()

        # Affichage des scores
        txt_score = font.render(f"Score: {score}", True, NOIR)
        txt_meilleur = font.render(f"Meilleur: {max(score, meilleur_score)}", True, NOIR)
        ECRAN.blit(txt_score, (10, 10))
        ECRAN.blit(txt_meilleur, (10, 35))

        pygame.display.flip()
        HORLOGE.tick(10)

    # Mise à jour du meilleur score
    if score > meilleur_score:
        meilleur_score = score

    # Afficher l'écran de fin et attendre l'appui sur une touche
    afficher_ecran_game_over(score, meilleur_score)

    return meilleur_score


def main():
    meilleur_score = 0
    while True:
        meilleur_score = jouer_une_partie(meilleur_score)


if __name__ == "__main__":
    main()