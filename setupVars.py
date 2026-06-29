import pygame, os
from vars import screenWIDTH, screenHEIGHT, numBites, eatTime, taskbarHeight

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1920, 100
x, y = screenWIDTH - WIDTH, screenHEIGHT - HEIGHT - taskbarHeight

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Overlay")

duckSize = 2 * HEIGHT // 3
duckPos = [WIDTH // 2, (HEIGHT - duckSize) // 2]


duckRightImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duck.png").convert_alpha(), [duckSize]*2)
duckLeftImage = pygame.transform.flip(duckRightImage, True, False)
duckRightMuteImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckMute.png").convert_alpha(), [duckSize]*2)
duckLeftMuteImage = pygame.transform.flip(duckRightMuteImage, True, False)

duckEatImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckEat.png").convert_alpha(), [duckSize]*2)
duckEatMuteImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckEatMute.png").convert_alpha(), [duckSize]*2)

duckFrontImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckFront.png").convert_alpha(), [duckSize]*2)
duckFrontLeftImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckFrontTilt.png").convert_alpha(), [duckSize]*2)
duckFrontRightImage = pygame.transform.flip(duckFrontLeftImage, True, False)
duckFrontMuteImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckFrontMute.png").convert_alpha(), [duckSize]*2)
duckFrontMuteLeftImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckFrontTiltMute.png").convert_alpha(), [duckSize]*2)
duckFrontMuteRightImage = pygame.transform.flip(duckFrontMuteLeftImage, True, False)

foods = [pygame.transform.scale(pygame.image.load(f"assets/images/food/food{i}.png").convert_alpha(), [duckSize]*2) for i in range(7)]

numSounds = 6
quacks = [pygame.mixer.Sound("".join(["assets/audio/QUACK_", str(i), ".mp3"])) for i in range(numSounds)]

foodnumber = 6
foodImage = foods[foodnumber]

hungryTime = 0
wiggleTime = 0
noMoveTime = 0

FOOD_OFFSET = 50

noMove = False
running = True
muted = False
rightMove = True
hungry = False
wiggleState = False

biteTime = 0.2
biteInterval = (eatTime - biteTime / 2) / numBites
biteTimes = list(reversed([[eatTime - i * (biteInterval) - biteTime / 2, eatTime - i * (biteInterval) + biteTime / 2] for i in range(numBites)]))