import pygame
import sys
import os
#from SpiderInit import init_spider
#from ServoControll import *
#from SpiderBot import *

class MainLoop():
    def __init__(self):
        self.forward = False
        self.backwards = False
        self.left = False
        self.right = False
        self.x = 0
        self.y = 0
        
        #self.start()
    #def update(self):
    #    self.posx = +1
    def forward_action(self):        
        print("forward")   
        
    def start_spider(self):
        self.spider = SpiderMoves()

pygame.init()
main = True
loop = MainLoop()


while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                loop.forward_action()