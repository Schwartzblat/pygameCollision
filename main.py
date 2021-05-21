import pygame
import threading


def loop():
    def isCollisionSquares(square1X, square2X):
        distance = square1X - square2X
        if distance <= 50.0:
            return True
        else:
            return False

    def isCollisionLine(squareX):
        if squareX <= 5:
            return True
        return False

    global running
    while running:
        global aX, bX, counter, aSpeed, bSpeed
        if isCollisionSquares(aX, bX):
            counter += 1
            temp = aSpeed
            aSpeed = (aSpeed * (mA - mB) + 2 * mB * bSpeed) / (mB + mA)
            bSpeed = (mA * temp + mB * bSpeed - mA * aSpeed) / mB
            # print(counter)

        if isCollisionLine(aX):
            aSpeed = -aSpeed
            print("fuck")
        if isCollisionLine(bX):
            counter += 1
            bSpeed = -bSpeed
        aX += aSpeed
        bX += bSpeed


def value(X, Y, num):
    over_text = font.render("Collisions:   "+str(int(num)), True, (255, 255, 255))
    screen.blit(over_text, (X, Y))

def showText(x,y,string):
    over_text = font1.render(string, True, (255, 255, 255))
    screen.blit(over_text, (x, y))

pygame.init()
screen = pygame.display.set_mode((1500, 800))
font = pygame.font.Font("freesansbold.ttf", 30)
font1 = pygame.font.Font("freesansbold.ttf", 25)

pygame.display.set_caption("The Game")
aX = 800
bX = 280
mA = 10000000000  # kg
mB = 1  # kg
aSpeed = -0.0001
bSpeed = 0
counter = 0
running = True
#threading.Thread(target=loop).start()
while running:
    screen.fill((0, 0, 0))
    line = pygame.draw.line(screen, (255, 255, 255), (5, 0), (5, 1000))
    pygame.draw.line(screen, (255, 255, 255), (0, 500), (1500, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(counter)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                threading.Thread(target=loop).start()

    a = pygame.draw.rect(screen, (0, 0, 180), (aX, 350, 150, 150))
    showText(aX+20, 320, "10^10 Kg")
    b = pygame.draw.rect(screen, (0, 100, 180), (bX, 450, 50, 50))
    showText(bX, 420, "1 Kg")
    value(800, 20, counter)
    pygame.display.update()
