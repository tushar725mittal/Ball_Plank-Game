import math
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
music = pygame.mixer.Sound("Assets/back_music.mp3")
music.play(-1)

ball1 = pygame.image.load("Assets/ball1.png")
pygame.display.set_caption("Balancing The Balls")
pygame.display.set_icon(ball1)

Example1 = pygame.image.load("Assets/Example1.png")
Example2 = pygame.image.load("Assets/Example2.png")
StartImg = pygame.image.load("Assets/StartImg.png")
screen.blit(Example1,(0,0))
pygame.display.update()
pygame.time.delay(2000)
screen.blit(Example2,(0,0))
pygame.display.update()
pygame.time.delay(2000)
screen.blit(StartImg,(0,0))
pygame.display.update()
pygame.time.delay(2000)

bar = pygame.image.load("Assets/gamebar.png")
def bar_image(x):
    screen.blit(bar,(x,bar_y))
bar_x = random.randint(0,736)
bar_y = 500
bar_x_change = 0
speed_bar = 0.3
speedchange_bar = True

def ball1_image(x,y):
    screen.blit(ball1,(x,y))
ball1_x = random.randint(0,736)
ball1_y = random.randint(0,100)
ball1_x_change = 0
ball1_y_change = 0
ball1_move = True

ball2 = pygame.image.load("Assets/ball2.png")
def ball2_image(x,y):
    screen.blit(ball2,(x,y))
ball2_x = random.randint(0,736)
ball2_y = random.randint(0,100)
ball2_x_change = 0
ball2_y_change = 0
ball2_move = True

speed = 0.2
speedchange = True

score = 0
score_change1 = True
score_change2 = True
font = pygame.font.Font(('freesansbold.ttf'),32)
def show_score():
    result = font.render("Score: "+ str(score), True, (255,255,255))
    screen.blit(result,(10,10))

gameover = pygame.image.load("Assets/GameOver.png")
def GameOver():
    screen.blit(gameover,(0,0))

Tick = pygame.mixer.Sound("Assets/Tick.mp3")
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if ball1_move:
                ball1_y_change = speed
                ball1_move = False
            if event.key == pygame.K_RIGHT:
                bar_x_change = speed_bar
            if event.key == pygame.K_LEFT:
                bar_x_change = -speed_bar
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                bar_x_change = 0

    if ball1_y > 450 and ball1_y < 500 and math.sqrt(math.pow(ball1_x - bar_x,2)) < 50 and score_change1 == True:
        if ball2_move:
            ball2_y_change = speed
            ball2_move = False
        Tick.play()
        ball1_x_change = (ball1_x - bar_x)*0.01
        ball1_y_change = -speed
        score+=1
        score_change1 = False
        speedchange = True
        speedchange_bar = True
    
    if ball1_x < 0 or ball1_x > 736:
        ball1_x_change *= -1
        score_change1 = True
    if ball1_y < 0:
        ball1_y_change *= -1
        score_change1 = True

    if ball2_y > 450 and  ball2_y < 500 and math.sqrt(math.pow(ball2_x - bar_x,2)) < 50 and score_change2 == True:
        Tick.play()
        ball2_x_change = (ball2_x - bar_x)*0.01
        ball2_y_change = -speed
        score+=1
        score_change2 = False
        speedchange = True
        speedchange_bar = True
    
    if ball2_x < 0 or ball2_x > 736:
        ball2_x_change *= -1
        score_change2 = True
    if ball2_y < 0:
        ball2_y_change *= -1
        score_change2 = True


    screen.fill((100,0,100))

    bar_x += bar_x_change
    if bar_x < 0:
        bar_x = 0
        bar_x_change = 0
    elif bar_x > 736:
        bar_x = 736
        bar_x_change = 0
    bar_image(bar_x)

    ball1_x += ball1_x_change
    ball1_y += ball1_y_change
    ball1_image(ball1_x,ball1_y)
    ball2_x += ball2_x_change
    ball2_y += ball2_y_change
    ball2_image(ball2_x,ball2_y)
    show_score()
    if score%10 == 0 and speed <= 0.7 and score > 0:
            if speedchange:
                speed += 0.1
                speedchange = False
    if score%20 == 0 and speed_bar <= 0.9 and score > 0:
            if speedchange_bar:
                speed_bar += 0.1
                speedchange_bar = False  
    if ball1_y > 600 or ball2_y > 600:
        ball1_y = 1000
        ball2_y = 1000
        bar_y = 1000
        bar_x_change = 0
        ball1_x_change = 0
        ball2_x_change = 0
        ball1_y_change = 0
        ball2_y_change = 0
        GameOver()
        for event in pygame.event.get():
            x,y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x >= 299 and y <= 374 and y>= 320 and x <= 503:
                    Tick.play()
                    bar_x = random.randint(0,736)
                    bar_y = 500
                    bar_x_change = 0
                    ball1_x = random.randint(0,736)
                    ball1_y = random.randint(0,100)
                    ball1_move = True
                    ball2_x = random.randint(0,736)
                    ball2_y = random.randint(0,100)
                    ball2_move = True
                    speed = 0.2
                    speedchange = True
                    speedchange_bar = True
                    speed_bar = 0.3
                    score = 0
            if event.type == pygame.QUIT:
                running = False                    
       
    pygame.display.update()