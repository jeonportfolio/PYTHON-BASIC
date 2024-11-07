from myTurtle import *
import turtle
import random  

inStr = ''
swidth, sheight = 300, 300
tX, tY, tAngle, txtSize = [0] * 4

def getXYAS(sw, sh):
    x = random.randrange(int(-sw / 2), int(sw / 2))
    y = random.randrange(int(-sh / 2), int(sh / 2))
    angle = random.randrange(0, 360)  # 각도
    size = random.randint(10, 30)  # 텍스트 크기
    return x, y, angle, size

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()  

for ch in inStr:
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight)
    r, g, b = getRGB()  

    turtle.goto(tX, tY)
    turtle.left(tAngle)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

turtle.done()
