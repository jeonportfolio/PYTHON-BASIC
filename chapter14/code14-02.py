import pygame
import random
import sys


def paintEntity(entity, x, y) :
   monitor.blit(entity, (int(x), int(y)))

def writeScore(score) :
    myfont = pygame.font.Font('chapter14/img/NanumGothic.ttf', 20)     
    txt = myfont.render(u'파괴한 우주괴물 수 : ' + str(score), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (10, sheight - 40))

def playGame() :
    global monitor, ship, monster, misile

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256) 
    
     
    shipX = swidth / 2 
    shipY = sheight * 0.8
    dx, dy = 0, 0 

    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size                
    monsterX = 0 
    monsterY = random.randrange(0, int(swidth * 0.3))
    monsterSpeed = random.randrange(1, 5)

    missileX, missileY = None, None

    fireCount = 0
   
    while True :
        (pygame.time.Clock()).tick(50)  
        monitor.fill((r, g, b))              

       
        for e in pygame.event.get() :
            if e.type in [pygame.QUIT]  :
                pygame.quit()
                sys.exit()

       
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT : dx = +5
                elif e.key == pygame.K_UP : dy = -5
                elif e.key == pygame.K_DOWN : dy = +5

                elif e.key == pygame.K_SPACE : 
                    if missileX == None :                   
                        missileX = shipX + shipSize[0]/2  
                        missileY = shipY

            if e.type in [pygame.KEYUP] :
                 if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx, dy = 0, 0

    
        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
            and (sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]) :  
            shipX += dx
            shipY += dy
        paintEntity(ship, shipX, shipY)   

        monsterX += monsterSpeed
        if monsterX > swidth :
            monsterX = 0
            monsterY = random.randrange(0, int(swidth * 0.3))
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1, 5)
           
        paintEntity(monster, monsterX, monsterY)

        if missileX != None :                         
            missileY -= 10
            if missileY < 0 :
                  missileX, missileY = None, None  
        if missileX != None :          
            paintEntity(missile, missileX, missileY)

            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                   (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                fireCount += 1

                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterX = 0
                monsterY =random.randrange(0, int(swidth * 0.3))
                monsterSpeed = random.randrange(1, 5)
                            
                missileX, missileY= None, None  

        writeScore(fireCount)

        pygame.display.update()

r, g, b = [0] * 3               
swidth, sheight = 500, 700  
monitor = None               
ship, shipSize = None, 0   

monsterImage = ['chapter14/img/monster01.png', 'chapter14/img/monster02.png', 'chapter14/img/monster03.png', 'chapter14/img/monster04.png', \
                'chapter14/img/monster05.png', 'chapter14/img/monster06.png', 'chapter14/img/monster07.png', 'chapter14/img/monster08.png', \
                'chapter14/img/monster09.png', 'chapter14/img/monster10.png']
monster = None 

missile = None


pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship = pygame.image.load('chapter14/img/ship02.png')
shipSize = ship.get_rect().size

missile = pygame.image.load('chapter14/img/missile.png')



playGame()
