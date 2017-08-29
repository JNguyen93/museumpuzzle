# Museum Puzzle
# By Justin Nguyen
# For use by Texas Panic Room
import pygame, sys, random
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 680
WINDOWHEIGHT = 680
BORDERTHICK = 3
LINETHICK = 5

#            R    G    B		
GRAY     = (100, 100, 100)		
NAVYBLUE = ( 60,  60, 100)		
WHITE    = (255, 255, 255)		
RED      = (255,   0,   0)		
GREEN    = (  0, 255,   0)		
BLUE     = (  0,   0, 255)		
YELLOW   = (255, 255,   0)		
ORANGE   = (255, 128,   0)		
PURPLE   = (255,   0, 255)		
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

COLORS = [WHITE, BLUE, YELLOW, GREEN, RED, BLACK]

bg = "Mondrian-I-Pi.png"
bgimg = pygame.image.load(bg)
vic = "Mondrian-Map.png"
vicimg = pygame.image.load(vic)
rects = []
resets = []
mondrians = []
resetMondrians = []
blacks = [0, 10, 13, 20, 21, 24]
blues = [3, 5, 11, 17, 29, 38]
reds = [9, 15, 18, 27, 28, 32, 34]
yellows = [2, 8, 23, 26, 31, 36]
changed = False
win = False
cheatFlag = False

class Mondrian:
    
    def __init__(self, rect, num, sol = None):
        self.rect = rect
        self.num = num
        self.counter = random.randint(0, len(COLORS) - 2)
        
        if sol is None:
            self.sol = 0
        else:
            self.sol = sol
            
        if self.counter == self.sol:
            self.correct = True
        else:
            self.correct = False

    def changeColor(self):
        if self.counter >= len(COLORS) - 1:
            self.counter = 0
        else:
            self.counter += 1

    def getNum(self):
        return self.num
    
    def getSol(self):
        return self.sol

    def randomizeColor(self):
        self.counter = random.randint(0, len(COLORS) - 2)
    
    def getColor(self):
        return COLORS[self.counter]

    def checkCorrect(self):
        if self.counter == self.sol:
            self.correct = True
        else:
            self.correct = False
        return self.correct

    def setCorrect(self, flag):
        self.correct = flag

    def getCorrect(self):
        return self.correct

def changeMondrianColor(moux, mouy):
    for z in mondrians:
        if z.rect.collidepoint(moux, mouy):
            z.changeColor()
            return z
    return None

def checkWin():
    for x in mondrians:
        if not x.checkCorrect():
            return False
    return True

def resetCheck(moux, mouy):
    for i in resetMondrians:
        if i.rect.collidepoint(moux, mouy):
            i.setCorrect(True)
            #i.changeColor()
    if resetMondrians[0].getCorrect() and resetMondrians[1].getCorrect() and resetMondrians[2].getCorrect() and resetMondrians[3].getCorrect():
        return True
    else:
        return False

def reset():
    global win, cheatFlag, changed
    win = False
    cheatFlag = False
    changed = False
    
    DISPLAYSURF.blit(bgimg, (0, 0))

    for y in mondrians:
        y.randomizeColor()
        pygame.draw.rect(DISPLAYSURF, y.getColor(), y.rect)

    for i in resetMondrians:
        i.setCorrect(False)
    
    pygame.display.update()

def main():
    global FPSCLOCK, DISPLAYSURF
    global cheatFlag, win, changed
    global mondrians, resetMondrians
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Museum Puzzle')

    DISPLAYSURF.blit(bgimg, (0, 0))
    
    #Column 1
    Rect0 = pygame.Rect(0 + BORDERTHICK, 0 + BORDERTHICK, 43 - LINETHICK, 185 - LINETHICK)
    Rect1 = pygame.Rect(0 + BORDERTHICK, 183 + LINETHICK, 43 - LINETHICK, 290 - LINETHICK)
    Rect2 = pygame.Rect(0 + BORDERTHICK, 472 + LINETHICK, 43 - LINETHICK, 141 - LINETHICK)
    Rect3 = pygame.Rect(0 + BORDERTHICK, 613 + LINETHICK, 162 - LINETHICK, 64 - LINETHICK)
    #Column 2
    Rect4 = pygame.Rect(43 + BORDERTHICK, 0 + BORDERTHICK, 119 - LINETHICK, 43 - LINETHICK)
    Rect5 = pygame.Rect(43 + BORDERTHICK, 43 + BORDERTHICK, 119 - LINETHICK, 86 - LINETHICK)
    Rect6 = pygame.Rect(43 + BORDERTHICK, 129 + BORDERTHICK, 83 - LINETHICK, 125 - LINETHICK)
    Rect7 = pygame.Rect(43 + BORDERTHICK, 254 + BORDERTHICK, 83 - LINETHICK, 220 - LINETHICK)
    Rect8 = pygame.Rect(43 + BORDERTHICK, 474 + BORDERTHICK, 83 - LINETHICK, 141 - LINETHICK)
    #Column 3
    Rect9 = pygame.Rect(125 + BORDERTHICK, 129 + BORDERTHICK, 37 - LINETHICK, 486 - LINETHICK)
    #Column 4
    Rect10 = pygame.Rect(162 + BORDERTHICK, 0 + BORDERTHICK, 136 - LINETHICK, 43 - LINETHICK)
    Rect11 = pygame.Rect(162 + BORDERTHICK, 43 + BORDERTHICK, 136 - LINETHICK, 86 - LINETHICK)
    Rect12 = pygame.Rect(161 + BORDERTHICK, 129 + BORDERTHICK, 106 - LINETHICK, 201 - LINETHICK)
    Rect13 = pygame.Rect(161 + BORDERTHICK, 330 + BORDERTHICK, 39 - LINETHICK, 90 - LINETHICK)
    Rect14 = pygame.Rect(161 + BORDERTHICK, 420 + BORDERTHICK, 38 - LINETHICK, 259 - LINETHICK)
    #Column 5
    Rect15 = pygame.Rect(265 + BORDERTHICK, 129 + BORDERTHICK, 34 - LINETHICK, 201 - LINETHICK)
    Rect16 = pygame.Rect(199 + BORDERTHICK, 330 + BORDERTHICK, 99 - LINETHICK, 90 - LINETHICK)
    Rect17 = pygame.Rect(199 + BORDERTHICK, 420 + BORDERTHICK, 171 - LINETHICK, 148 - LINETHICK)
    Rect18 = pygame.Rect(199 + BORDERTHICK, 568 + BORDERTHICK, 99 - LINETHICK, 111 - LINETHICK)
    #Column 6
    Rect19 = pygame.Rect(43 + 119 + 136 + BORDERTHICK, 0 + BORDERTHICK, 299 - LINETHICK, 43 - LINETHICK)
    Rect20 = pygame.Rect(43 + 119 + 136 + BORDERTHICK, 43 + BORDERTHICK, 111 - LINETHICK, 86 - LINETHICK)
    Rect21 = pygame.Rect(43 + 119 + 136 + BORDERTHICK, 129 + BORDERTHICK, 110 - LINETHICK, 42 - LINETHICK)
    Rect22 = pygame.Rect(43 + 119 + 136 + BORDERTHICK, 171 + BORDERTHICK, 110 - LINETHICK, 159 - LINETHICK)
    Rect23 = pygame.Rect(43 + 119 + 136 + BORDERTHICK, 330 + BORDERTHICK, 110 - LINETHICK, 90 - LINETHICK)
    Rect24 = pygame.Rect(199 + 171 + BORDERTHICK, 420 + BORDERTHICK, 120 - LINETHICK, 148 - LINETHICK)
    Rect25 = pygame.Rect(43 + 119 + 136 + BORDERTHICK, 568 + BORDERTHICK, 192 - LINETHICK, 111 - LINETHICK)
    #Column 7
    Rect26 = pygame.Rect(43 + 119 + 136 + 110 + BORDERTHICK, 43 + BORDERTHICK, 189 - LINETHICK, 87 - LINETHICK)
    Rect27 = pygame.Rect(43 + 119 + 136 + 110 + BORDERTHICK, 129 + BORDERTHICK, 142 - LINETHICK, 107 - LINETHICK)
    Rect28 = pygame.Rect(43 + 119 + 136 + 110 + BORDERTHICK, 236 + BORDERTHICK, 142 - LINETHICK, 94 - LINETHICK)
    Rect29 = pygame.Rect(43 + 119 + 136 + 110 + BORDERTHICK, 330 + BORDERTHICK, 142 - LINETHICK, 90 - LINETHICK)
    Rect30 = pygame.Rect(199 + 171 + 120 + BORDERTHICK, 420 + BORDERTHICK, 60 - LINETHICK, 148 - LINETHICK)
    Rect31 = pygame.Rect(199 + 171 + 120 + BORDERTHICK, 568 + BORDERTHICK, 189 - LINETHICK, 111 - LINETHICK)
    #Column 8
    Rect32 = pygame.Rect(43 + 119 + 136 + 110 + 142 + BORDERTHICK, 129 + BORDERTHICK, 47 - LINETHICK, 201 - LINETHICK)
    Rect33 = pygame.Rect(43 + 119 + 136 + 110 + 142 + BORDERTHICK, 330 + BORDERTHICK, 47 - LINETHICK, 90 - LINETHICK)
    Rect34 = pygame.Rect(43 + 119 + 136 + 110 + 142 + BORDERTHICK, 420 + BORDERTHICK, 47 - LINETHICK, 148 - LINETHICK)
    #Column 9
    Rect35 = pygame.Rect(43 + 119 + 136 + 299 + BORDERTHICK, 0 + BORDERTHICK, 43 - LINETHICK, 330 - LINETHICK)
    Rect36 = pygame.Rect(43 + 119 + 136 + 299 + BORDERTHICK, 330 + BORDERTHICK, 82 - LINETHICK, 90 - LINETHICK)
    Rect37 = pygame.Rect(43 + 119 + 136 + 299 + BORDERTHICK, 420 + BORDERTHICK, 82 - LINETHICK, 148 - LINETHICK)
    #Column 10
    Rect38 = pygame.Rect(43 + 119 + 136 + 299 + 43 + BORDERTHICK, 0 + BORDERTHICK, 39 - LINETHICK, 330 - LINETHICK)

    Reset0 = pygame.Rect(71, 135, 54, 47)
    Reset1 = pygame.Rect(126, 182, 55, 49)
    Reset2 = pygame.Rect(181, 231, 57, 49)
    Reset3 = pygame.Rect(238, 280, 57, 49)

    resets = [Reset0, Reset1, Reset2, Reset3]
    
    rects = [Rect0, Rect1, Rect2, Rect3, Rect4, Rect5, Rect6, Rect7, Rect8, Rect9, Rect10,
             Rect11, Rect12, Rect13, Rect14, Rect15, Rect16, Rect17, Rect18, Rect19, Rect20,
             Rect21, Rect22, Rect23, Rect24, Rect25, Rect26, Rect27, Rect28, Rect29, Rect30,
             Rect31, Rect32, Rect33, Rect34, Rect35, Rect36, Rect37, Rect38]

    #0,2,3,5,8,9,10,11,13,15,17,18,20,21,23,24,26,27,28,29,31,32,34,36,38
    #Black = 5: 0,10,13,20,21,24
    #Blue = 1: 3,5,11,17,29,38
    #Red = 4: 9,15,18,27,28,32,34
    #Yellow = 2: 2,8,23,26,31,36
    
    for x in range(0, 39):
        if x in blacks:
            mondrians.append(Mondrian(rects[x], x, 5))
        elif x in blues:
            mondrians.append(Mondrian(rects[x], x, 1))
        elif x in reds:
            mondrians.append(Mondrian(rects[x], x, 4))
        elif x in yellows:
            mondrians.append(Mondrian(rects[x], x, 2))
        else:
            mondrians.append(Mondrian(rects[x], x))

    for a in range(0, len(resets)):
        resetMondrians.append(Mondrian(resets[a], a))
    
    for y in mondrians:
        pygame.draw.rect(DISPLAYSURF, y.getColor(), y.rect)
    
    pygame.display.update()

    while True:
        for event in pygame.event.get(): # event handling loop
            mouseClicked = False
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):		
                pygame.quit()		
                sys.exit()		
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos		
            elif event.type == MOUSEBUTTONUP:		
                mousex, mousey = event.pos
                mouseClicked = True
            elif event.type == KEYUP and event.key == K_j:
                cheatFlag = True
            if mouseClicked and not win:
                changedMondrian = changeMondrianColor(mousex, mousey)
                if changedMondrian is None:
                    changed = False
                else:
                    changed = True
            elif mouseClicked and win:
                resetFlag = resetCheck(mousex, mousey)
                if resetFlag:
                    reset()
        
        if changed:
            pygame.draw.rect(DISPLAYSURF, changedMondrian.getColor(), changedMondrian.rect)
            changed = False
        
        if checkWin() or cheatFlag:
            for i in resetMondrians:
                pygame.draw.rect(DISPLAYSURF, i.getColor(), i.rect)
            DISPLAYSURF.blit(vicimg, (0, 0))
            win = True

        pygame.display.update()
                
if __name__ == '__main__':
    main()
