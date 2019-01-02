import pygame
import SpiderMoves
from SpiderInit import spider_init
from ServoControll import reset_servos

pygame.init()
spider_init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("SpiderBot")
SMoves = SpiderMoves.SpiderMoves()
x = 200
y = 200
point_zero = 200
width = 40
height = 60
vel = 5
run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            reset_servos()
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                SMoves.calibrate()
                y = point_zero
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        SMoves.move_forward()
        y -= vel
    if keys[pygame.K_DOWN]:
        SMoves.move_backwards()
        y += vel
#    if keys[pygame.K_LEFT]:
#        SMoves        
#    if keys[pygame.K_RIGHT]:
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()
            
pygame.quit()