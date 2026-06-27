import pygame, os

pygame.init()
pygame.mixer.init()


backgroundColor = (28, 28, 28)

screenWIDTH, screenHEIGHT = 1920, 1080
WIDTH, HEIGHT = 1920, 100
x, y = screenWIDTH - WIDTH, screenHEIGHT - HEIGHT - 45

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Overlay")

duckSpeed = 50
duckSize = 2 * HEIGHT // 3
duckPos = [WIDTH // 2, (HEIGHT - duckSize) // 2]


numSounds = 6
quacks = [pygame.mixer.Sound("".join(["assets/audio/QUACK_", str(i), ".mp3"])) for i in range(numSounds)]


duckRightImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duck.png").convert_alpha(), [duckSize]*2)
duckLeftImage = pygame.transform.flip(duckRightImage, True, False)
duckRightMuteImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckMute.png").convert_alpha(), [duckSize]*2)
duckLeftMuteImage = pygame.transform.flip(duckRightMuteImage, True, False)

duckEatMuteImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckEatMute.png").convert_alpha(), [duckSize]*2)
duckEatImage = pygame.transform.scale(pygame.image.load("assets/images/duck/duckEat.png").convert_alpha(), [duckSize]*2)

foods = [pygame.transform.scale(pygame.image.load(f"assets/images/food/food{i}.png").convert_alpha(), [duckSize]*2) for i in range(7)]

foodnumber = 6
foodImage = foods[foodnumber]

hungryTime = 0

running = True
muted = False
rightMove = True
hungry = False