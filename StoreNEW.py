#capitalistMining Created by Andrew Ely


'''

CHECKLIST
---------
- All businesses milestones
- All business upgrades 
- upgrade values
- cash per second total
- cash per second per business
- cash per second per business dynamic ranking (best earners are indetified on screen)
- idle cash gain between game sessions 
- save data 
- "Angel Investors" / resets

'''


import pygame, sys, math
import time as Time
from decimal import Decimal
import random
from upgradeItems import *
from storeItems import *
from levels import *

#initialize Pygame 
pygame.init()
pygame.display.set_caption('capitalist')
clock = pygame.time.Clock()

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
managerBoard = pygame.image.load('pngImages/managerBoard.png')
mainMenu = pygame.image.load('pngImages/mainMenu.png')
background = pygame.image.load('pngImages/background.png')
itemSillouete = pygame.image.load('pngImages/nextItemSillouete.png')
upgradeBoard = pygame.image.load('pngImages/upgradeBoard.png')
checkBox = pygame.image.load('pngImages/checkBox.png')
chains = pygame.image.load('pngImages/menuChains.png')
unlockChain = pygame.image.load('pngImages/unlockChain.png')
torchLight = pygame.image.load('pngImages/torchLight.png')

minecartRailUp = pygame.image.load('pngImages/railUp.png')
minecartRailUpTopLeft = pygame.image.load('pngImages/railUpTopLeft.png')
minecartRailUpBottomRight = pygame.image.load('pngImages/railUpBottomRight.png')
minecartRailStraight = pygame.image.load('pngImages/railStraight.png')
minecartRailDown = pygame.image.load('pngImages/railDown.png')
minecartRailDownTopRight = pygame.image.load('pngImages/railDownTopRight.png')
minecartRailDownBottomLeft = pygame.image.load('pngImages/railDownBottomLeft.png')
minecartPlayer = pygame.image.load('pngImages/minerMinecartFlat.png')
minecartPlayerJump = pygame.image.load('pngImages/minerMinecartJump.png')
dynamite = pygame.image.load('pngImages/Dynamite.png')
minecartLevelBackground = pygame.image.load('pngImages/minecartLevelBackground.png')

finishLevel2 = pygame.image.load('pngImages/finishLevel2.png')
torchLight_rect = torchLight.get_rect()
torchImage = pygame.image.load('pngImages/torch.png')

level3Background = pygame.image.load('pngImages/level3Background.png')
valveEmptyImage = pygame.image.load('pngImages/valveEmpty.png')
valveFullImage = pygame.image.load('pngImages/valveFull.png')
pipeUpImage = pygame.image.load('pngImages/pipeUp.png')
pipeDownImage = pygame.image.load('pngImages/pipeDown.png')
pipeLeftImage = pygame.image.load('pngImages/pipeLeft.png')
pipeRightImage = pygame.image.load('pngImages/pipeRight.png')
valveSwitch = pygame.image.load('pngImages/valveSwitch.png')
level3Finish = pygame.image.load('pngImages/level3Finish.png')
minerLeftWalk = pygame.image.load('pngImages/minerLeft.png')
minerRightWalk = pygame.image.load('pngImages/minerRight.png')
minerLeftWalk2 = pygame.image.load('pngImages/minerLeft2.png')
minerRightWalk2 = pygame.image.load('pngImages/minerRight2.png')
minerIdle = pygame.image.load('pngImages/minerIdle.png')
airBubble = pygame.image.load('pngImages/airBubble.png')
squid = pygame.image.load('pngImages/squid.png')
fish = pygame.image.load('pngImages/fish.png')
level6Background = pygame.image.load('pngImages/level6Background.png')
level1Background = pygame.image.load('pngImages/level1Background.png')
level4Background = pygame.image.load('pngImages/level4Background.png')
level10Lava = pygame.image.load('pngImages/level10Lava.png')
minerSwimmingIdle = pygame.image.load('pngImages/minerSwimmingIdle.png')
minerSwimming1 = pygame.image.load('pngImages/minerSwimming1.png')
minerSwimming2 = pygame.image.load('pngImages/minerSwimming2.png')
minerIdleJump = pygame.image.load('pngImages/minerIdleJump.png')
minerTopView1 = pygame.image.load('pngImages/minerTopView1.png')
minerTopView2 = pygame.image.load('pngImages/minerTopView2.png')
minerTopView3 = pygame.image.load('pngImages/minerTopView3.png')
minerTopView4 = pygame.image.load('pngImages/minerTopView4.png')
minerTopView5 = pygame.image.load('pngImages/minerTopView5.png')
minerTopView6 = pygame.image.load('pngImages/minerTopView6.png')
minerTopView7 = pygame.image.load('pngImages/minerTopView7.png')
minerTopView8 = pygame.image.load('pngImages/minerTopView8.png')
minerTopViewIdle = pygame.image.load('pngImages/minerTopViewIdle.png')
minerLeftJump = pygame.image.load('pngImages/minerLeftJump.png')
minerRightJump = pygame.image.load('pngImages/minerRightJump.png')

batStill = pygame.image.load('pngImages/batStill.png')
bat1 = pygame.image.load('pngImages/bat1.png')
bat2 = pygame.image.load('pngImages/bat2.png')
skeleton1 = pygame.image.load('pngImages/skeleton1.png')
skeleton2 = pygame.image.load('pngImages/skeleton2.png')

ratRight1 = pygame.image.load('pngImages/ratRight1.png')
ratRight2 = pygame.image.load('pngImages/ratRight2.png')
ratLeft1 = pygame.image.load('pngImages/ratLeft1.png')
ratLeft2 = pygame.image.load('pngImages/ratLeft2.png')

#fonts
font1 = pygame.font.SysFont('monaco', 24)
font2 = pygame.font.SysFont('monaco', 18)

#set windows icon (top left of window)
pygame.display.set_icon(logo)

#game variables
running = True
displayStore = False
displayMine = False
displayMainMenu = True
profit = 400000000000000000000
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

hints = [
            ["Welcome! Here you will buy businesses to gain money, purchase your first business!",20,225,675,100],
            ["Managers run your businesses for you, so you don't have to! Buy your first manager!",20,600,675,100],
            ["Buy mode allows you to buy multiple of one business in one click!",125,35,530,35],
            ["Upgrades greatly increase a businesses profit!",120,772,475,30],
            ["The speed of a business increases the more you buy!",20,425,675,100],
            ["Don't forget to check on your Mines!",325,850,300,30]
        ]
hintProgress = 0
hintButtonActive = True
hintButton = pygame.Rect(hints[0][1], hints[0][2], hints[0][3], hints[0][4])
hintButtonSurface = pygame.Surface((hints[0][3], hints[0][4]))
hintButtonOpacity = 0

storeButtonOpacity = 0
mineButtonOpacity = 0
mineLocked = True

#function to display the entire start screen
def startScreen():

    global mineLocked
    global displayStore
    global displayMine
    global displayMainMenu
    global storeButtonOpacity
    global mineButtonOpacity
    global profit

    #Start screen drawing
    storeButton = pygame.Rect(205, 495, 300, 150)
    mineButton = pygame.Rect(205, 315, 300, 150) 

    storeButtonSurface = pygame.Surface((300,150))  
    mineButtonSurface = pygame.Surface((300,150))  
    
    
    #start screen loop 
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if storeButton.collidepoint(mouse_pos):
            storeButtonOpacity = 75
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                displayMainMenu = False
                displayStore = True
        elif not storeButton.collidepoint(mouse_pos):
            storeButtonOpacity = 0

        if mineButton.collidepoint(mouse_pos) and not mineLocked:
            mineButtonOpacity = 75
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                displayMainMenu = False
                displayMine = True
        elif not mineButton.collidepoint(mouse_pos):
            mineButtonOpacity = 0

    #Draw to screen
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(logo, (275, 100))
    DISPLAYSURF.blit(menu, (125, 225))

    if profit >= 1000:
        mineLocked = False
    if mineLocked:
        DISPLAYSURF.blit(chains, (125, 225))

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
    if pos == 'center':
        rect.center = (x,y)

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
    managerButtonImage = managerBoard.subsurface((0,0+(itemNumber*58),45,45))
    DISPLAYSURF.blit(managerButtonImage, (row-30,725))
    if managerStatus:
        checkMarkImage = checkBox.subsurface((0,0,35,35))
        DISPLAYSURF.blit(checkMarkImage, (row-30,725))
        

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
    if speed < 15:
        pygame.draw.rect(DISPLAYSURF, GREEN, (306, row, length, 44))
    elif(managerStatus == True):
        pygame.draw.rect(DISPLAYSURF, GREEN, (306, row, 194, 44))
    else:
        pygame.draw.rect(DISPLAYSURF, GREEN, (306, row, length, 44))

    gainButton = pygame.Rect(305, row, 195, 45)
    pygame.draw.rect(DISPLAYSURF, BLACK, gainButton, 2)
 
    
    #draw numbers
    if buyModeQuantityIndex == 0:
        quantity = 1
    if buyModeQuantityIndex == 1:
        quantity = 25
        surface = font1.render('{0}'.format(quantity), True, RED)
        rect = (40,row+25,25,25)
        DISPLAYSURF.blit(surface, rect)
    if buyModeQuantityIndex == 2:
        quantity = 100
        surface = font1.render('{0}'.format(quantity), True, RED)
        rect = (40,row+25,25,25)
        DISPLAYSURF.blit(surface, rect)
    if buyModeQuantityIndex == 3:

        logFunction = ( (profit*(costMultilplier-1))/(initialCosts[itemNumber]*(costMultilplier ** amount)) ) + 1
        quantity = math.floor(math.log(logFunction ,costMultilplier))
        surface = font1.render('{0}'.format(quantity), True, RED)
        rect = (40,row+25,25,25)
        DISPLAYSURF.blit(surface, rect)

    costCalculation = cost * (costMultilplier**quantity - 1)/(costMultilplier - 1)
    if costCalculation == 0:
        costCalculation = cost
    drawNumber(costCalculation, 75, row+10, font1, "left")
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
    global hintButton
    global hintProgress
    global hintButtonActive
    global hintButtonSurface
    global hintButtonOpacity
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
    global displayStore
    global displayMainMenu
    

    storeItemsFullLen = len(storeItemsFull) - 1
    nextRow = 95

    upgradeItemsFullLen = len(upgradeItemsFull) - 1
    
    #Draw the title texts
    drawTitle('Revenue:', 10, 20, font1)
    drawNumber(profit, 120, 20, font1, "left")

    drawTitle('cost', 75, 80, font1)
    drawTitle('quantity', 285, 80, font1)
    drawTitle('profit', 510, 80, font1)


    #buy mode button
    buyModeButton = pygame.Rect(665, 12, 40, 40)
    pygame.draw.rect(DISPLAYSURF, BLACK, buyModeButton, 2)
    drawTitle(buyModeQuantityList[buyModeQuantityIndex], 670, 30, font2)

    #Draw hint button
    if hintButtonActive:
        pygame.draw.rect(DISPLAYSURF, BLACK, hintButton, 2)
        hintTextSurface = font1.render(hints[hintProgress][0], True, BLACK)
        hintTextRect = hintTextSurface.get_rect()
        hintTextRect.center = hintButton.center
        DISPLAYSURF.blit(hintTextSurface, hintTextRect)

        hintButtonSurface.set_alpha(hintButtonOpacity)     
        hintButtonSurface.fill((255,255,255))     
        DISPLAYSURF.blit(hintButtonSurface, (hints[hintProgress][1], hints[hintProgress][2]))

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
                displayStore = False
                displayMainMenu = True
                menuButtonOpacity = 0
        elif not menuRect.collidepoint(mouse_pos):
            menuButtonOpacity = 0

        #hints
        if profit > (hintProgress) * 1000 and hintProgress < len(hints):
            hintButton = pygame.Rect(hints[hintProgress][1], hints[hintProgress][2], hints[hintProgress][3], hints[hintProgress][4])
            hintButtonSurface = pygame.Surface((hints[hintProgress][3], hints[hintProgress][4]))
            hintButtonActive = True   
            if hintButton.collidepoint(mouse_pos):
                hintButtonOpacity = 75
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    hintProgress += 1
                    hintButtonActive = False
            elif not hintButton.collidepoint(mouse_pos):
                hintButtonOpacity = 0


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
        

    pygame.display.flip()


levelSelect = [

    {"levelNumber": 0 , "rectangle" : pygame.Rect(40,50,310,100), "completed": False, "purchased": False, "cost": 2500},
    {"levelNumber": 1 , "rectangle" : pygame.Rect(40,200,310,100), "completed": False, "purchased": False, "cost": 10000},
    {"levelNumber": 2 , "rectangle" : pygame.Rect(40,350,310,100), "completed": False, "purchased": False, "cost": 100000},
    {"levelNumber": 3 , "rectangle" : pygame.Rect(40,500,310,100), "completed": False, "purchased": False, "cost": 500000},
    {"levelNumber": 4 , "rectangle" : pygame.Rect(40,650,310,100), "completed": False, "purchased": False, "cost": 1000000},
    {"levelNumber": 5 , "rectangle" : pygame.Rect(370,50,310,100), "completed": False, "purchased": False, "cost": 10000000},
    {"levelNumber": 6 , "rectangle" : pygame.Rect(370,200,310,100), "completed": False, "purchased": False, "cost": 100000000},
    {"levelNumber": 7 , "rectangle" : pygame.Rect(370,350,310,100), "completed": False, "purchased": False, "cost": 1000000000},
    {"levelNumber": 8 , "rectangle" : pygame.Rect(370,500,310,100), "completed": False, "purchased": False, "cost": 5000000000},
    {"levelNumber": 9 , "rectangle" : pygame.Rect(370,650,310,100), "completed": False, "purchased": False, "cost": 10000000000}

]
levelButtonOpacity = 0
levelActive = False
currentLevel = 0


def mineScreen():

    global profit
    global menuButtonOpacity
    global displayMainMenu
    global displayMine
    global levelSelect
    global levelButtonOpacity
    global levelActive
    global currentLevel

    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(mainMenu, (680, 860))
    drawTitle('Revenue:', 10, 20, font1)
    drawNumber(profit, 120, 20, font1, "left")

    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    for level in levelSelect:
        pygame.draw.rect(DISPLAYSURF, BLACK, level['rectangle'], 5)
        drawTitle('Level ' + str((level['levelNumber']+1)) , level['rectangle'][0]+10, level['rectangle'][1]+15, font1)
        if not level['purchased']:
            DISPLAYSURF.blit(unlockChain, (level['rectangle'][0], level['rectangle'][1]-10))
            drawTitle('cost ' , level['rectangle'][0]+135, level['rectangle'][1]+75, font1)
            drawNumber(level['cost'], level['rectangle'][0]+150, level['rectangle'][1]+90, font2, "center")
        if level['completed']:
            DISPLAYSURF.blit(checkBox, (level['rectangle'][0]+60, level['rectangle'][1]-10))

        if level['rectangle'].collidepoint(mouse_pos):
            levelButtonOpacity = 75
        else:
            levelButtonOpacity = 0
        levelButtonSurface = pygame.Surface((level['rectangle'][2],level['rectangle'][3]))
        levelButtonSurface.set_alpha(levelButtonOpacity)     
        levelButtonSurface.fill((255,255,255))     
        DISPLAYSURF.blit(levelButtonSurface, (level['rectangle'][0],level['rectangle'][1]))

    

    menuButtonSurface = pygame.Surface((30,30))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        #Return to main menu
        if menuRect.collidepoint(mouse_pos):
            menuButtonOpacity = 75
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                displayMine = False
                displayMainMenu = True
                menuButtonOpacity = 0
        elif not menuRect.collidepoint(mouse_pos):
            menuButtonOpacity = 0

        

        for level in levelSelect:
            if level['rectangle'].collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if profit >= level['cost'] and not level['purchased']:
                        level['purchased'] = True
                        profit -= level['cost']
                    elif level['purchased']:
                        currentLevel = level['levelNumber']
                        levelActive = True
                        displayMine = False

    menuButtonSurface.set_alpha(menuButtonOpacity)     
    menuButtonSurface.fill((255,255,255))     
    DISPLAYSURF.blit(menuButtonSurface, (680,860))



    pygame.display.flip()




class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0

    def update(self):
        if self.direction == -1:
            if frame <= 30:
                self.image = minerLeftWalk
            else:
                self.image = minerLeftWalk2
        elif self.direction == 1:
            if frame <= 30:
                self.image = minerRightWalk
            else:
                self.image = minerRightWalk2
        elif self.direction == 2:
            self.image = minerIdleJump
        else:
            self.image = minerIdle

class PlayerLevel10(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0
        self.isJumping = False
        self.startingY = self.rect.y
        self.isGrounded = False

    def update(self):
        if self.isJumping:
            player.rect.y -= 12
        if self.rect.y <= self.startingY - 120:
            self.isJumping = False

        if self.direction == 0:
            if self.isJumping:
                self.image = minerIdleJump
            else:
                self.image = minerIdle

        if self.direction == 1:
            if self.isJumping:
                self.image = minerLeftJump
            elif frame <= 30:
                self.image = minerLeftWalk
            else:
                self.image = minerLeftWalk2
        if self.direction == 2:
            if self.isJumping:
                self.image = minerRightJump
            elif frame <= 30:
                self.image = minerRightWalk
            else:
                self.image = minerRightWalk2

class LavaLevel10(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level10Lava
        self.rect = self.image.get_rect(topleft=(x,y))
        self.topOut = False

    def update(self, scrollSpeed):
        if self.rect.y >= 700 and not self.topOut:
            self.rect.y -= scrollSpeed
        if self.topOut and self.rect.y >= 240:
            self.rect.y -= scrollSpeed*2

class FinishBlockLevel10(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level3Finish
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        if self.rect.y <= 75:
            self.rect.y += scrollSpeed

class floorBlockLevel10(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, scrollSpeed):
        self.rect.y += scrollSpeed

        if self.rect.y >= 900:
            self.kill()
        
class topFloorBlockLevel10(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        if self.rect.y <= 200:
            self.rect.y += scrollSpeed
        else:
            global level10StopScrolling
            level10StopScrolling = True

class Level10Background(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level1Background
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, scrollSpeed):
        self.rect.y += scrollSpeed

class Level1Background(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level1Background
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, scrollSpeed):
        self.rect.y -= scrollSpeed

class PlayerTopView(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerTopViewIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0

    def update(self):
        if self.direction == 1: #left
            if frame <= 30:
                self.image = minerTopView7
            else:
                self.image = minerTopView8
        elif self.direction == 2: #right
            if frame <= 30:
                self.image = minerTopView5
            else:
                self.image = minerTopView6
        elif self.direction == 3: #up
            if frame <= 30:
                self.image = minerTopView1
            else:
                self.image = minerTopView2
        elif self.direction == 4: #down
            if frame <= 30:
                self.image = minerTopView3
            else:
                self.image = minerTopView4
        else:
            self.image = minerTopViewIdle

class PlayerMinecart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartPlayer
        self.rect = self.image.get_rect(topleft=(x,y))
        self.isJumping = False
        self.startingY = self.rect.y
        self.isGrounded = False
 
    def update(self):
        if self.isGrounded == False and self.isJumping == False:
            self.rect.y += 6

        if self.isJumping:
            self.image = minecartPlayerJump
            self.rect.y -= 6

            if self.rect.y <= self.startingY - 110:
                self.isJumping = False
                self.image = minecartPlayer

class floorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, scrollSpeed):
        self.rect.y -= scrollSpeed

        if self.rect.y <= -32:
            self.kill()
        
class bottomFloorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        if self.rect.y >= 868:
            self.rect.y -= scrollSpeed
        else:
            global level1StopScrolling
            level1StopScrolling = True
        

class MinecartFinishBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level3Finish
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

class FinishBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level3Finish
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        if self.rect.y >= 736:
            self.rect.y -= scrollSpeed

class FinishLevel2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = finishLevel2
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        pass

class stillFloorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        pass

class SidescrollFloorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self,scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()

class SidescrollKillBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = dynamite
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()

class SidescrollUpRail(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailUp
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()
class SidescrollUpRailTopLeft(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailUpTopLeft
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self,scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()
class SidescrollUpRailBottomRight(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailUpBottomRight
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()

class SidescrollDownRail(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailDown
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self,scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()
class SidescrollDownRailBottomLeft(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailDownBottomLeft
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self,scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()
class SidescrollDownRailTopRight(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailDownTopRight
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self,scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()

class SidescrollStraightRail(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartRailStraight
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self,scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.x <= -32:
            self.kill()

class SidescrollBackground(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minecartLevelBackground
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

class Torch(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = torchImage
        self.rect = self.image.get_rect(topleft=(x,y))
        self.collected = False
    def update(self):
        pass

class playerLevel3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0   #  0:idle   1:left   2:right

    def update(self):
        if self.direction == 0:
            self.image = minerIdle
        if self.direction == 1:
            if frame <= 15:
                self.image = minerLeftWalk
            else:
                self.image = minerLeftWalk2
        if self.direction == 2:
            if frame <= 15:
                self.image = minerRightWalk
            else:
                self.image = minerRightWalk2

class Level6FloorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, playerX, playerSpeed, direction):
        self.rect.x += (playerSpeed-1)*direction
        
   

class Level6Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerSwimmingIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0   #  different than playerDirection variable and param

    def update(self, playerDirection):
        if playerDirection == 1:
            if frame <= 30:
                self.image = minerSwimming1
            else:
                self.image = minerSwimming2
        else:
            self.image = minerSwimmingIdle

class Level6Enemy1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = fish
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self,playerSpeed, direction):
        if direction == 1:
            self.rect.x -= 1
        elif direction == -1:
            self.rect.x -= 3
        else:
            self.rect.x -= 2

class Level6Enemy2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = squid
        self.rect = self.image.get_rect(topleft=(x,y))
        self.topRange = self.rect.y - 150
        self.bottomRange = self.rect.y + 150
        self.direction = 1
        self.collidedWall = False

    def update(self, playerX, playerSpeed, direction):

        if self.rect.y == self.topRange:
            self.direction = 1
        if self.rect.y == self.bottomRange:
            self.direction = -1
        if self.collidedWall:
            self.direction = self.direction * -1
            self.collidedWall = False

        self.rect.x += (playerSpeed-1)*direction

        self.rect.y += self.direction

class Level6Dynamite(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = dynamite
        
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, playerX, playerSpeed, direction):
        self.rect.x += (playerSpeed-1)*direction

class Level6Finish(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, playerX, playerSpeed, direction):
        self.rect.x += (playerSpeed-1)*direction


class Level8Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0   #  different than playerDirection variable and param

    def update(self):
        if self.direction == 1:
            if frame <= 30:
                self.image = minerLeftWalk
            else:
                self.image = minerLeftWalk2
        if self.direction == 2:
            if frame <= 30:
                self.image = minerRightWalk
            else:
                self.image = minerRightWalk2
        else:
            self.image = minerIdle

class Level8Enemy1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.image.fill((0,0,0))
        self.direction = 0   #  different than playerDirection variable and param

    def update(self, playerPosX):
        if self.rect.x <= playerPosX:
            self.rect.x += 1
        if self.rect.x >= playerPosX:
            self.rect.x -= 1

class Level8Enemy2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.image.fill((0,0,0))
        self.direction = 0   #  different than playerDirection variable and param

    def update(self, playerPosX):
        if self.rect.x <= playerPosX:
            self.rect.x += 1
        if self.rect.x >= playerPosX:
            self.rect.x -= 1

class Level8Floor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((0,820))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.image.fill((0,0,0))

    def update(self):
        pass

        

pipesInitial = [

    [[1,1,1,1],[1,1,0,1],[1,1,1,0],[1,1,0,0],[1,1,0,0],[0,0,0,1]],
    [[1,1,1,0],[1,0,1,0],[1,1,0,1],[0,1,1,1],[1,1,0,0],[1,1,1,1]],
    [[1,1,0,0],[1,0,1,1],[0,1,1,0],[1,1,0,1],[1,1,0,0],[1,1,0,0]],
    [[1,1,0,0],[1,1,0,0],[1,0,0,0],[1,1,1,0],[1,1,1,1],[1,1,0,0]],
    [[1,1,0,0],[0,1,0,0],[1,1,0,1],[1,1,0,0],[1,1,1,0],[0,1,0,1]],
    [[1,1,0,0],[0,1,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,0],[1,1,0,0]]


]

class Valve(pygame.sprite.Sprite):
    def __init__(self,x,y,pipes, valveNumber):
        super().__init__()
        self.image = valveEmptyImage
        self.rect = self.image.get_rect(topleft=(x,y))
        self.pipes = pipes
        
        self.valveNumber = valveNumber
        self.full = False

    def rotate(self):
        temp = self.pipes.copy()
        self.pipes[0] = temp[3]
        self.pipes[1] = temp[0]
        self.pipes[2] = temp[1]
        self.pipes[3] = temp[2]
        
    def update(self):
        if self.full:
            self.image = valveFullImage
        if self.full == False:
            self.image = valveEmptyImage

class ValveSwitch(pygame.sprite.Sprite):
    def __init__(self,x,y,valvesAffected):
        super().__init__()
        self.image = valveSwitch
        self.rect = self.image.get_rect(topleft=(x,y))
        self.valvesAffected = valvesAffected

    def update(self):
        pass


def dfsValve(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices that are not visited yet
    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfsValve(adj, visited, i, res)

def DFS(adj, source):
    visited = [False] * len(adj)
    res = []
    dfsValve(adj, visited, source, res)  # Start DFS from vertex 0
    return res

def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1  # Since it's an undirected graph


class Level4FloorBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

class Level4Finish(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect(topleft=(x,y))
    
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

class Level4ExitSign(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level3Finish
        self.rect = self.image.get_rect(topleft=(x,y))
    
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

class Level4Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = minerIdle
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0 #0:idle  1:left  2:right  3:up  4:down
        self.isJumping = False
        self.startingY = self.rect.y
        self.isGrounded = False

 
    def update(self):
        if self.isJumping:
            player.rect.y -= 12
        if self.rect.y <= self.startingY - 120:
            self.isJumping = False

        if self.direction == 0:
            if self.isJumping:
                self.image = minerIdleJump
            else:
                self.image = minerIdle

        if self.direction == 1:
            if self.isJumping:
                self.image = minerLeftJump
            elif frame <= 30:
                self.image = minerLeftWalk
            else:
                self.image = minerLeftWalk2
        if self.direction == 2:
            if self.isJumping:
                self.image = minerRightJump
            elif frame <= 30:
                self.image = minerRightWalk
            else:
                self.image = minerRightWalk2

class Level4Dynamite(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = dynamite
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

class Level4Enemy1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = ratRight2
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 1
        self.direction = 1

    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

        self.rect.x += self.direction * self.speed

        if self.direction == 1:
            if frame <= 30:
                self.image = ratRight2
            else:
                self.image = ratRight1
        if self.direction == -1:
            if frame <= 30:
                self.image = ratLeft2
            else:
                self.image = ratLeft1

class Level4Enemy2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = batStill
        self.rect = self.image.get_rect(topleft=(x,y))
        self.spotted = False
        self.swoop = False
        self.xCor = 81
        self.yInitial = y
        self.endPath = False

    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

        if self.spotted:
            if frame <= 30:
                self.image = bat2
            else:
                self.image = bat1

            yCor = 0.001*self.xCor**2
            self.rect.x -= 1
            if self.xCor >= 0:
                self.rect.y += yCor
            if self.xCor < 0:
                self.rect.y -= yCor
            self.xCor -= 1

            if self.rect.y < self.yInitial-64:
                self.spotted = False
                self.endPath = True
        if self.endPath:
            self.rect.x -=1
            self.rect.y -=1


        if self.rect.y <= 0:
            self.kill()

class Level4Enemy3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = skeleton1
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 0 #1:left  2:right  3:up  4:down
        self.isJumping = False
        self.startingY = self.rect.y
        self.isGrounded = True
 
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

        if self.isJumping:
            self.image = skeleton2
            self.rect.y -= 9
        if self.rect.y <= self.startingY - 150:
            self.isJumping = False
        if self.isGrounded:
            self.image = skeleton1

class BackgroundLevel4(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = level4Background
        self.rect = self.image.get_rect(topleft=(x,y))
 
    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed

#Game loop
initializeLevel = True
frame = 0
while running:
    clock.tick(60)
    frame +=1
    if frame >= 60:
        frame = 0

    if displayMainMenu:
        startScreen()
    elif displayStore:
        storeScreen()
    elif displayMine:
        mineScreen()
    elif levelActive:

        #Level 1, downscrolling avoid getting stuck
        if currentLevel == 0:
            if initializeLevel:

                scrollSpeed = 2
                level1StopScrolling = False

                all_backgrounds = pygame.sprite.Group()
                all_floors = pygame.sprite.Group()
                bottom_floors = pygame.sprite.Group()
                for i, row in enumerate(levelMap0):
                    currentY = 4+ (i * 32)
                    for j, block in enumerate(row):
                        currentX = 8+ (j * 32)
                        if block == 'p':
                            player = Player(currentX,currentY)
                        if block == 'b':
                            new_floor = floorBlock(currentX, currentY)
                            all_floors.add(new_floor)
                        if block == 'e':
                            new_floor = bottomFloorBlock(currentX, currentY)
                            bottom_floors.add(new_floor)
                        if block == 'f':
                            finish = FinishBlock(currentX, currentY)
                
                background1 = Level1Background(0,0)
                background2 = Level1Background(0,900)
                background3 = Level1Background(0,1800)
                background4 = Level1Background(0,2700)
                all_backgrounds.add(background1, background2, background3, background4)

                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            old_x, old_y = player.rect.x, player.rect.y
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and player.rect.x >= 8:
                player.rect.x -= 3
                player.direction = -1
            if keys[pygame.K_d] and player.rect.x <= 680:
                player.rect.x += 3
                player.direction = 1
            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.x = old_x

            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                player.direction = 0

            player.rect.y += 3

            collisions = pygame.sprite.spritecollide(player, all_floors, False)
            if collisions:
                player.rect.bottom = collisions[0].rect.top - 2
            if not collisions:
                player.direction = 2

            collisions = pygame.sprite.spritecollide(player, bottom_floors, False)
            if collisions:
                player.rect.bottom = collisions[0].rect.top - 1
                player.direction = 0

            if player.rect.y <= 0:
                levelActive = False
                initializeLevel = True
                displayMine = True

            if pygame.sprite.collide_rect(player, finish):
                levelActive = False
                initializeLevel = True
                levelSelect[0]['completed'] = True
                displayMine = True


            player.update()
            finish.update(scrollSpeed)
            bottom_floors.update(scrollSpeed)
            if level1StopScrolling == False:
                all_backgrounds.update(scrollSpeed)
                all_floors.update(scrollSpeed)

            all_backgrounds.draw(DISPLAYSURF)
            pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,8,900))
            pygame.draw.rect(DISPLAYSURF, BLACK, (712,0,8,900))
            all_floors.draw(DISPLAYSURF)
            bottom_floors.draw(DISPLAYSURF)
            DISPLAYSURF.blit(player.image, player.rect)
            DISPLAYSURF.blit(finish.image,finish.rect)

            pygame.display.flip()
 

        #level 2, a free-romaing maze with a torch for vision restriction
        if currentLevel == 1:
            if initializeLevel:
                all_floors = pygame.sprite.Group()
                for i, row in enumerate(levelMap1):
                    currentY = 4+ (i * 32)
                    for j, block in enumerate(row):
                        currentX = 8+ (j * 32)
                        if block == 'p':
                            player = PlayerTopView(currentX,currentY+8)
                        if block == 'b':
                            new_floor = stillFloorBlock(currentX, currentY)
                            all_floors.add(new_floor)
                        if block == 't':
                            torch = Torch(currentX, currentY)
                        if block == 'f':
                            finish = FinishLevel2(currentX, currentY)
                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            old_x, old_y = player.rect.x, player.rect.y
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and player.rect.x >= 8:
                player.rect.x -= 2
                player.direction = 1
            if keys[pygame.K_d] and player.rect.x <= 693:
                player.rect.x += 2
                player.direction = 2
            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.x = old_x

            if keys[pygame.K_w] and player.rect.y >= 8:
                player.rect.y -= 2
                player.direction = 3
            if keys[pygame.K_s] and player.rect.y <= 860:
                player.rect.y += 2
                player.direction = 4
            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.y = old_y

            if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                player.direction = 0

            if pygame.sprite.collide_rect(player, finish):
                levelActive = False
                initializeLevel = True
                levelSelect[1]['completed'] = True
                displayMine = True
            if pygame.sprite.collide_rect(player, torch):
                torch.collected = True

 
            player.update()

            DISPLAYSURF.blit(background, (0,0))
            pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,8,900))
            pygame.draw.rect(DISPLAYSURF, BLACK, (712,0,8,900))
            pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,720,8))
            pygame.draw.rect(DISPLAYSURF, BLACK, (0,892,720,8))

            DISPLAYSURF.blit(finish.image, finish.rect)
            DISPLAYSURF.blit(player.image, player.rect)
            all_floors.draw(DISPLAYSURF)
            if torch.collected == False:
                DISPLAYSURF.blit(torch.image, torch.rect)
                torchLight_rect.center = (torch.rect.x+16,torch.rect.y+16)
            elif torch.collected == True:
                torchLight_rect.center = (player.rect.x+16,player.rect.y+16)
            DISPLAYSURF.blit(torchLight, torchLight_rect)
            
            pygame.display.flip()


        #level 3, a puzzle
        if currentLevel == 2:
            if initializeLevel:

                player = playerLevel3(334,668)
                finish = False
                valves_sprites = pygame.sprite.Group()
                switch_sprites = pygame.sprite.Group()
                currentY = 59
                currentValve = 0
                for i, row in enumerate(pipesInitial):
                    currentY += 48 
                    currentX = 176
                    for j, pipe in enumerate(row):
                        currentX+= 48
                        pipes = pipe.copy()
                        new_valve = Valve(currentX, currentY, pipes, currentValve)
                        valves_sprites.add(new_valve)
                        currentValve += 1

                switch1 = ValveSwitch(81,668,[0,1,8,22,27,30])     #blue
                switch2 = ValveSwitch(186,668,[2,7,12,23,28,33])   #red
                switch3 = ValveSwitch(291,668,[3,5,19,24,29,31])   #green
                switch4 = ValveSwitch(396,668,[4,6,11,20,25,35])   #orange
                switch5 = ValveSwitch(501,668,[9,10,14,21,26,34])  #pink
                switch6 = ValveSwitch(606,668,[13,15,16,17,18,32]) #yellow
                switch_sprites.add(switch1,switch2,switch3,switch4,switch5,switch6)

                initializeLevel = False


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        switchCollide = pygame.sprite.spritecollide(player,switch_sprites,False)
                        for switch in switchCollide:
                            switchCollide = switch
                        if switchCollide:
                            for valve in valves_sprites:
                                if valve.valveNumber in switchCollide.valvesAffected:
                                    valve.rotate()


            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.rect.x -= 3
                player.direction = 1
            elif keys[pygame.K_d]:
                player.rect.x += 3
                player.direction = 2
            else:
                player.direction = 0
            if player.rect.x <= -16:
                levelActive = False
                initializeLevel = True
                displayMine = True

            if player.rect.x >= 684 and not finish:
                player.rect.x = 684
            if player.rect.x >= 704 and finish:
                levelActive = False
                initializeLevel = True
                levelSelect[2]['completed'] = True
                displayMine = True
            
            
            DISPLAYSURF.blit(level3Background, (0,0))
            valves_sprites.update()
            valves_sprites.draw(DISPLAYSURF)

            edges = set()
            for valve in valves_sprites:
                if valve.pipes[0] == 1:
                    DISPLAYSURF.blit(pipeUpImage, (valve.rect.x+12, valve.rect.y-8))
                if valve.pipes[1] == 1:
                    DISPLAYSURF.blit(pipeRightImage, (valve.rect.x+32, valve.rect.y+12))
                if valve.pipes[2] == 1:
                    DISPLAYSURF.blit(pipeDownImage, (valve.rect.x+12, valve.rect.y+32))
                if valve.pipes[3] == 1:
                    DISPLAYSURF.blit(pipeLeftImage, (valve.rect.x-8, valve.rect.y+12))

                currentValve = valve
                valveBelow = -1
                valveAbove = -1
                valveLeft = -1
                valveRight = -1
                for v in valves_sprites:
                    if v.valveNumber == currentValve.valveNumber + 6:
                        valveBelow = v
                    if v.valveNumber == currentValve.valveNumber - 1 and currentValve.valveNumber not in [0,6,12,18,24,30]:  
                        valveLeft = v
                    if v.valveNumber == currentValve.valveNumber + 1 and currentValve.valveNumber not in [5,11,17,23,29,35]: 
                        valveRight = v
                    if v.valveNumber == currentValve.valveNumber - 6:
                        valveAbove = v

                #CONSTRUCT EDGE SET
                if (valveBelow != -1) and (currentValve.pipes[2] == 1 and valveBelow.pipes[0] == 1): #below connection
                    e = (valveBelow.valveNumber,currentValve.valveNumber)
                    newEdge = tuple(sorted(e))
                    edges.add(newEdge)
                if (valveAbove != -1) and (currentValve.pipes[0] == 1 and valveAbove.pipes[2] == 1): #above connection
                    e = (valveAbove.valveNumber,currentValve.valveNumber)
                    newEdge = tuple(sorted(e))
                    edges.add(newEdge)
                if (valveLeft != -1) and (currentValve.pipes[3] == 1 and valveLeft.pipes[1] == 1): #left connection
                    e = (valveLeft.valveNumber,currentValve.valveNumber)
                    newEdge = tuple(sorted(e))
                    edges.add(newEdge)
                if (valveRight != -1) and (currentValve.pipes[1] == 1 and valveRight.pipes[3] == 1): #right connection
                    e = (valveRight.valveNumber,currentValve.valveNumber)
                    newEdge = tuple(sorted(e))
                    edges.add(newEdge)
                if currentValve.valveNumber == 6 and currentValve.pipes[3] == 1:
                    edges.add((6,36))


            #RUN DFS 
            V = 37 #ONE EXTRA DUMMY NODE
            adj = [[0] * V for _ in range(V)]
            for s, t in edges:
                add_edge(adj,s,t)
            res = DFS(adj, 36) #STARTING FROM A DUMMY NODE

            for valve in valves_sprites:
                if valve.valveNumber in res:
                    valve.full = True 
                else:
                    valve.full = False
                if 29 in res:
                    finish = True
                if 29 not in res:
                    finish = False

            if finish:
                DISPLAYSURF.blit(level3Finish, (650,495))
            switch_sprites.update()
            player.update()
            DISPLAYSURF.blit(player.image,player.rect)
            switch_sprites.draw(DISPLAYSURF)
           

            pygame.display.flip()




        #level 4, navigate to the end through enemies (like a standard mario level)
        if currentLevel == 3 or currentLevel == 5:
            if initializeLevel: 

                all_floors = pygame.sprite.Group()
                all_dynamite = pygame.sprite.Group()
                all_enemey1 = pygame.sprite.Group()
                all_enemey2 = pygame.sprite.Group()
                all_enemey3 = pygame.sprite.Group()
                finish_blocks = pygame.sprite.Group()
                all_backgrounds = pygame.sprite.Group()
                scroll_sprites = pygame.sprite.Group()

                scrollSpeed = 3
                playerSpeed = 3
                gravity = 5
                step = 0
                stepX = 0
                if currentLevel == 3:
                    levelMap = levelMap3
                if currentLevel == 5:
                    levelMap = levelMap5
                for i, row in enumerate(levelMap):
                    currentY = (step * 32)
                    if (i+1) % 28 == 0: 
                        step = 0
                        stepX +=1
                    else:
                        step+=1
                    for j, block in enumerate(row):
                        currentX = stepX*704+(j*32)
                        if block == 'b':
                            new_floor = Level4FloorBlock(currentX, currentY)
                            all_floors.add(new_floor)
                            scroll_sprites.add(new_floor)
                        if block == 'p':
                            player = Level4Player(currentX, currentY)
                        if block == 'd':
                            new_block = Level4Dynamite(currentX, currentY)
                            scroll_sprites.add(new_block)
                            all_dynamite.add(new_block)
                        if block == '1':
                            new_block = Level4Enemy1(currentX,currentY+16)
                            scroll_sprites.add(new_block)
                            all_enemey1.add(new_block)
                        if block == '2':
                            new_block = Level4Enemy2(currentX,currentY)
                            scroll_sprites.add(new_block)
                            all_enemey2.add(new_block)
                        if block == '3':
                            new_block = Level4Enemy3(currentX, currentY)
                            scroll_sprites.add(new_block)
                            all_enemey3.add(new_block)
                        if block == 'f':
                            new_block = Level4Finish(currentX, currentY)
                            scroll_sprites.add(new_block)
                            finish_blocks.add(new_block)
                        if block == 'e':
                            finishSign = Level4ExitSign(currentX,currentY)
                            scroll_sprites.add(finishSign)

                background1 = BackgroundLevel4(0,0)
                background2 = BackgroundLevel4(2160,0)
                background3 = BackgroundLevel4(4320,0)
                background4 = BackgroundLevel4(6480,0)
                background5 = BackgroundLevel4(8640,0)
                scroll_sprites.add(background1, background2, background3, background4, background5)
                all_backgrounds.add(background1, background2, background3, background4, background5)

                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            old_x, old_y = player.rect.x, player.rect.y
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player.rect.x -= playerSpeed
                player.direction = 1
            if keys[pygame.K_d]:
                player.rect.x += playerSpeed
                player.direction = 2
            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.x = old_x

            if keys[pygame.K_SPACE] and player.isGrounded:
                player.isJumping = True
                player.isGrounded = False
                player.startingY = player.rect.y



            player.rect.y += gravity
            collisions = pygame.sprite.spritecollide(player,all_floors,False)
            if collisions:
                if not player.isJumping:
                    player.rect.bottom = collisions[0].rect.top
                    player.isGrounded = True
                if player.isJumping and player.rect.y <= player.startingY-32:
                    player.isJumping = False
                    

            if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                player.direction = 0

            for enemey in all_enemey1:
                collisions = pygame.sprite.spritecollide(enemey, all_floors, False)
                if collisions:
                    enemey.direction = enemey.direction * -1


            for enemey in all_enemey2:
                distance = math.sqrt((player.rect.x-enemey.rect.x)**2+(player.rect.y-enemey.rect.y)**2)
                if distance <= 200:
                    enemey.spotted = True

            for enemey in all_enemey3:
                enemey.rect.y += gravity//2
                if enemey.isGrounded == True:
                    if frame >= 59:
                        random_int   = random.randint(1,10)
                        if random_int <= 5 and enemey.isGrounded:
                            enemey.isGrounded = False
                            enemey.startingY = enemey.rect.y
                            enemey.isJumping = True
                            
                collisions = pygame.sprite.spritecollide(enemey,all_floors,False)
                if collisions:
                    enemey.rect.bottom = collisions[0].rect.top
                    enemey.isGrounded = True

            if (pygame.sprite.spritecollide(player,all_enemey1,False) or 
            pygame.sprite.spritecollide(player,all_enemey2,False) or
            pygame.sprite.spritecollide(player,all_enemey3,False) or
            pygame.sprite.spritecollide(player,all_dynamite,False)): #Level failed
                levelActive = False
                initializeLevel = True
                displayMine = True
            if pygame.sprite.spritecollide(player, finish_blocks, False): #Level Completed
                levelActive = False
                initializeLevel = True
                levelSelect[3]['completed'] = True
                displayMine = True


            if player.rect.x <= 240:
                currentScroll = -1 * scrollSpeed
                player.rect.x += playerSpeed
            elif player.rect.x >= 480:
                currentScroll = scrollSpeed
                player.rect.x -= playerSpeed
            else:
                currentScroll = 0


            player.update()
            scroll_sprites.update(currentScroll)

            all_backgrounds.draw(DISPLAYSURF)
            all_floors.draw(DISPLAYSURF)
            all_dynamite.draw(DISPLAYSURF)
            all_enemey1.draw(DISPLAYSURF)
            all_enemey2.draw(DISPLAYSURF)
            all_enemey3.draw(DISPLAYSURF)
            finish_blocks.draw(DISPLAYSURF)
            DISPLAYSURF.blit(finishSign.image,finishSign.rect)
            DISPLAYSURF.blit(player.image, player.rect)
            pygame.draw.rect(DISPLAYSURF, RED, player.rect, 2)
            
            pygame.display.flip()


        #level 5, a minecart sidescroller (like geometry dash)
        if currentLevel == 4:
            if initializeLevel:
                
                scrollSpeed = 4

                background_sprites = pygame.sprite.Group()
                all_floors = pygame.sprite.Group()
                kill_blocks = pygame.sprite.Group()
                finish_blocks = pygame.sprite.Group()
                up_rails = pygame.sprite.Group()
                visual_rails = pygame.sprite.Group()
                straight_rails = pygame.sprite.Group()
                down_rails = pygame.sprite.Group()

                background1 = SidescrollBackground(0,0)
                background2 = SidescrollBackground(2160,0)
                background3 = SidescrollBackground(4320,0)
                background4 = SidescrollBackground(6480,0)
                background5 = SidescrollBackground(8640,0)
                background_sprites.add(background1, background2, background3, background4, background5)
                step = 0
                stepX = 0
                for i, row in enumerate(levelMap4):
                    currentY = (step * 32)
                    if (i+1) % 28 == 0: 
                        step = 0
                        stepX +=1
                    else:
                        step+=1
                    for j, block in enumerate(row):
                        currentX = stepX*704+(j*32)
                        if block == 'b':
                            new_floor = SidescrollFloorBlock(currentX, currentY)
                            all_floors.add(new_floor)
                        if block == 'p':
                            player = PlayerMinecart(currentX, currentY)
                        if block == 'k':
                            new_block = SidescrollKillBlock(currentX, currentY)
                            kill_blocks.add(new_block)
                        if block == 'f':
                            finish = MinecartFinishBlock(currentX, currentY)
                        if block == 'u':
                            new_block = SidescrollUpRail(currentX, currentY)
                            up_rails.add(new_block)
                        if block == 'd':
                            new_block = SidescrollDownRail(currentX, currentY)
                            down_rails.add(new_block)
                        if block == 's':
                            new_block = SidescrollStraightRail(currentX, currentY)
                            straight_rails.add(new_block)
                        if block == '1':
                            new_item = SidescrollUpRailTopLeft(currentX,currentY)
                            visual_rails.add(new_item)
                        if block == '2':
                            new_item = SidescrollUpRailBottomRight(currentX,currentY)
                            visual_rails.add(new_item)
                        if block == '3':
                            new_item = SidescrollDownRailBottomLeft(currentX,currentY)
                            visual_rails.add(new_item)
                        if block == '4':
                            new_item = SidescrollDownRailTopRight(currentX,currentY)
                            visual_rails.add(new_item)
                            
                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
            
            if pygame.sprite.spritecollide(player, kill_blocks, False) or player.rect.y >= 800:
                levelActive = False
                initializeLevel = True
                displayMine = True

            if pygame.sprite.collide_rect(player, finish):
                levelActive = False
                initializeLevel = True
                levelSelect[4]['completed'] = True
                displayMine = True
            
            if pygame.sprite.spritecollide(player, straight_rails, False):
                player.image = minecartPlayer
            if pygame.sprite.spritecollide(player, up_rails, False):
                player.rect.y -= 10
                rotatePlayerImage = pygame.transform.rotate(minecartPlayer,45)
                player.image = rotatePlayerImage
            if pygame.sprite.spritecollide(player, down_rails, False):
                player.rect.y -= 1
                rotatePlayerImage = pygame.transform.rotate(minecartPlayer,-45)
                player.image = rotatePlayerImage
            
            collidedFloor = pygame.sprite.spritecollide(player, all_floors, False)
            if collidedFloor:
                for floor in collidedFloor:
                    if player.rect.y <= floor.rect.y:
                        player.isGrounded = True
                    if player.rect.y >= floor.rect.y:
                        player.rect.y = floor.rect.y + 33
                player.isJumping = False
            else:
                player.isGrounded = False
            if player.rect.y <= 260:
                player.rect.y = 270
                player.isJumping = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and player.isJumping == False and player.isGrounded == True:
                player.startingY = player.rect.y
                player.isJumping = True

            background_sprites.update(scrollSpeed)
            all_floors.update(scrollSpeed)
            kill_blocks.update(scrollSpeed)
            finish.update(scrollSpeed)
            up_rails.update(scrollSpeed)
            visual_rails.update(scrollSpeed)
            down_rails.update(scrollSpeed)
            straight_rails.update(scrollSpeed)
            player.update()

            background_sprites.draw(DISPLAYSURF)
            all_floors.draw(DISPLAYSURF)
            kill_blocks.draw(DISPLAYSURF)
            up_rails.draw(DISPLAYSURF)
            visual_rails.draw(DISPLAYSURF)
            straight_rails.draw(DISPLAYSURF) 
            down_rails.draw(DISPLAYSURF)

            DISPLAYSURF.blit(finish.image, finish.rect)
            DISPLAYSURF.blit(player.image, player.rect)
            
            pygame.display.flip()

        

        #level 7, underwater avoid enemies and don't run out of breath 
        if currentLevel == 6:
            if initializeLevel:
                all_floors = pygame.sprite.Group()
                all_enemey1 = pygame.sprite.Group()
                all_enemey2 = pygame.sprite.Group()
                all_dynamite = pygame.sprite.Group()
                all_finish = pygame.sprite.Group()

                breath = 10 #10 air bubbles, lose one every ~10-12 seconds 
                startTime = pygame.time.get_ticks() #in milliseconds

                playerSpeed = 2
                step = 0
                stepX = 0
                for i, row in enumerate(levelMap6):
                    currentY = (step * 32)
                    if (i+1) % 28 == 0: 
                        step = 0
                        stepX +=1
                    else:
                        step+=1
                    for j, block in enumerate(row):
                        currentX = stepX*704+(j*32)
                        if block == 'b':
                            new_floor = Level6FloorBlock(currentX, currentY)
                            all_floors.add(new_floor)
                        if block == 'p':
                            player = Level6Player(currentX, currentY)
                        if block == '1':
                            new_e = Level6Enemy1(currentX, currentY)
                            all_enemey1.add(new_e)
                        if block == '2':
                            new_e = Level6Enemy2(currentX, currentY)
                            all_enemey2.add(new_e)
                        if block == 'd':
                            new_d = Level6Dynamite(currentX, currentY)
                            all_dynamite.add(new_d)
                        if block == 'f':
                            new_f = Level6Finish(currentX, currentY)
                            all_finish.add(new_f)
                        
                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            old_x, old_y = player.rect.x, player.rect.y
            if keys[pygame.K_a]:
                player.rect.x -= playerSpeed
                playerDirection = 1
            if keys[pygame.K_d]:
                player.rect.x += playerSpeed
                playerDirection = 1
            

            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.x = old_x

            if keys[pygame.K_w]:
                player.rect.y -= playerSpeed+1
                playerDirection = 1
            if keys[pygame.K_s]:
                player.rect.y += playerSpeed
                playerDirection = 1
            elif not keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                player.rect.y += playerSpeed-1
                playerDirection = 0

            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.y = old_y

            if player.rect.x <= 335:
                direction = 1
                player.rect.x += 1
            elif player.rect.x >= 375:
                direction = -1
                player.rect.x -= 1
            else:
                direction = 0

            if not pygame.sprite.spritecollide(player, all_floors, False):
                all_floors.update(player.rect.x, playerSpeed, direction)
                all_enemey2.update(player.rect.x, playerSpeed, direction)
                all_dynamite.update(player.rect.x, playerSpeed, direction)
                all_finish.update(player.rect.x, playerSpeed, direction)
            else:
                player.rect.x += direction+5
            
            currentTime = pygame.time.get_ticks() #in milliseconds
            if currentTime - startTime >= 10000: #every 10 seconds
                breath -= 1 
                print(breath)
                startTime = currentTime

            if (breath <= 0 or pygame.sprite.spritecollide(player, all_enemey1, False) or   
                pygame.sprite.spritecollide(player, all_enemey2, False) or 
                pygame.sprite.spritecollide(player, all_dynamite, False)):
                
                levelActive = False
                initializeLevel = True
                displayMine = True

            if pygame.sprite.spritecollide(player, all_finish, False):
                levelActive = False
                initializeLevel = True
                levelSelect[6]['completed'] = True
                displayMine = True

            for enemey in all_enemey2:
                if pygame.sprite.spritecollide(enemey, all_floors, False):
                    enemey.collidedWall = True

            player.update(playerDirection)
            all_enemey1.update(playerSpeed, direction)
            
            DISPLAYSURF.blit(level6Background , (0,0))
            DISPLAYSURF.blit(player.image, player.rect)
            all_floors.draw(DISPLAYSURF)
            all_enemey1.draw(DISPLAYSURF)
            all_enemey2.draw(DISPLAYSURF)
            all_dynamite.draw(DISPLAYSURF)
            all_finish.draw(DISPLAYSURF)

            for i in range(breath):
                DISPLAYSURF.blit(airBubble, (280+i*17,825,16,16))

            pygame.display.flip()

        #level 8, a puzzle
        if currentLevel == 7:
            if initializeLevel: 
                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if mouse_pressed[0]: #Level failed
                levelActive = False
                initializeLevel = True
                displayMine = True
            if mouse_pressed[2]: #Level Completed
                levelActive = False
                initializeLevel = True
                levelSelect[3]['completed'] = True
                displayMine = True

            DISPLAYSURF.blit(background,(0,0))
            pygame.display.flip()

        #level 9, Waves of enemies coming from both left and right and you need to defeat them all
        if currentLevel == 8:
            if initializeLevel:

                player = Level8Player(350,468)
                floor = Level8Floor(-50,500)
                all_enemy1 = pygame.sprite.Group()
                all_enemy2 = pygame.sprite.Group()
                all_enemy = pygame.sprite.Group()
                playerSpeed = 3
                spawnLevelY = 500

                currentX = 0
                for item in levelMap8[0]: #enemies that come from the left
                    if item == 'a': #enemy type
                        e = Level8Enemy1(CurrentX, spawnLevelY)
                        all_enemey1.add(e)
                        all_enemy.add(e)
                    elif item == 'b': #enemey type
                        e = Level8Enemy2(CurrentX, spawnLevelY)
                        all_enemey2.add(e)
                        all_enemy.add(e)
                    else: #number representing amount of space of 32 pixels to add
                        currentX -= int(item) * 32

                currentX = 720
                for item in levelMap8[1]: #enemies that come from the right
                    if item == 'a': #enemy type
                        e = Level8Enemy1(CurrentX, spawnLevelY)
                        all_enemey1.add(e)
                        all_enemy.add(e)
                    elif item == 'b': #enemey type
                        e = Level8Enemy2(CurrentX, spawnLevelY)
                        all_enemey2.add(e)
                        all_enemy.add(e)
                    else: #number representing amount of space of 32 pixels to add
                        currentX += int(item) * 32
                
                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.rect.x >= 8:
                player.rect.x -= playerSpeed
                player.direction = 1
            if keys[pygame.K_d] and player.rect.x <= 680:
                player.rect.x += playerSpeed
                player.direction = 2

            if mouse_pressed[0]: #Level failed
                levelActive = False
                initializeLevel = True
                displayMine = True
            if mouse_pressed[2]: #Level Completed
                levelActive = False
                initializeLevel = True
                levelSelect[3]['completed'] = True
                displayMine = True

            player.update()
            all_enemy.update(player.rect.x)

            DISPLAYSURF.blit(background,(0,0))
            all_enemy.draw(DISPLAYSURF)
            DISPLAYSURF.blit(player.image, player.rect)
            DISPLAYSURF.blit(floor.image, floor.rect)

            pygame.display.flip()

        #level 10, an upscrolling and side scrolling escape, avoid getting stuck
        if currentLevel == 9:
            if initializeLevel: 

                scrollSpeed = 1
                level10StopScrolling = False
                gravity = 6

                all_backgrounds = pygame.sprite.Group()
                all_floors = pygame.sprite.Group()
                bottom_floors = pygame.sprite.Group()

                offset = 0
                for i, row in enumerate(levelMap9):
                    currentY = (i * 32)  - 900*((len(levelMap9)-28)/28)
                    for j, block in enumerate(row):
                        currentX = 8+ (j * 32)
                        if block == 'p':
                            player = PlayerLevel10(currentX,currentY)
                        if block == 'b':
                            new_floor = floorBlockLevel10(currentX, currentY)
                            all_floors.add(new_floor)
                        if block == 'e':
                            new_floor = topFloorBlockLevel10(currentX, currentY)
                            bottom_floors.add(new_floor)
                        if block == 'f':
                            finish = FinishBlockLevel10(currentX, currentY)

                
                background1 = Level10Background(0,0)
                background2 = Level10Background(0,-900)
                background3 = Level10Background(0,-1800)
                background4 = Level10Background(0,-2700)
                all_backgrounds.add(background1, background2, background3, background4)

                lava = LavaLevel10(0,880)

                initializeLevel = False

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            old_x, old_y = player.rect.x, player.rect.y
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and player.rect.x >= 8:
                player.rect.x -= 3
                player.direction = 1
            if keys[pygame.K_d] and player.rect.x <= 680:
                player.rect.x += 3
                player.direction = 2
            if pygame.sprite.spritecollide(player, all_floors, False):
                player.rect.x = old_x

            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                player.direction = 0

            player.rect.y += gravity
            if keys[pygame.K_SPACE] and player.isGrounded and player.isJumping == False:
                player.isJumping = True
                player.isGrounded = False 
                player.startingY = player.rect.y

            collisions = pygame.sprite.spritecollide(player, all_floors, False)
            if collisions:
                if not player.isJumping:
                    player.rect.bottom = collisions[0].rect.top
                    player.isGrounded = True
                if player.isJumping and player.rect.y <= player.startingY-32:
                    player.isJumping = False

            collisions = pygame.sprite.spritecollide(player, bottom_floors, False)
            if collisions:
                if not player.isJumping:
                    player.rect.bottom = collisions[0].rect.top
                    player.isGrounded = True
                if player.isJumping and player.rect.y <= player.startingY-32:
                    player.isJumping = False
            

            if  pygame.sprite.collide_rect(player, lava):
                levelActive = False
                initializeLevel = True
                displayMine = True

            if pygame.sprite.collide_rect(player, finish):
                levelActive = False
                initializeLevel = True
                levelSelect[9]['completed'] = True
                displayMine = True


            player.update()
            finish.update(scrollSpeed)
            bottom_floors.update(scrollSpeed)
            lava.update(scrollSpeed)

            if level10StopScrolling == False:
                all_backgrounds.update(scrollSpeed)
                all_floors.update(scrollSpeed)
            else:
                lava.topOut = True
            


            all_backgrounds.draw(DISPLAYSURF)
            pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,8,900))
            pygame.draw.rect(DISPLAYSURF, BLACK, (712,0,8,900))
            all_floors.draw(DISPLAYSURF)
            bottom_floors.draw(DISPLAYSURF)
            DISPLAYSURF.blit(player.image, player.rect)
            DISPLAYSURF.blit(finish.image,finish.rect)
            DISPLAYSURF.blit(lava.image,lava.rect)

            pygame.display.flip()