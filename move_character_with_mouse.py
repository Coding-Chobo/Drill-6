from pico2d import *
import os
import random
import math

os.chdir('c:/TUK/2nd Grade/2DGP/Professor/Labs/Lecture07_Linear_Movement')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)


TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def Set_arrow():
    global arrow_x, arrow_y
    arrow_x = random.randint(0, TUK_WIDTH)
    arrow_y = random.randint(0, TUK_HEIGHT)
    normalize()

def normalize():
    global normalVector_X, normalVector_Y
    dx = arrow_x - x
    dy = arrow_y - y
    distance = math.sqrt(dx ** 2 + dy ** 2) 

    if distance != 0:
        normalVector_X = dx / distance
        normalVector_Y = dy / distance
    else:
        normalVector_X, normalVector_Y = 0, 0

def Movement():
    global x, y
    step = 2 
    dx = arrow_x - x
    dy = arrow_y - y
    distance = math.sqrt(dx ** 2 + dy ** 2) 
    if distance > step:
        x += normalVector_X * step
        y += normalVector_Y * step
    else:
        x, y = arrow_x, arrow_y 
        Set_arrow() 

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2  
arrow_x, arrow_y = x, y  
normalVector_X, normalVector_Y = 0, 0 
frame = 0

hide_cursor()

Set_arrow()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2) 
    if normalVector_X >= 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)  
    else :
        character.clip_draw(frame * 100, 0, 100, 100, x, y)  
    
    hand.draw(arrow_x, arrow_y) 
    Movement()  
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
