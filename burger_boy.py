# Logan's Project

import pygame
import time
import sys
from pygame.locals import *
import random

pygame.init()
height = 20
fatness = 20
fattallness = 20
poop = 0
pointcounter = 0
x = random.randint(1, 10)
level = 1
start = 1
life = 1000
bulletmove = 1
bullet_speed = 17

# burger_king = pygame.Rect

bullet1 = pygame.Rect(1, 660, 15, 15)
bullet2 = pygame.Rect(1, 680, 15, 15)
bullet3 = pygame.Rect(1, 700, 15, 15)
bullet4 = pygame.Rect(1, 720, 15, 15)
bullet5 = pygame.Rect(1, 740, 15, 15)
bullet6 = pygame.Rect(1, 760, 15, 15)
bullet7 = pygame.Rect(1, 780, 15, 15)
bullet8 = pygame.Rect(1, 800, 15, 15)
bullet9 = pygame.Rect(1, 820, 15, 15)
bullet10 = pygame.Rect(1, 840, 15, 15)

sideline_left = pygame.Rect(0, 0, 1, 920)
sideline_right = pygame.Rect(1279, 0, 1, 920)

sideline = [sideline_left, sideline_right]

bullet = [bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, bullet8, bullet9, bullet10]

screen = pygame.display.set_mode((1280, 920))
screen.fill((236, 136, 21))
pygame.display.set_caption('Burger Boy by Logan Gier')

main_clock = pygame.time.Clock()
player = pygame.Rect(640, 900, fatness, 20)
player_speed = 10

point = 0

wall11 = pygame.Rect(0, 490, 630, 15)
wall12 = pygame.Rect(650, 490, 640, 15)
wall13 = pygame.Rect(10, 440, 1260, 15)
wall14 = pygame.Rect(0, 390, 1280, 15)
wall15 = pygame.Rect(10, 340, 1270, 15)

walll21 = pygame.Rect(0, 455, 1280, 10)
walll22 = pygame.Rect()

walll = [walll21]

bathroom = pygame.Rect(1260, 900, 20, 20)

font = pygame.font.SysFont(None, 36)


def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (255, 0, 0,))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)


bouncepad = pygame.Rect(630, 435, 20, 5)
bouncepad_two = pygame.Rect(630, 0, 20, 5)
wall = [wall11, wall12, wall13, wall14, wall15]

burger_patty = pygame.Rect(1040, 45, 40, 20)
cheese = pygame.Rect(1040, 35, 40, 10)
top_bun = pygame.Rect(1040, 25, 40, 10)
bottom_bun = pygame.Rect(1040, 65, 40, 10)
counter = 12
burger = [burger_patty, cheese, top_bun, bottom_bun]
move_left = False
move_right = False
move_up = False
move_down = False
fatcount = 0
for _ in range(0, 2):
    rny = random.randint(0, 880)
    rnx = random.randint(0, 1230)
    burger_patty = pygame.Rect(rnx, rny, 40, 20)
    cheese = pygame.Rect(rnx, rny - 10, 40, 10)
    top_bun = pygame.Rect(rnx, rny - 20, 40, 10)
    bottom_bun = pygame.Rect(rnx, rny + 20, 40, 10)
    burger.append(burger_patty)
    burger.append(cheese)
    burger.append(top_bun)
    burger.append(bottom_bun)

while True:
    if level == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    move_right = False
                    move_up = False
                    move_down = False
                    move_left = True
                if event.key == K_d:
                    move_left = False
                    move_up = False
                    move_down = False
                    move_right = True
                if event.key == K_w:
                    move_left = False
                    move_right = False
                    move_down = False
                    move_up = True
                if event.key == K_s:
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = True
            if event.type == KEYUP:
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False
                if event.key == K_w:
                    move_up = False
                if event.key == K_s:
                    move_down = False
                if event.key == K_r:
                    height = 20
                    fatness = 20
                    fattallness = 20
                    poop = 0
                    pointcounter = 0
                    player_speed = 10
                    point = 0
                    player.x = 640
                    player.y = 900
                    level = 1

        main_clock.tick(30)

        if move_left and player.left > 0:
            player.x -= player_speed
        if move_right and player.right < 1280:
            player.x += player_speed
        if move_up and player.y > 0:
            player.y -= player_speed
        if move_down and player.y < 920:
            player.y += player_speed

        screen.fill((236, 136, 21))

        for walls in wall:
            pygame.draw.rect(screen, (0, 0, 0), walls)
            if player.colliderect(walls):
                if move_down:
                    player.y -= player_speed
                elif move_up:
                    player.y += player_speed
                elif move_left:
                    player.x += player_speed
                elif move_right:
                    player.x -= player_speed

        pygame.draw.rect(screen, (0, 0, 255), bouncepad_two)
        if player.colliderect(bouncepad_two):
            if move_down:
                player.y -= player_speed
            elif move_up:
                player.y += 900
            elif move_left:
                player.x += player_speed
            elif move_right:
                player.x -= player_speed
        pygame.draw.rect(screen, (255, 0, 0), bouncepad)
        if player.colliderect(bouncepad):
            if move_down:
                player.y -= 60
            elif move_up:
                player.y += player_speed
            elif move_left:
                player.x += player_speed
            elif move_right:
                player.x -= player_speed
        player = pygame.Rect(player.x, player.y, fatness, fattallness)
        pygame.draw.rect(screen, (255, 211, 155), player)
        if counter < 400:
            for x in range(0, 2):
                rny = random.randint(0, 880)
                rnx = random.randint(0, 1230)
                burger_patty = pygame.Rect(rnx, rny, 40, 20)
                cheese = pygame.Rect(rnx, rny - 10, 40, 10)
                top_bun = pygame.Rect(rnx, rny - 20, 40, 10)
                bottom_bun = pygame.Rect(rnx, rny + 20, 40, 10)
                burger.append(burger_patty)
                burger.append(cheese)
                burger.append(top_bun)
                burger.append(bottom_bun)
                counter += 4
        # slims when not moving
        if (not move_left) and (not move_up) and (not move_right) and (not move_down) and fatness >= 0:
            fatcount += 1
            if fatcount == 10:
                fatness -= 2
                fattallness -= 1
                fatcount = 0

        else:
            fatcount = 0

        for burgers in burger:
            if player.colliderect(burgers):
                burger.remove(burgers)

                fatness += 1
                fattallness = height + fatness / 2
                # if fattallness >=20:
                # fattallness = 30

                point += 1
                counter -= 1
        pygame.draw.rect(screen, (255, 255, 255), bathroom)
        if player.colliderect(bathroom):
            if move_down:
                player.y -= player_speed
                fatness -= 10
                fattallness -= 5
                poop += 1
                if poop > 10:
                    point -= 4
            elif move_up:
                player.y += player_speed
            elif move_left:
                player.x += player_speed
            elif move_right:
                player.x -= player_speed
                fatness -= 8
                fattallness -= 4
                poop += 1
                if poop > 10:
                    point -= 4

        count = 0
        for burgers in burger:
            if count == 0:
                pygame.draw.rect(screen, (92, 51, 23), burgers)
            if count == 1:
                pygame.draw.rect(screen, (255, 215, 0), burgers)
            if count == 2:
                pygame.draw.rect(screen, (255, 193, 37), burgers)
            if count == 3:
                pygame.draw.rect(screen, (255, 193, 37), burgers)
            count += 1
            if count == 4:
                count = 0
        if fatness <= 0:
            pointcounter += 1
            if pointcounter == 5:
                point -= 5
                pointcounter = 0
        if point < 0:
            screen.fill((255, 100, 0))
            draw_text('5000 years ago man was challenged with the idea to eat 250 burgers in under 10 minutes.', font,
                      screen, 5, 120)
            draw_text(
                'Your great great grandfather was the 18th to reach 200 burgers. By the time of his death everyone remembered',
                font, screen, 5, 140)
            draw_text(
                'him \'Alexander the Great\'. After his record of 214 burgers everyone was motivated to reach the big 250,',
                font, screen, 5, 160)
            draw_text('but none were great enough. Then one day his daughter, Alice the Great, was able to eat', font,
                      screen, 5, 180)
            draw_text(
                '219 burgers in under 10 minutes. After Alice, there were the brothers, George and Bob the Great,',
                font, screen, 5, 200)
            draw_text(
                'who were the new up and coming eaters. Competing, they were able to shatter their mother\'s record and ate',
                font, screen, 5, 220)
            draw_text(
                '233 burgers each in 10 minutes. Finally the day came and George passed away, after this Bob was sent into',
                font, screen, 5, 240)
            draw_text(
                'Burgerland which forced him to keep eating until he reached 1000 pounds. Bob was reincarnated 3 times',
                font, screen, 5, 260)
            draw_text(
                'before he was able to reach 1000 pounds, but the second he arrived back on Earth he was sent into a coma.',
                font, screen, 5, 280)
            draw_text(
                'While Bob was in a coma, George was reincarnated into a man named Thomas the Train, but he craved burgers,',
                font, screen, 5, 300)
            draw_text(
                'so much that a curse was put onto his family. The curse was that if he didn\'t eat burgers within a certain',
                font, screen, 5, 320)
            draw_text(
                'amount of time he would lose size and weight. Thomas (George) kept eating burgers until he died,',
                font, screen, 5, 340)
            draw_text(
                'but in 10 minutes he still only could eat 243 burgers. His son, your father, was always the fatest kid',
                font, screen, 5, 360)
            draw_text(
                'growing up because of his weird desease that the doctors were calling... \'NoBurgerPhobiaOfEpicProportions\'',
                font, screen, 5, 380)
            draw_text(
                'he had to constantly eat burgers, but one day he couldn\'t take it anymore and ate cookies instead.',
                font, screen, 5, 400)
            draw_text(
                'It was a painful death, but the Burger Gods were not pleased with his change of heart and chose for his legacy',
                font, screen, 5, 420)
            draw_text(
                'to come to Burgerland.Just as Bob did, you have to reach the goal that your predecessors couldn\'t reach,',
                font, screen, 5, 440)
            draw_text(
                '250 burgers in under 10 minutes.This is Your Job, the Burger Gods decided that if you were able to eat',
                font, screen, 5, 460)
            draw_text(
                '250 burgers in under 10 minutes you could leave. And they have told your previous incarnates that you could',
                font, screen, 5, 480)
            draw_text(
                'also break the curse of the need for burger meat. You could break the record and you could be remembered as',
                font, screen, 5, 500)
            draw_text(
                'the Greatest Burger Eater ever. Some day you will do it, but today is not that day. Goodbye... You Lose!',
                font, screen, 5, 520)
        ###############################
        if point >= 100 and level == 1:
            screen.fill((236, 136, 21))
            draw_text('You Win!', font, screen, 500, 400)
            draw_text('After Reaching 1000 pounds you obtained a TV Show', font, screen, 350, 500)
            draw_text('\'My 1000 Pound Life\' Was Hysterical as people watched you roll around eating burgers', font,
                      screen, 200, 550)
            pygame.display.update()
            time.sleep(3)
            level += 1
            point = 0
            start = 0

        player_speed = 10 - point/100

        draw_text('Points = %s Pounds' % point, font, screen, 5, 5)
        draw_text('Speed = %s rolls per second' % player_speed, font, screen, 5, 85)

        pygame.display.update()

    if level == 2:
        if start == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((236, 136, 21))
            pygame.display.update()
            draw_text('You Thought You Won', font, screen, 500, 400)
            draw_text('But There is Always More', font, screen, 450, 450)
            pygame.display.update()
            time.sleep(2)
            draw_text('Welcome! I am the king...', font, screen, 450, 500)
            pygame.display.update()
            time.sleep(2)
            draw_text('The Burger King', font, screen, 450, 550)
            pygame.display.update()
            time.sleep(2)
            screen.fill((236, 136, 21))
            pygame.display.update()
            time.sleep(1)
            # draw_text ('Coming Soon...', font, screen, 500, 400)
            # pygame.display.update()
            # time.sleep(2)
            start += 1

        elif start == 1:
            screen.fill((255, 255, 255))
            player = pygame.Rect(640, 900, 10, 20)
            pygame.display.update()
            start += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    move_right = False
                    move_up = False
                    move_down = False
                    move_left = True
                if event.key == K_d:
                    move_left = False
                    move_up = False
                    move_down = False
                    move_right = True
                if event.key == K_w:
                    move_left = False
                    move_right = False
                    move_down = False
                    move_up = True
                if event.key == K_s:
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = True
            if event.type == KEYUP:
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False
                if event.key == K_w:
                    move_up = False
                if event.key == K_s:
                    move_down = False
        main_clock.tick(30)

        screen.fill((0, 0, 0))

        player_speed = 4
        if move_left and player.left > 0:
            player.x -= player_speed
        if move_right and player.right < 1280:
            player.x += player_speed
        if move_up and player.y > 0:
            player.y -= player_speed
        if move_down and player.y < 920:
            player.y += player_speed

        for wallls in walll:
            pygame.draw.rect(screen, (255, 0, 0), wallls)
            if player.colliderect(wallls):
                if move_down:
                    player.y -= player_speed
                elif move_up:
                    player.y += player_speed
                elif move_left:
                    player.x += player_speed
                elif move_right:
                    player.x -= player_speed

        for bullets in bullet:
            pygame.draw.rect(screen, (192, 192, 192), bullets)

            if bulletmove == 2 and bullets.left > 0:
                bullets.x -= bullet_speed
                if not bullets.left > 0:
                    bulletmove = 1
            if bulletmove == 1 and bullets.right < 1280:
                bullets.x += bullet_speed
                if not bullets.right < 1280:
                    bulletmove = 2
            if player.colliderect(bullets):
                life -= 5
                player.x = 640
                player.y = 900


        draw_text('LifeForce = %s' % life, font, screen, 5, 5)

        pygame.draw.rect(screen, (255, 211, 155), player)
        pygame.display.update()
