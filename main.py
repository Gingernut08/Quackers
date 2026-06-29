import pygame,  mouse, keyboard, time
from random import randint
from setupVars import WIDTH, HEIGHT, FOOD_OFFSET, duckSize, foods, screen, duckFrontMuteLeftImage, duckFrontMuteRightImage, duckFrontMuteImage, duckEatMuteImage, biteTimes, duckRightMuteImage, duckLeftMuteImage, duckFrontLeftImage, duckFrontRightImage, duckEatImage, duckRightImage, duckRightImage, duckLeftImage, duckFrontImage, quacks, running, hungry, duckPos, noMove, wiggleTime, muted, foodImage, foodnumber, wiggleState
from vars import screenHEIGHT, eatTime, wiggleStationaryTime, wiggleStayTime, wiggleIdleTime, duckSpeed, wiggleSpeed, numBites, backgroundColor, taskbarHeight, alwaysOnTop

def hungry_check(pos): 
    global hungry, hungryTime
    if WIDTH - HEIGHT < pos[0] and screenHEIGHT - HEIGHT - taskbarHeight < pos[1] and not hungry:
        hungry = True
    if hungry and time.time() - hungryTime > eatTime:
        hungry = False
        cycle_image()
    if not (duckPos[0] >= WIDTH - HEIGHT - duckSize and hungry):
        hungryTime = time.time()

def wiggle_check():
    global wiggleState, wiggleTime
    if noMove and time.time() - noMoveTime > wiggleStationaryTime:
        if not wiggleState:
            wiggleTime = time.time()
            wiggleState = True
    if time.time() - wiggleTime > wiggleStayTime:
        wiggleState = False
    if time.time() - wiggleTime > wiggleIdleTime and not hungry:
        wiggleState = True
        wiggleTime = time.time()

def move_duck(pos):
    global duckPos, rightMove, noMove, noMoveTime
    if not wiggleState:
        hungry_check(pos)
    if not hungry:
        wiggle_check()
    if not wiggleState:
        if not hungry:
            duckmove = round(((pos[0] - duckSize // 2) - duckPos[0]) / duckSpeed)
        else:
            duckmove = round(((FOOD_OFFSET +  WIDTH - HEIGHT - duckSize // 2) - duckPos[0]) / duckSpeed)
        duckPos[0] = max(min(duckPos[0] + duckmove, WIDTH - HEIGHT - duckSize), HEIGHT)
        noMove = False
        if duckmove > 0:
            rightMove = True
            noMoveTime = time.time()
        elif duckmove < 0:
            rightMove = False
            noMoveTime = time.time()
        else:
            noMove = True

def cycle_image():
    global foodImage, foodnumber
    foodnumber = (foodnumber - 1) % len(foods)
    foodImage = foods[foodnumber]

def draw_duck(pos):
    move_duck(pos)
    wiggleDir = int((time.time() - wiggleTime) * wiggleSpeed) % 2
    if muted:
        if wiggleState:
            if wiggleDir == 0:
                screen.blit(duckFrontMuteLeftImage, duckPos)
            elif wiggleDir == 1:
                screen.blit(duckFrontMuteRightImage, duckPos)
        elif noMove:
            screen.blit(duckFrontMuteImage, duckPos)
        else:
            if duckPos[0] >= WIDTH - HEIGHT - duckSize and hungry:
                if any([biteTimes[i][0] < time.time() - hungryTime < biteTimes[i][1] for i in range(numBites)]):
                    screen.blit(duckEatMuteImage, duckPos)
                else:
                    screen.blit(duckRightMuteImage, duckPos)
            elif rightMove:
                screen.blit(duckRightMuteImage, duckPos)
            else:
                screen.blit(duckLeftMuteImage, duckPos)
    else:
        if wiggleState:
            if wiggleDir == 0:
                screen.blit(duckFrontLeftImage, duckPos)
            elif wiggleDir == 1:
                screen.blit(duckFrontRightImage, duckPos)
        elif noMove:
            screen.blit(duckFrontImage, duckPos)
        else:
            if duckPos[0] >= WIDTH - HEIGHT - duckSize and hungry:
                if any([biteTimes[i][0] < time.time() - hungryTime < biteTimes[i][1] for i in range(numBites)]):
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
        pygame.mixer.Sound.play(quacks[randint(0, len(quacks) - 1)])

def random_quack(event):
    if randint(0, 50) == 0:
        quack()

def mute_toggle(event):
    global muted
    muted = not muted

mouse.on_click(quack)
keyboard.on_press(random_quack)
keyboard.on_press_key('insert', mute_toggle)

keyboard.press_and_release(alwaysOnTop)
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