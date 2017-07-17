import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,460))
screen.fill((255,165,0))
pygame.display.set_caption('Logan\'s Lame Lazy Learning Game of Land, Lines and Luck')

font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()
player = pygame.Rect(300, 400, 60, 10)
player_speed = 6

move_left = False
move_right = False

x_position = 380
y_position = 395
last_x = x_position
last_y = y_position
ball_can_move = False
speed = [5, -5]

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0,))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display,text_rect)

all_bubbles = []
bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 70
bubble_spacing = 60

def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position

    for rows in range(0, 3):
        for columns in range(0, 10):
            bubble = pygame.draw.circle((screen), (255, 255, 255), (bubble_x, bubble_y),bubble_radius, bubble_edge)
            bubble_x += bubble_spacing
            all_bubbles.append(bubble)
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position

create_bubbles()

def draw_bubbles():
    for bubble in all_bubbles:
        bubble = pygame.draw.circle((screen), (255,255,255), (bubble.x, bubble.y), bubble_radius, bubble_edge)
        
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_left = False
                move_right = True
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if event.key == K_SPACE:
                ball_can_move = True
    main_clock.tick(50)
                
    if move_left and player.left > 0:
        player.x -= player_speed
    if move_right and player.right < 640:
        player.x += player_speed
        

    if ball_can_move:
        last_x = x_position
        last_y = y_position

        x_position += speed[0]
        y_position += speed[1]
        if ball.y <= 0:
            y_position = 15
            speed[1] = -speed[1]
        #if ball.y >= 460:
            #y_position = 445
            #speed[1] = -speed[1]
        if ball.x <= 0:
            x_position = 15
            speed[0] = -speed[0]
        if ball.x >= 640:
            x_position = 625
            speed[0] = -speed[0]
        if ball.colliderect(player):
            y_position -= 15
            speed[1] = -speed[1]

        move_direction = ((x_position - last_x), (y_position - last_y))

        for bubble in all_bubbles:
            if ball.colliderect(bubble):
                if move_direction[1] > 0:
                    speed[1] = -speed[1]
                    y_position -= 10
                elif move_direction[1] < 0:
                    speed[1] = -speed[1]
                    y_position += 10
                all_bubbles.remove(bubble)
                break
    else:
        x_position = player.x + 30


    screen.fill((255,165,0))
    draw_text('Text', font, screen, 5,5)
    draw_bubbles()
    ball = pygame.draw.circle(screen, (0, 0, 0,), (x_position, y_position), 5,0)
    pygame.draw.rect(screen, (225, 0, 115), player)
    pygame.display.update()
