import pygame
from game import Game

pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arrire plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

running = True

# Boucle de jeu
while running:

    # Appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200)) # applique une surface à un endroit de la fenetre
    
    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Vérifier si le joueur souhaite aller à droite ou à gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    
    #print(game.player.rect.x)
    
    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que l'évènement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeu')
        # Détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False