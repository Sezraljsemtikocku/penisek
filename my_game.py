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
font = pygame.font.Font('8-BIT WONDER.TTF', 12)
mouse = pygame.image.load("Mouse.png")
backgroundV2 = pygame.image.load("v2.png")
mouse_size = 16
mouse_count = -1 # -1 because the spawn also increments this counter
cat_w = 56
cat_h = 41

#check which blocks are empty
empty_space = []
hpixel = 0
wpixel = 0
empty_space_message = "Empty blocks: "
while hpixel < DISPLAY_H:
    wpixel = 0
    while wpixel < DISPLAY_W:
        if background.get_at((wpixel, hpixel))[3] == 0:
            empty_space.append([wpixel, hpixel])
            empty_space_message += str(wpixel) + ", " + str(hpixel) + "; "
        wpixel += 16
    hpixel += 16
    if not empty_space_message.endswith("\n"):
        empty_space_message += "\n"
print(empty_space_message)

#check which blocks are above the floor
floor_blocks = []
for key, value in enumerate(empty_space):
    x, y = value
    block_below = [x, y + 16]

    if block_below not in empty_space:
        floor_blocks.append(empty_space[key])

################################# LOAD PLAYER ###################################
cat = Player()
################################# GAME LOOP ##########################
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
    
    
    if mouse_count < 0 or check_mouse(mousex, mousey, catx, caty):
        block = random.randrange(0, len(floor_blocks))
        mousex, mousey = floor_blocks[block][0], floor_blocks[block][1]
        while check_mouse(mousex, mousey, catx, caty):
            block = random.randrange(0, len(floor_blocks))
            mousex, mousey = floor_blocks[block][0], floor_blocks[block][1]
        print("spawned a mouse at", mousex, mousey)
        mouse_count += 1
        print("Mouse count:", mouse_count)

    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((255,255,255))
    canvas.blit(backgroundV2, (0, 0))
    canvas.blit(background, (0,0))
    cat.draw(canvas)
    window.blit(canvas, (0,0))
    window.blit(mouse, (mousex, mousey))
    counter_text = font.render("Score - " + str(mouse_count), True, (0, 0, 0))
    window.blit(counter_text, (10, 10))
    pygame.display.update()


