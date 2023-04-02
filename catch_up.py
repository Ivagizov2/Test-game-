from pygame import *


def my_sprite_collide(x1, y1, x2, y2):
    if x1 <= x2 <= x1 +80 and y1 <= y2 <= y1 +80:
        return True
    return False 

#главное окно 
main_win = display.set_mode((800, 600))
display.set_caption("Догонялки")

bg = transform.scale(image.load("background.png"), (800,600))

#спрайты
ghost1 = transform.scale(image.load("sprite1.png"), (80, 80))
ghost2 = transform.scale(image.load("sprite2.png"), (80, 80))

#переменые 
run = True
clock = time.Clock()
ghost1_XCore = 100
ghost1_YCore = 300
ghost2_XCore = 300
ghost2_YCore = 300

while run:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and ghost1_YCore > 0:
        ghost1_YCore -= 10
    if keys_pressed[K_DOWN] and ghost1_YCore < 520:
        ghost1_YCore += 10 
    if keys_pressed[K_LEFT] and ghost1_XCore > 0:
        ghost1_XCore -= 10
    if keys_pressed[K_RIGHT] and ghost1_XCore < 720 :
        ghost1_XCore += 10
        
    keys_pressed = key.get_pressed()
    if keys_pressed[K_w] and ghost2_XCore > 0:
        ghost2_XCore -= 10
    if keys_pressed[K_s] and ghost2_XCore < 520:
        ghost2_XCore += 10 
    if keys_pressed[K_a] and ghost2_YCore > 0:
        ghost2_YCore -= 10
    if keys_pressed[K_d] and ghost2_YCore < 720:
        ghost2_YCore += 10    

    if my_sprite_collide(ghost1_YCore, ghost1_XCore, ghost2_YCore, ghost2_XCore):
        print("Столкновение!")

    main_win.blit(bg, (0, 0))
    main_win.blit(ghost1, (ghost1_XCore, ghost1_YCore))
    main_win.blit(ghost2, (ghost2_YCore, ghost2_XCore))

    display.update()
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    clock.tick(60)