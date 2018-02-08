import pygame
import cmath
pygame.init()

display_width = 800
display_height = 600
display_width = int(input("Please pick a display width: "))
display_height = int(input("Please pick a display height: "))
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DogeOS')
iconImage = pygame.image.load('DogeCoin.png').convert_alpha()
pygame.display.set_icon(iconImage)
black = (0, 0, 0)
white = (255, 255, 255)
mouseCord = (0,0)
clock = pygame.time.Clock()
closed = False
backgroundImg = pygame.image.load('Doge_Cartoon.png').convert_alpha()
backgroundImg = pygame.transform.scale(backgroundImg,(display_width, display_height))

def createImage(imagename):
    image = pygame.image.load(imagename).convert_alpha()
    return image

def imageScale(image,scaleFactor):
    image2 = pygame.transform.scale(image, (((int(display_width * scaleFactor)),(int(display_height * scaleFactor)))))
    return image2

def startDisplay(image,x, y):
    gameDisplay.blit(image, (x, y))

def imageCenter(width, height, xCord, yCord):
    x = xCord - (.5 * width)
    y = yCord - (.5 * height)
    return (x,y)


def standingItemScale(backgroundImg, imagename, state, scale, xCord, yCord):
    if state == 1:
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        scaledPicture = imageScale(picture, scale)
        Cords = imageCenter(scaledPicture.get_width(), scaledPicture.get_height(), xCord, yCord)
        xCord = Cords[0]
        yCord = Cords[1]
        startDisplay(scaledPicture, xCord, yCord)
        return True

def standingItem(backgroundImg, imagename, xCord, yCord):
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
        xCord = Cords[0]
        yCord = Cords[1]
        startDisplay(picture, xCord, yCord)


def tempItemScale(backgroundImg, imagename, state, scale, xCord, yCord):
    if state == 1:
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        scaledPicture = imageScale(picture, scale)
        Cords = imageCenter(scaledPicture.get_width(), scaledPicture.get_height(), xCord, yCord)
        xCord = Cords[0]
        yCord = Cords[1]
        startDisplay(scaledPicture, xCord, yCord)
    else:
        startDisplay(backgroundImg, 0, 0)

def tempItem(backgroundImg, imagename, state, xCord, yCord):
    if state == 1:
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
        xCord = Cords[0]
        yCord = Cords[1]
        startDisplay(picture, xCord, yCord)
    else:
        startDisplay(backgroundImg, 0, 0)

def findAreaPos(image):
    print("A")
    #Finds area in which the bar can be left clicked and removed.


x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
move_speed = 0
gameDisplay.fill(white)
startDisplay(backgroundImg, 0, 0)
rightButtonClicked = 0
while not closed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ############################
        #if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION or pygame.mouse.get_rel() == (0, 0):


        mouseCord = pygame.mouse.get_pos()
        print(mouseCord)
        xCord = mouseCord[0]
        yCord = mouseCord[1]
        mouseButtons = pygame.mouse.get_pressed()
        print(mouseButtons)
        leftButton = mouseButtons[0]
        middleButton = mouseButtons[1]
        rightButton = mouseButtons[2]
        print("Hello")
        #LeftButton
        scale = .25
        tempItemScale(backgroundImg, 'DogeCoin.png', leftButton, .125, xCord, yCord)
        if rightButtonClicked == 0:
            xCord = xCord
            yCord = yCord
        else:
            xCord = xStill
            yCord = yStill
        if rightButton == 1:
            rightButtonClicked = 1
        if rightButtonClicked == 1:
            xStill = xCord
            yStill = yCord
            standingItem(backgroundImg, 'SearchBox.jpg', xCord, yCord)
        if xCord >= display_width - 1 or xCord == 0 or yCord >= display_height - 1 or yCord == 0:
            rightButtonClicked = 0

        print(mouseCord)
        #MiddleButton
        if middleButton == 1:
            print("Farming")
        #RightButton
        if rightButton == 1:
            print("CinderappleCow")



        ######################
    ##
    x += x_change
    ##


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()