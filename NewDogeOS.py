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
leftButtonClicked = 0
rightButtonClicked = 0
remainOpen = False
count = 0
xStill = 0
yStill = 0
close = 0
standCount = -1
xImageCord = -1
yImageCord = -1
index = -1
Priorities = []
priorityCount = 0
markerOpen = 1
backgroundClick= pygame.event.Event(pygame.USEREVENT)
searchBoxClick = pygame.event.Event(pygame.USEREVENT)
def createImage(imagename):
    image = pygame.image.load(imagename).convert_alpha()
    return image

def imageScale(image, widthScale, heightScale):
    resScaleW = display_width * widthScale
    resScaleH = display_height * heightScale
    widthSF = resScaleW / image.get_width()
    heightSF = resScaleH / image.get_height()
    print("Width: " + str(widthSF))
    print("Height: " + str(heightSF))
    image2 = pygame.transform.scale(image, (((int(image.get_width() * widthSF),(int(image.get_height() * heightSF))))))
    return image2



def startDisplay(image,x, y):
    gameDisplay.blit(image, (x, y))

def imageCenter(width, height, xCord, yCord):
    x = xCord - (.5 * width)
    y = yCord - (.5 * height)
    return (x,y)

def imageUncenter(width, height, xCord, yCord):
    x = xCord + (.5 * width)
    y = yCord + (.5 * height)
    return (x,y)


def standingItemScale(imagename, widthScale, heightScale, xCord, yCord):
        #
        picture = createImage(str(imagename))
        scaledPicture = imageScale(picture, widthScale, heightScale)
        startDisplay(scaledPicture, xCord, yCord)

# Cords = imageCenter(, picture.get_height(), xCord, yCord)
 #       xCordShift = Cords[0]
 #       yCordShift = Cords[1]
def standingItem(backgroundImg, imagename, xCord, yCord):
    if xCord == -1 and yCord == -1:
        return None
    else:
        #
        picture = createImage(str(imagename))
        startDisplay(picture, xCord, yCord)


def searchBoxCreate(imagename, xCord, yCord, close, count):
        if close == 1:
            startDisplay(backgroundImg, 0, 0)
            if True:
                standingItemScale("TestWindow.png", .75, .45, 0, 0)
            return ("Reset")
        if checkButtons()[0] == 1 and count == 0:
            if close == 0:
                startDisplay(backgroundImg, 0, 0)
                if True:
                    standingItemScale("TestWindow.png", .75, .45, 0, 0)
                picture = createImage(str(imagename))
                Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
                xCordShift = Cords[0]
                yCordShift = Cords[1]
                startDisplay(picture, xCordShift, yCordShift)
                return (xCordShift, yCordShift)
        else:
            return (-1, -1)

startDisplay(backgroundImg, 0, 0)
def mouseFollowItem(imagename, xCord, yCord):
    #
    picture = createImage(str(imagename))
    Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
    xCordShift = Cords[0]
    yCordShift = Cords[1]
    startDisplay(picture, xCordShift, yCordShift)

def mouseFollowItemScale(imagename, scale, xCord, yCord):
    #
    picture = createImage(str(imagename))
    scaledPicture = imageScale(picture, scale)
    Cords = imageCenter(scaledPicture.get_width(), scaledPicture.get_height(), xCord, yCord)
    xCordShift = Cords[0]
    yCordShift = Cords[1]
    startDisplay(scaledPicture, xCordShift, yCordShift)


def tempItemScale(imagename, state, scale, xCord, yCord):
    if state == 1:
        #
        picture = createImage(str(imagename))
        scaledPicture = imageScale(picture, scale)
        Cords = imageCenter(scaledPicture.get_width(), scaledPicture.get_height(), xCord, yCord)
        xCordShift = Cords[0]
        yCordShift = Cords[1]
        startDisplay(scaledPicture, xCordShift, yCordShift)
    #else:
        #

def tempItem(imagename, state, xCord, yCord):
    if state == 1:
        #
        picture = createImage(str(imagename))
        Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
        xCordShift = Cords[0]
        yCordShift = Cords[1]
        startDisplay(picture, xCordShift, yCordShift)
    #else:
        #

def findAreaPos(image, xCord, yCord):
    width = image.get_width()
    height = image.get_height()
    topLeft = (xCord, yCord)
    topRight = (xCord + width, yCord)
    bottomLeft = (xCord, yCord + height)
    bottomRight = (xCord + width, yCord + height)
    return [topLeft, topRight, bottomLeft, bottomRight]


    #Finds area in which the bar can be left clicked and removed.
def checkButtons():
    mouseButtons = pygame.mouse.get_pressed()
    leftButton = mouseButtons[0]
    middleButton = mouseButtons[1]
    rightButton = mouseButtons[2]
    return (leftButton, middleButton, rightButton)

def searchBoxCheckClose(imagename, xCord, yCord):
    if mouseCord[0] >= int(findAreaPos(createImage(str(imagename)), xCord, yCord)[0][0]) and mouseCord[0] <= int(findAreaPos(createImage(str(imagename)), xCord, yCord)[3][0]) and mouseCord[1] >= int(findAreaPos(createImage(imagename), xCord, yCord)[0][1]) and mouseCord[1] <= int(findAreaPos(createImage(imagename), xCord, yCord)[3][1]) and checkButtons()[2] == 1 and xCord != -1 and yCord != -1:
        close = 1
        return close
    else:
        close = 0
        return close


x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
move_speed = 0
gameDisplay.fill(white)
startDisplay(backgroundImg, 0, 0)
rightButtonClicked = 0
while not closed:

    for event in pygame.event.get():
        #startDisplay(backgroundImg, 0, 0)
        print(event)
        if event.type == pygame.QUIT:
            closed = True

        mouseCord = pygame.mouse.get_pos()
        xCord = mouseCord[0]
        yCord = mouseCord[1]
        # LeftButton
        scale = .25
        mouseButtons = checkButtons()
        leftButton = mouseButtons[0]
        middleButton = mouseButtons[1]
        rightButton = mouseButtons[2]
        #tempItemScale(backgroundImg, 'DogeCoin.png', leftButton, .125, xCord, yCord)
        #mouseFollowItemScale(backgroundImg, 'DogeCoin.png', .125, xCord, yCord)

        with open("Priorities.txt") as file:
            Priorities = file.read().split()

        print(standCount)
        if leftButton == 1:
            if standCount == -1:
                standCount = 0
            standCount = standCount + 1
        if standCount == 1:
            xStillWindow = xCord
            yStillWindow = yCord
        elif standCount > 1:
            xStillWindow = xStillWindow
            yStillWindow = yStillWindow
        elif standCount == -1:
            xStillWindow = -1
            yStillWindow = -1

        if True:
           standingItemScale("TestWindow.png", .75, .45, 0, 0)

        #Open Up a Search Box with left button, close with right#############################
        #pygame.event.post(backgroundClick)

        if True: #event == backgroundClick:

            imageCords = searchBoxCreate("SearchBox.jpg", xCord, yCord, close, count)
            if imageCords == "Reset":
                close = 0
                count = 0
                xImageCord = -1
                yImageCord = -1
                imageCords = (xImageCord, yImageCord)
            if imageCords != (-1, -1):
                if count == 0:
                    xImageCord = imageCords[0]
                    yImageCord = imageCords[1]
                else:
                    xImageCord = xImageCord
                    yImageCord = yImageCord
                    startDisplay(backgroundImg, 0, 0)
                count = count + 1
            if mouseButtons[0] == 1 and mouseCord[0] >= int(findAreaPos(createImage(str('SearchBox.jpg')), xImageCord, yImageCord)[0][0]) and mouseCord[0] <= int(findAreaPos(createImage(str('SearchBox.jpg')), xImageCord, yImageCord)[3][0]) and mouseCord[1] >= int(findAreaPos(createImage('SearchBox.jpg'), xImageCord, yImageCord)[0][1]) and mouseCord[1] <= int(findAreaPos(createImage('SearchBox.jpg'), xImageCord, yImageCord)[3][1]) and xImageCord != -1 and yImageCord != -1:
                count = 0
                mouseFollowItem('SearchBox.jpg', mouseCord[0], mouseCord[1])
            close = searchBoxCheckClose("SearchBox.jpg", xImageCord, yImageCord)




            #####################################################################################


        # MiddleButton
        if middleButton == 1:
            print("Farming")
        # RightButton
        if rightButton == 1:
            print("CinderappleCow")
        ##############################################################################
        #tempItemScale(backgroundImg, 'DogeCoin.png', leftButton, .125, xCord, yCord)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
