import pygame, os, mouse, keyboard, mouse, time
from random import randint
from vars import foodnumber, foodImage, foods, screen, hungry, x, y, WIDTH, HEIGHT, duckEatImage, duckEatMuteImage, screenHEIGHT, running, duckSize, duckPos, muted, duckSpeed, duckRightMuteImage, duckLeftImage, duckLeftMuteImage, duckRightImage, quacks, numSounds, backgroundColor

def hungry_check(pos): 
    global hungry, hungryTime
    if WIDTH - HEIGHT < pos[0] and screenHEIGHT - HEIGHT - 45 < pos[1] and not hungry:
        hungry = True
    if hungry and time.time() - hungryTime > 3:
        hungry = False
        cycle_image()
    if not (duckPos[0] >= WIDTH - HEIGHT - duckSize and hungry):
        hungryTime = time.time()

def move_duck(pos):
    global duckPos, rightMove
    hungry_check(pos)
    if not hungry:
        duckmove = round(((pos[0] - duckSize // 2) - duckPos[0]) / duckSpeed)
    else:
        duckmove = round(((50 +  WIDTH - HEIGHT - duckSize // 2) - duckPos[0]) / duckSpeed)
    duckPos[0] = max(min(duckPos[0] + duckmove, WIDTH - HEIGHT - duckSize), HEIGHT)
    if duckmove > 0:
        rightMove = True
    elif duckmove < 0:
        rightMove = False

def cycle_image():
    global foodImage, foodnumber
    foodnumber = (foodnumber - 1) % 7
    foodImage = foods[foodnumber]

def draw_duck(pos):
    move_duck(pos)
    if muted:
        if duckPos[0] >= WIDTH - HEIGHT - duckSize and hungry:
            if 0.9 < time.time() - hungryTime < 1.1:
                screen.blit(duckEatMuteImage, duckPos)
            elif 1.9 < time.time() - hungryTime < 2.1:
                screen.blit(duckEatMuteImage, duckPos)
            elif 2.9 <= time.time() - hungryTime:
                screen.blit(duckEatMuteImage, duckPos)
            else:
                screen.blit(duckRightMuteImage, duckPos)
        elif rightMove:
            screen.blit(duckRightMuteImage, duckPos)
        else:
            screen.blit(duckLeftMuteImage, duckPos)
    else:
        if duckPos[0] >= WIDTH - HEIGHT - duckSize and hungry:
            if 0.9 < time.time() - hungryTime < 1.1:
                screen.blit(duckEatImage, duckPos)
            elif 1.9 < time.time() - hungryTime < 2.1:
                screen.blit(duckEatImage, duckPos)
            elif 2.9 <= time.time() - hungryTime:
                screen.blit(duckEatImage, duckPos)
            else:
                screen.blit(duckRightImage, duckPos)
        elif rightMove:
            screen.blit(duckRightImage, duckPos)
        else:
            screen.blit(duckLeftImage, duckPos)
    screen.blit(foodImage, (WIDTH - HEIGHT, duckPos[1]))

def quack():
    if not muted:
        pygame.mixer.stop()
        pygame.mixer.Sound.play(quacks[randint(0, numSounds - 1)])

def random_quack(event):
    if randint(0, 50) == 0:
        quack()

def mute_toggle(event):
    global muted
    muted = not muted

pygame.init()
pygame.mixer.init()


keyboard.press_and_release('alt+shift+t')
mouse.on_click(quack)
keyboard.on_press(random_quack)
keyboard.on_press_key('insert', mute_toggle)




clock = pygame.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if keyboard.is_pressed('escape'):
        running = False
    
    screen.fill(backgroundColor)
    draw_duck(mouse.get_position())
    pygame.display.flip()
    clock.tick(30)

pygame.quit()