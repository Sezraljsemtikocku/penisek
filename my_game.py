import pygame
import random
from player import Player


################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 272
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
background = pygame.image.load('background.png').convert_alpha()
mouse = pygame.image.load("Mouse.png")
mouse_size = 16
cat_w = 56
cat_h = 41
#check which blocks are empty
empty_space = []
hpixel = 0
wpixel = 0
while hpixel < DISPLAY_H:
    wpixel = 0
    while wpixel < DISPLAY_W:
        if background.get_at((wpixel, hpixel))[3] == 0:
            empty_space.append([wpixel, hpixel])
            print(wpixel, hpixel)
        wpixel += 16
    hpixel += 16

################################# LOAD PLAYER ###################################
cat = Player()
################################# GAME LOOP ##########################
mousex, mousey = random.randrange(0, 480, 5), random.randrange(235, 240 , 5)
while running:
    clock.tick(60)

    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY, cat.FACING_LEFT = True, True
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY, cat.FACING_LEFT = True, False
            elif event.key == pygame.K_UP:
                cat.UP_KEY = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY = False
            elif event.key == pygame.K_UP:
                cat.UP_KEY = False
    
    ################################# UPDATE/ Animate SPRITE #################################
    cat.update(empty_space)
    catx = cat.rect.x
    caty = cat.rect.y
    
    ########## MOUSE CHECK ########

    def check_mouse(mousex, mousey, catx, caty ):
        if(catx - mousex) <= mouse_size and (mousex - catx) <= cat_w:
            if(caty - mousey) <= mouse_size and (mousey - caty) <= cat_h:
                return True
        
        return False

    if check_mouse(mousex, mousey, catx, caty):
        mousex, mousey = random.randrange(0, 480, 5), random.randrange(235, 245, 5)

    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((255,255,255))
    canvas.blit(background, (0,0))
    cat.draw(canvas)
    window.blit(canvas, (0,0))
    window.blit(mouse, (mousex, mousey))
    pygame.display.update()


