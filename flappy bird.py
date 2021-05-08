import pygame
from threading import Timer
import random
import time

#Wdith and Height
from PIL import ImageOps

width = 360
height = 600

#x and y
x = 100
y = 100

xFloor = 0
xFloor2 = 500

xPipe = 500
yPipe = 350
yPipe2 = yPipe - 700

randomNum = 0
randomChoice = 0
#Speed
v = 9
m = 1

#Jump
isjump = False
jumpCount = 10

collision = False

points = 0

pygame.init()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumping Game 2")

run = True

#Keeps the window running
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Detects where the player clicks
        if event.type == pygame.MOUSEBUTTONUP:
            cx, cy = pygame.mouse.get_pos()
            print(cx, cy)

    keys = pygame.key.get_pressed()
        #Extras
    if isjump == False:
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            # make isjump equal to True
            isjump = True
    if isjump:
        if collision == False:
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
            F = (1 / 2) * m * (v ** 2)
            # change in the y co-ordinate
            y -= F
            # decreasing velocity while going up and become negative while coming down
            v = v - 1
            # object reached its maximum height
            if v < 0:
                # negative sign is added to counter negative velocity
                m = -1
            # objected reaches its original state
            if v == -6:
                # making isjump equal to false
                isjump = False
                # setting original values to v and m
                v = 9
                m = 1

    #Generates Font
    font = pygame.font.SysFont("comicsans", 50)
    fontBig = pygame.font.SysFont("comicsans", 150)
    fontSmall = pygame.font.SysFont("comicsans", 26)

    #colors
    greenColor = 150, 200, 20
    blueColor = 67, 84, 255
    orangeColor = 255, 165, 0
    redColor = 250, 0, 0
    purpleColor = 172, 79, 198
    grayColor = 128, 128, 128

    # Fills the screen with black
    win.fill((0, 0, 0))

    #background image
    image = pygame.image.load('flappyBirdbackground.png')
    win.blit(image, (0, 0))

    #Draws the bird
    imageB = pygame.image.load('favpng_flappy-bird-flappy-eagle-video-games.png')
    imageB = pygame.transform.scale(imageB, (35, 35))
    win.blit(imageB, (x, y))

    #Draws the floor
    imageF = pygame.image.load('flappyBirdFloor.png')
    imageF = pygame.transform.scale(imageF, (500, 100))
    win.blit(imageF, (xFloor, 500))
    imageF2 = pygame.image.load('flappyBirdFloor.png')
    imageF2 = pygame.transform.scale(imageF2, (500, 100))
    win.blit(imageF2, (xFloor2, 500))
    if collision == False:
        xFloor -= 5
        xFloor2 -= 5
        if xFloor2 == 0:
            xFloor = 500
        if xFloor == 0:
            xFloor2 = 500

    #Draws the pipes
    imageP = pygame.image.load('toppng.com-mobile-flappy-bird-version-12-sprites-the-spritersthe-tubo-de-mario-bros-629x801.png')
    imageP = pygame.transform.scale(imageP, (115, 500))
    win.blit(imageP, (xPipe, yPipe))
    imagePV = pygame.image.load('toppng.com-mobile-flappy-bird-version-12-sprites-the-spritersthe-tubo-de-mario-bros-629x801.png')
    imagePV = pygame.transform.scale(imagePV, (115, 500))
    imagePV = pygame.transform.flip(imagePV, False, True)
    win.blit(imagePV, (xPipe, yPipe2))
    if collision == False:
        if xPipe < -120:
            points += 1
            xPipe = 500
            yPipe = 350
            randomChoice = random.randint(1,2)
            if randomChoice == 1:
                randomNum = random.randint(0, 100)
                yPipe = yPipe - randomNum
            if randomChoice == 2:
                randomNum = random.randint(0, 200)
                yPipe = yPipe + randomNum
            yPipe2 = yPipe - 700
            print(yPipe)
            print(yPipe2)
        xPipe -= 10

    #Collision detection
    if y >= yPipe or y <= yPipe2 + 485:
        if abs(x - xPipe - 85) <= 115:
            collision = True
    # Gravity
    grav = 20
    if y >= 470:
        grav = 0
        collision = True
    else:
        if collision == False:
            if isjump == False:
                y += grav
    if collision == True:
        LostLabel = font.render("Game Over", bool(1), (255, 255, 255))
        win.blit(LostLabel, (100, 100))
        pointsEnd = font.render(f"Total Points: {points}", bool(1), (255, 255, 255))
        win.blit(pointsEnd, (75, 150))
    pointsLabel = font.render(f"Points: {points}", bool(1), (255, 255, 255))
    win.blit(pointsLabel, (15, 15))
    pygame.display.update()
pygame.quit()