#capitalistMining Created by Andrew Ely


'''

CHECKLIST
---------
- All businesses milestones
- All business upgrades 
- upgrade values
- cash per second
- idle cash gain between game sessions 
- save data 
- "Angel Investors" / resets

'''


import pygame, sys, math
import time as Time
from decimal import Decimal
from upgradeItems import *
from storeItems import *

#initialize Pygame 
pygame.init()
pygame.display.set_caption('capitalist')

#display variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (95, 180, 90)   
RED = pygame.Color('red')
GRAY = pygame.Color('grey')
DARKYELLOW = pygame.Color(129,106,8)
YELLOW = pygame.Color(156,139,13)
DISPLAYSURF = pygame.display.set_mode((720, 900))

#Sprites
logo = pygame.image.load('pngImages/Logo.png')
menu = pygame.image.load('pngImages/menu.png')
storeBoard = pygame.image.load('pngImages/storeBoard.png')
mainMenu = pygame.image.load('pngImages/mainMenu.png')
background = pygame.image.load('pngImages/background.png')
itemSillouete = pygame.image.load('pngImages/nextItemSillouete.png')
upgradeBoard = pygame.image.load('pngImages/upgradeBoard.png')
checkBox = pygame.image.load('pngImages/checkBox.png')

#fonts
font1 = pygame.font.SysFont('monaco', 24)
font2 = pygame.font.SysFont('monaco', 18)

#set windows icon (top left of window)
pygame.display.set_icon(logo)

#game variables
running = True
displayStore = True
profit = 4
menuRect = pygame.Rect(680, 860, 30, 30)
itemsIndex = 1
upgradesIndex = 1
buyModeQuantityList = ['x1','x25', 'x100', 'MAX']
buyModeQuantityIndex = 0
dragging = False
offset_x = 0
menuButtonOpacity = 0
buyModeButtonOpacity = 0 
upgradeWindow = pygame.Rect(100, 800, 500, 45)

#list of upgrade item lists 
upgradesItems = [upgradeItemsFull[0]] #Start off with first Item

#List of store Item Lists
storeItems = [storeItemsFull[0]] #start off with first item

#function to display the entire start screen
def startScreen():

    #Start screen drawing
    storeButton = pygame.Rect(205, 495, 300, 150)
    mineButton = pygame.Rect(205, 315, 300, 150) 

    storeButtonSurface = pygame.Surface((300,150))  
    storeButtonOpacity = 0
    mineButtonSurface = pygame.Surface((300,150))  
    mineButtonOpacity = 0
    
    displayMainMenu = True
    #start screen loop 
    while displayMainMenu:
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if storeButton.collidepoint(mouse_pos):
                storeButtonOpacity = 75
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    return "store"
            elif not storeButton.collidepoint(mouse_pos):
                storeButtonOpacity = 0

            if mineButton.collidepoint(mouse_pos):
                mineButtonOpacity = 75
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    return "mine"
            elif not mineButton.collidepoint(mouse_pos):
                mineButtonOpacity = 0

        #Draw to screen
        DISPLAYSURF.blit(background, (0,0))
        DISPLAYSURF.blit(logo, (275, 100))
        DISPLAYSURF.blit(menu, (125, 225))
        pygame.draw.rect(DISPLAYSURF, RED, storeButton, 2) 
        pygame.draw.rect(DISPLAYSURF, RED, mineButton, 2)

        storeButtonSurface.set_alpha(storeButtonOpacity)     
        storeButtonSurface.fill((255,255,255))     
        DISPLAYSURF.blit(storeButtonSurface, (205,495))

        mineButtonSurface.set_alpha(mineButtonOpacity)     
        mineButtonSurface.fill((255,255,255))     
        DISPLAYSURF.blit(mineButtonSurface, (205,315)) 

        pygame.display.flip()

#Function to draw Titles to store Screen
def drawNumber(number, x, y, font, pos):

    number = round(number, 2)
    if number >= 100000000000:
        number = '{:.2E}'.format(number)
    else:
        number = '{:,}'.format(number)
    surface = font.render('{0}'.format(number), True, BLACK)
    rect = surface.get_rect()
    if pos == "left":
        rect.midleft = (x, y)
    if pos == "right":
        rect.midright = (x, y)

    DISPLAYSURF.blit(surface, rect)

def drawTitle(title, x, y, font):

    titleSurface = font.render(title, True, BLACK)
    titleRect = titleSurface.get_rect()
    titleRect.midleft = (x, y)
    DISPLAYSURF.blit(titleSurface, titleRect)

#function for all store buttons
def storeButtons(item, row):
    
    #assign values of current store item
    name = item[0]
    cost = item[1]
    gain = item[2]
    amount = item[3]
    itemNumber = item[4]
    length = item[5]
    speed = item[6]
    active = item[7]
    managerStatus = item[8]
    managerCost = item[9]
    costMultilplier = item[10]
    gainMultiplier = item[11]

    #draw item buy button
    storeButton = pygame.Rect(20, row, 45, 45)
    buyButtonImage = storeBoard.subsurface((0,0+(itemNumber*58),45,45))
    DISPLAYSURF.blit(buyButtonImage, (19,row-1))

    #draw item opacity
    storeButtonSurface = pygame.Surface((40,40))  
    storeButtonOpacity = 0

    #draw manager button
    managerButton = pygame.Rect((row+20)-50, 725, 45, 45)
    if not managerStatus:    
    
        pygame.draw.rect(DISPLAYSURF, RED, managerButton, 2)
    else:
        pygame.draw.rect(DISPLAYSURF, RED, managerButton)

    #draw manager button opacity
    managerButtonSurface = pygame.Surface((45,45))  
    managerButtonOpacity = 0

    mouse_pos = pygame.mouse.get_pos()
    if (storeButton.collidepoint(mouse_pos)):
        storeButtonOpacity = 75

    if (managerButton.collidepoint(mouse_pos)):
        managerButtonOpacity = 75
        if managerCost >= 100000:
            drawNumber(managerCost, (row+20)-50, 705, font1, "left")
        else:   
            drawNumber(managerCost, (row+20)-50, 705, font1, "left")

    storeButtonSurface.set_alpha(storeButtonOpacity)     
    storeButtonSurface.fill((255,255,255))     
    DISPLAYSURF.blit(storeButtonSurface, (24,row+3))

    managerButtonSurface.set_alpha(managerButtonOpacity)
    managerButtonSurface.fill((255,255,255))
    DISPLAYSURF.blit(managerButtonSurface, ( (row+20)-50 , 725))

    #draw gain bar
    if speed < 50:
        pygame.draw.rect(DISPLAYSURF, GREEN, (306, row, length, 44))
    elif(managerStatus == True):
        pygame.draw.rect(DISPLAYSURF, GREEN, (306, row, 195, 44))
    else:
        pygame.draw.rect(DISPLAYSURF, GREEN, (306, row, length, 44))

    gainButton = pygame.Rect(305, row, 195, 45)
    pygame.draw.rect(DISPLAYSURF, BLACK, gainButton, 2)
    
    #draw numbers
    drawNumber(cost, 75, row+10, font1, "left")
    drawNumber(amount, 295, row+10, font1, "right")
    drawNumber(gain, 510, row+10, font1, "left") 

    drawTitle(name, 75, row+30, font1)
    
    #return the new values for current item 
    return [storeButton, gainButton, amount, itemNumber, cost, gain, length, active, 
    managerStatus, managerButton, managerCost, costMultilplier, gainMultiplier]

def upgradeButtons(item):
    name = item[0]
    cost = item[1]
    position = item[2]
    itemNumber = item[3]
    offset = item[4]
    effect = item[5]
    itemInfluenced = item[6]
    active = item[7]

    global upgradeWindow

    upgradeButton = pygame.Rect(position, 805, 35, 35)
    upgradeButtonImage = upgradeBoard.subsurface((0,0+(itemInfluenced*58),35,35))
    DISPLAYSURF.blit(upgradeButtonImage, (position,805))

    upgradeButtonSurface = pygame.Surface((35,35))  
    upgradeButtonOpacity = 0

    mouse_pos = pygame.mouse.get_pos()
    if (upgradeButton.collidepoint(mouse_pos) and upgradeWindow.collidepoint(mouse_pos)):
        upgradeButtonOpacity = 75
        drawNumber(cost, position, 793, font2, "left")
        drawTitle(name, position, 780, font1)

    upgradeButtonSurface.set_alpha(upgradeButtonOpacity)     
    upgradeButtonSurface.fill((255,255,255))     
    DISPLAYSURF.blit(upgradeButtonSurface, (position,805))


    if active:
        checkMarkImage = checkBox.subsurface((0,0,35,35))
        DISPLAYSURF.blit(checkMarkImage, (position,805))

    return[upgradeButton, cost, position, itemNumber, offset, itemInfluenced]

#loop for entire store screen 
def storeScreen():

    #draw background
    DISPLAYSURF.blit(background, (0,0)) 
    DISPLAYSURF.blit(mainMenu, (680, 860))
    
    #variables 
    global itemsIndex
    global mileStonesIndex
    global upgradesIndex
    global profit
    global mileStones
    global buyModeQuantityList
    global buyModeQuantityIndex
    global dragging
    global offset_x
    global menuButtonOpacity
    global buyModeButtonOpacity
    global upgradeWindow

    storeItemsFullLen = len(storeItemsFull) - 1
    nextRow = 95

    upgradeItemsFullLen = len(upgradeItemsFull) - 1
    
    #Draw the title texts
    drawTitle('Revenue:', 10, 20, font1)

    if profit >= 100000000:
        drawNumber(profit, 120, 20, font1, "left")
    else:
        drawNumber(profit, 120, 20, font1, "left")

    drawTitle('cost', 75, 80, font1)
    drawTitle('quantity', 285, 80, font1)
    drawTitle('profit', 510, 80, font1)

    #buy mode button
    buyModeButton = pygame.Rect(665, 12, 40, 40)
    pygame.draw.rect(DISPLAYSURF, RED, buyModeButton, 2)
    drawTitle(buyModeQuantityList[buyModeQuantityIndex], 670, 30, font2)

    #checks if there are remaining store items
    if itemsIndex <= storeItemsFullLen:
        
        #check if next item should be added
        if profit >= storeItemsFull[itemsIndex][1] * 0.6:
            storeItems.append(storeItemsFull[itemsIndex])
            itemsIndex += 1

        #Draws a sillouete of the next item 
        DISPLAYSURF.blit(itemSillouete, (20, 155+((itemsIndex-1)*60)))

    #checks if there are remaining upgrade items
    if upgradesIndex <= upgradeItemsFullLen:

        #check if the next item should be added 
        if profit >= upgradeItemsFull[upgradesIndex][1] * 0.6:
            upgradesItems.append(upgradeItemsFull[upgradesIndex])
            upgradeItemsFull[upgradesIndex][2] = upgradeItemsFull[upgradesIndex - 1 ][2] + 50
            upgradesIndex += 1

    #checks which buisnesses are accessible by the player
    values = []
    for x in storeItems:
        values.append(storeButtons(x, nextRow))
        nextRow += 60

    #checks which upgrades are accessible by the player
    upgradeValues = []
    for x in upgradesItems:
        upgradeValues.append(upgradeButtons(x))

    #event loop
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    menuButtonSurface = pygame.Surface((30,30)) 
    buyModeButtonSurface = pygame.Surface((40,40))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        #Return to main menu
        if menuRect.collidepoint(mouse_pos):
            menuButtonOpacity = 75
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                startScreen()
                displayStore = False
                menuButtonOpacity = 0
        elif not menuRect.collidepoint(mouse_pos):
            menuButtonOpacity = 0


        #buy Mode button
        if buyModeButton.collidepoint(mouse_pos):
            buyModeButtonOpacity = 75
            if  event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if buyModeQuantityIndex < len(buyModeQuantityList) - 1:
                    buyModeQuantityIndex += 1
                else:
                    buyModeQuantityIndex = 0
        elif not buyModeButton.collidepoint(mouse_pos):
            buyModeButtonOpacity = 0

        #Checks each upgrade items events
        for u in upgradeValues:

            #upgrade window scroll logic 
            if upgradeWindow.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEWHEEL:
                    if event.y > 0 and upgradeValues[upgradesIndex-1][0].x > 560:
                        upgradesItems[u[3]][2] -= 20
                    elif event.y < 0 and upgradeValues[0][0].x < 100:
                       upgradesItems[u[3]][2] += 20

            #upgrade purchase logic
            if (profit >= upgradesItems[u[3]][1] and u[0].collidepoint(mouse_pos) 
                and event.type == pygame.MOUSEBUTTONUP and event.button == 1 and upgradesItems[u[3]][7] == False and upgradeWindow.collidepoint(mouse_pos)):

                upgradesItems[u[3]][7] = True
                profit -= upgradesItems[u[3]][1]
                storeItems[u[5]][2] *= upgradesItems[u[3]][5]
                storeItems[u[5]][11] *= upgradesItems[u[3]][5]

        #checks each store items events
        for b in values:

            #Buy Item Button
            if (profit >= storeItems[b[3]][1] and b[0].collidepoint(mouse_pos) 
              and event.type == pygame.MOUSEBUTTONUP and event.button == 1):


                if buyModeQuantityIndex == 0:
                    profit -= storeItems[b[3]][1]

                    storeItems[b[3]][3] += 1
                    storeItems[b[3]][1] *= storeItems[b[3]][10]
                    storeItems[b[3]][2] += storeItems[b[3]][11]

                elif (buyModeQuantityIndex == 1 and (profit >= initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** (storeItems[b[3]][3] + 25)) / (1 - storeItems[b[3]][10]) - initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** storeItems[b[3]][3])/(1 - storeItems[b[3]][10]) )):
                    profit -= initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** (storeItems[b[3]][3] + 25)) / (1 - storeItems[b[3]][10]) - initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** storeItems[b[3]][3])/(1 - storeItems[b[3]][10])

                    storeItems[b[3]][3] += 25
                    storeItems[b[3]][1] = initialCosts[b[3]] * storeItems[b[3]][10] ** (storeItems[b[3]][3])
                    storeItems[b[3]][2] = 1 * storeItems[b[3]][11] * (storeItems[b[3]][3])

                elif (buyModeQuantityIndex == 2 and (profit >= initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** (storeItems[b[3]][3] + 100)) / (1 - storeItems[b[3]][10]) - initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** storeItems[b[3]][3])/(1 - storeItems[b[3]][10]) )):
                    profit -= initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** (storeItems[b[3]][3] + 100)) / (1 - storeItems[b[3]][10]) - initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** storeItems[b[3]][3])/(1 - storeItems[b[3]][10])

                    storeItems[b[3]][3] += 100
                    storeItems[b[3]][1] = initialCosts[b[3]] * storeItems[b[3]][10] ** (storeItems[b[3]][3])
                    storeItems[b[3]][2] = 1 * storeItems[b[3]][11] * (storeItems[b[3]][3])

                elif (buyModeQuantityIndex == 3 and (profit >= storeItems[b[3]][1])):

                    priceGrowth = storeItems[b[3]][10]
                    currentOwned = storeItems[b[3]][3]
                    logFunction = ( (profit*(priceGrowth-1))/(initialCosts[b[3]]*(priceGrowth ** currentOwned)) ) + 1
                    maxPurchase = math.floor(math.log(logFunction ,priceGrowth))

                    profit -= initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** (storeItems[b[3]][3] + maxPurchase)) / (1 - storeItems[b[3]][10]) - initialCosts[b[3]] * (1 - storeItems[b[3]][10] ** storeItems[b[3]][3])/(1 - storeItems[b[3]][10])

                    storeItems[b[3]][3] += maxPurchase
                    storeItems[b[3]][1] = initialCosts[b[3]] * storeItems[b[3]][10] ** (storeItems[b[3]][3])
                    storeItems[b[3]][2] = 1 * storeItems[b[3]][11] * (storeItems[b[3]][3])

            #gain bar button
            if (b[1].collidepoint(mouse_pos) and b[2] != 0 and event.type == pygame.MOUSEBUTTONUP 
              and storeItems[b[3]][8] == False and event.button == 1):

                storeItems[b[3]][7] = True

            #manager button
            if (profit >= storeItems[b[3]][9] and b[9].collidepoint(mouse_pos) 
              and event.type == pygame.MOUSEBUTTONUP and storeItems[b[3]][8] != True 
              and storeItems[b[3]][3] >= 1 and event.button == 1):

                storeItems[b[3]][8] = True
                profit -= storeItems[b[3]][9]

    for v in values:

        #mile Stone logic 
        i = 0
        for s in mileStones:
            if storeItems[v[3]][3] >= s and mileStonesIndex[v[3]] < (i+1):
                mileStonesIndex[v[3]] = (i+1)
                storeItems[v[3]][6] *= 2
            i += 1
        #Gain button logic
        if v[6] <= 195 and storeItems[v[3]][7] == True or storeItems[v[3]][8] == True:
            storeItems[v[3]][5] += storeItems[v[3]][6]

        if v[6] >= 190:
            storeItems[v[3]][5] = 0
            storeItems[v[3]][7] = False
            profit += storeItems[v[3]][2]

    #update Screen
    menuButtonSurface.set_alpha(menuButtonOpacity)     
    menuButtonSurface.fill((255,255,255))     
    DISPLAYSURF.blit(menuButtonSurface, (680,860))


    buyModeButtonSurface.set_alpha(buyModeButtonOpacity)     
    buyModeButtonSurface.fill((255,255,255))     
    DISPLAYSURF.blit(buyModeButtonSurface, (665, 12))


    upgradeWindowCoverRight = background.subsurface((600,800,125,45))
    upgradeWindowCoverLeft = background.subsurface((0,800,100,45))
    DISPLAYSURF.blit(upgradeWindowCoverRight, (600,800))
    DISPLAYSURF.blit(upgradeWindowCoverLeft, (0,800))
    pygame.draw.rect(DISPLAYSURF, GRAY, upgradeWindow, 2)
    pygame.display.flip()


#Game loop
state = startScreen()
print(state)
while running:

    if state == "store":
        storeScreen()




