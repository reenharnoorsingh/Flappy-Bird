import random  # for the generation of rasndom numbers
import sys  # sys.exit will be used to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports

# Global Variables
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
# initialises a window for display
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\bird.png"
BACKGROUND = r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\bg.png"
PIPE = r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\pipe.png"


def welcomeScreen():  # shows welcome screen
    playerx = int(SCREENHEIGHT/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if the user presses the cross or escape, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if the user presses space or up, start the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
'''
def mainGame():
    score =0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/5)
    basex = 0
'''
if __name__ == "__main__":
    # main function
    pygame.init()  # initialize pygame module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Harnoor Singh')
    GAME_SPRITES['numbers'] = (
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\0.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\1.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\2.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\3.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\4.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\5.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\6.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\7.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\8.png").convert_alpha(),
        pygame.image.load(
            r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\9.png").convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\tile.png").convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\sprites\base.png").convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180,),
        pygame.image.load(PIPE).convert_alpha()
    )
    # Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\audio\die.wav")
    GAME_SOUNDS['hit'] = pygame.mixer.Sound(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\audio\hit.wav")
    GAME_SOUNDS['point'] = pygame.mixer.Sound(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\audio\point.wav")
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\audio\swoosh.wav")
    GAME_SOUNDS['wing'] = pygame.mixer.Sound(
        r"C:\Users\Harnoor Singh\Documents\GitHub\Flappy-Bird\gallery\audio\wing.wav")

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()  # shows the welcome screen
        mainGame()  # main function
