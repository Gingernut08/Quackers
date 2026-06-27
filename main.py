import pygame, os, mouse, keyboard

screenWIDTH, screenHEIGHT = 1920, 1080
WIDTH, HEIGHT = 1920, 200
x, y = screenWIDTH - WIDTH, screenHEIGHT - HEIGHT

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Overlay")

running = True


duckPos = [WIDTH // 2, 50]

keyboard.press_and_release('alt+shift+t')

def draw_duck(pos):
    global duckPos
    duckPos[0] += (pos[0] - duckPos[0]) // 50
    duckPos[0] = max(min(duckPos[0], WIDTH - 200), 100)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(duckPos[0], duckPos[1], 100, 100))


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
    screen.fill((255, 0, 0))
    draw_duck(mouse.get_position())
    pygame.display.flip()
    clock.tick(30)

pygame.quit()