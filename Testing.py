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

def imageUncenter(width, height, xCord, yCord):
    x = xCord + (.5 * width)
    y = yCord + (.5 * height)
    return (x,y)


def standingItemScale(backgroundImg, imagename, state, scale, xCord, yCord):
    if state == 1:
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        scaledPicture = imageScale(picture, scale)
        Cords = imageCenter(scaledPicture.get_width(), scaledPicture.get_height(), xCord, yCord)
        xCordShift = Cords[0]
        yCordShift = Cords[1]
        startDisplay(scaledPicture, xCordShift, yCordShift)
        return True

def standingItem(backgroundImg, imagename, xCord, yCord):
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
        xCordShift = Cords[0]
        yCordShift = Cords[1]
        startDisplay(picture, xCordShift, yCordShift)


def tempItemScale(backgroundImg, imagename, state, scale, xCord, yCord):
    if state == 1:
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        scaledPicture = imageScale(picture, scale)
        Cords = imageCenter(scaledPicture.get_width(), scaledPicture.get_height(), xCord, yCord)
        xCordShift = Cords[0]
        yCordShift = Cords[1]
        startDisplay(scaledPicture, xCordShift, yCordShift)
    else:
        startDisplay(backgroundImg, 0, 0)

def tempItem(backgroundImg, imagename, state, xCord, yCord):
    if state == 1:
        startDisplay(backgroundImg, 0, 0)
        picture = createImage(str(imagename))
        Cords = imageCenter(picture.get_width(), picture.get_height(), xCord, yCord)
        xCordShift = Cords[0]
        yCordShift = Cords[1]
        startDisplay(picture, xCordShift, yCordShift)
    else:
        startDisplay(backgroundImg, 0, 0)

def findAreaPos(image, xCord, yCord):
    width = image.get_width()
    height = image.get_height()
    xCord = xCord - (.5 * (width))
    yCord = yCord - (.5 * (height))
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

def standingCheckClose(openButton, closeButton, backgroundImg, imagename, buttonInputOpen, buttonInputClose, remainOpenInfo):
    xCord = mouseCord[0]
    yCord = mouseCord[1]
    remainOpen = remainOpenInfo[0]
    xStill = remainOpenInfo[1]
    yStill = remainOpenInfo[2]
    count = remainOpenInfo[3]
    if openButton == 'leftButton':
        rightButton = buttonInputClose
        leftButton = buttonInputOpen
        if leftButton == 0:
            leftButtonClicked = 0
            print("LeftClicked: " + str(leftButtonClicked))
            print("xCord2: " + str(xCord))
        else:
            leftButtonClicked = 1
            xStill = xCord
            yStill = yCord
            print("xCord3: " + str(xCord))

        if rightButton == 1:
            rightButtonClicked = 1
            rightButtonClicked = rightButtonClicked + 1
        else:
            rightButtonClicked = 0

        if leftButton == 1:
            leftButtonClicked = leftButtonClicked + 1

        if leftButtonClicked >= 1 and remainOpen == False and count == 0:
            #print("Counttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt" + str(count))
            count = count + 1
            #print("Counttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt" + str(count))
            #print("xStill: " + str(xStill))
            #print("MouseCord: " + str(mouseCord))
            #print("xStill: " + str(xStill))
            #print("yStill: " + str(yStill))
            #print("leftButtonClicked: " + str(leftButtonClicked))
            #print("rightButtonClicked: " + str(rightButtonClicked))
            standingItem(backgroundImg, str(imagename), xStill, yStill)
            #print("TopLeft: " + str(findAreaPos(createImage(str(imagename)), xStill, yStill)[0]))
            #print("BottomRight: " + str(findAreaPos(createImage(str(imagename)), xStill, yStill)[3]))
            remainOpen = True
            if mouseCord[0] >= int(findAreaPos(createImage(str(imagename)), xStill, yStill)[0][0]) and mouseCord[0] <= int(findAreaPos(createImage(str(imagename)), xStill, yStill)[3][0]) and mouseCord[1] >= int(findAreaPos(createImage(imagename), xStill, yStill)[0][1]) and mouseCord[1] <= int(findAreaPos(createImage(imagename), xStill, yStill)[3][1]) and rightButtonClicked >= 1:
                rightButtonClicked = 0
                startDisplay(backgroundImg, 0, 0)
                remainOpen = False
            else:
                leftButtonClicked = 0

        if remainOpen == True:
            #print("xStill: " + str(xStill))
            #("MouseCord: " + str(mouseCord))
            #print("xStill: " + str(xStill))
            #print("yStill: " + str(yStill))
            #print("leftButtonClicked: " + str(leftButtonClicked))
            #print("rightButtonClicked: " + str(rightButtonClicked))
            standingItem(backgroundImg, str(imagename), xStill, yStill)
            #print("TopLeft: " + str(findAreaPos(createImage(str(imagename)), xStill, yStill)[0]))
            #print("BottomRight: " + str(findAreaPos(createImage(str(imagename)), xStill, yStill)[3]))
            #print("RemainOpen: " + str(remainOpen))
            remainOpen = True
            if mouseCord[0] >= int(findAreaPos(createImage(str(imagename)), xStill, yStill)[0][0]) and mouseCord[0] <= int(findAreaPos(createImage(str(imagename)), xStill, yStill)[3][0]) and mouseCord[1] >= int(findAreaPos(createImage(imagename), xStill, yStill)[0][1]) and mouseCord[1] <= int(findAreaPos(createImage(imagename), xStill, yStill)[3][1]) and rightButtonClicked == 1:
                startDisplay(backgroundImg, 0, 0)
                count = count + 1
                xStill = 0
                yStill = 0
                remainOpen = False
                rightButtonClicked = 0
                leftButtonClicked = 0
                print("Micheallllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
            else:
                print("Simonssssssssssssssssssssssssssssss")
                print("mouseCord:" + str(mouseCord))
                print("TopLeft: " + str((findAreaPos(createImage(str(imagename)), xStill, yStill)[0])))
                print("TopRight: " + str((findAreaPos(createImage(str(imagename)), xStill, yStill)[1])))
                print("BottomLeft: " + str((findAreaPos(createImage(str(imagename)), xStill, yStill)[2])))
                print("BottomRight: " + str((findAreaPos(createImage(imagename), xStill, yStill)[3])))
                leftButtonClicked = 0
            if count == 3:
                count = 0
                rightButtonClicked = 0
        print('count' + str(count))



    if openButton == 'rightButton':
        rightButton = buttonInputOpen
        leftButton = buttonInputClose
        if rightButton == 1:
            rightButtonClicked = 1

        if leftButton == 1:
            leftButtonClicked = 1

        if rightButtonClicked == 0:
            xStill = xCord
            yStill = yCord
        else:
            xCordStill = xStill
            yCordStill = yStill
            print("TopLeftx: " + str(int(findAreaPos(createImage(str(imagename)), xStill, yStill)[0][0])))
            print("BottomRightx:" + str(int(findAreaPos(createImage(str(imagename)), xStill, yStill)[3][0])))
            standingItem(backgroundImg, str(imagename), xCordStill, yCordStill)
            if mouseCord[0] >= int(findAreaPos(createImage(str(imagename)), xStill, yStill)[0][0]) and mouseCord[0] <= int(findAreaPos(createImage(str(imagename)), xStill, yStill)[3][0]) and mouseCord[1] >= int(findAreaPos(createImage('SearchBox.jpg'), xStill, yStill)[0][1]) and mouseCord[1] <= int(findAreaPos(createImage('SearchBox.jpg'), xStill, yStill)[3][1]) and leftButtonClicked == 1:
                rightButtonClicked = 0
                leftButtonClicked = 0
            else:
                leftButtonClicked = 0
                return True
    return (remainOpen,xStill,yStill,count)


x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
move_speed = 0
gameDisplay.fill(white)
startDisplay(backgroundImg, 0, 0)
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
        #LeftButton
        scale = .25
        mouseButtons = checkButtons()
        leftButton = mouseButtons[0]
        middleButton = mouseButtons[1]
        rightButton = mouseButtons[2]
        #tempItemScale(backgroundImg, 'DogeCoin.png', leftButton, .125, xCord, yCord)
        standingItem(backgroundImg, 'SearchBox.jpg', xCord, yCord)
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