from smbus2 import SMBus
from smbus2 import SMBusWrapper
from Leg import Leg
from ServoControll import initialize, move_angle
import time

chip_addr = 0x40

class PairOfLegs():

    def __init__(self, start_addr, stop_addr):

        self.angle = 0
        self.start_addr = start_addr[0]
        self.stop_addr = stop_addr[0]              
        self.min = -44
        self.max = 44
        self.mode = 1
        self.modes = []
        self.last = 0

        initialize(self.start_addr, self.stop_addr)


        self.lleg = Leg('left', start_addr[1], stop_addr[1])
        self.rleg = Leg('right', start_addr[2], stop_addr[2])
        
    def calibrate(self):        

        # if(self.lleg.angle <= abs(self.angle)):
        #     self.lleg.lock = False
        # if(self.rleg.angle <= abs(self.angle)):
        #     self.rleg.lock = False
        while((abs(self.angle) > self.lleg.angle and self.lleg.angle > 0) or (abs(self.angle) > self.rleg.angle and self.rleg.angle > 0)):
                if(self.angle != 0):
                    self.angle = self.angle + (0-self.angle)/abs(self.angle)
                    move_angle(self.angle, self.stop_addr)
                    time.sleep(.01)
                    # if(self.lleg.angle + self.rleg.angle == 0):
                    #     self.rleg.lock = True
                    #     self.lleg.lock = True

        while(self.angle != 0 or self.lleg.angle != 0 or  self.rleg.angle != 0):
            #while((self.angle > self.lleg.angle and self.lleg.angle > 0) or (self.angle > self.rleg.angle and self.rleg.angle > 0)):
            if(self.angle != 0):
                self.angle = self.angle + (0-self.angle)/abs(self.angle)
            if(self.lleg.angle + self.rleg.angle == 0):
                self.rleg.lock = True
                self.lleg.lock = True
            if(self.lleg.angle != 0 and self.lleg.lock):
                self.lleg.calibrate()
            if(self.rleg.angle != 0 and self.rleg.lock):
                self.rleg.calibrate()
            time.sleep(.01)
            #move_angle(self.addr)
            #print('p: {}, l: {}, r: {}'.format(self.angle, self.lleg.angle, self.rleg.angle))
            self.last = 0
    
    def move(self, mode):  
        
        if(self.lleg.lock):
            self.lleg.move(self.last, mode)

        if(self.rleg.lock):
            self.rleg.move(self.last, mode)

        self.angle = self.angle + self.modes[self.last]
        
        move_angle(self.angle, self.stop_addr)   
        
        if(self.angle >= self.max):            
            self.last = 1            
        elif(self.angle <= self.min):
            self.last = 3
        elif(self.angle == 0 and self.last == 1):
            self.last = 2            
        elif(self.angle == 0 and self.last == 3):
            self.last = 4
        elif(abs(self.angle) == 22 and self.last == 0):
            self.last = 5

        if(self.last == 2 or self.last == 4 or self.last == 5):
            
            if(self.lleg.angle + self.rleg.angle == 0):
                self.rleg.lock = True
                self.lleg.lock = True        
        
    def move_up(self, mode):
        
        self.lleg.move(self.last, self.lleg.mode)
        move_angle(self.lleg.angle, self.lleg.stop_addr)
        self.rleg.move(self.last, self.rleg.mode)
        move_angle(self.rleg.angle, self.rleg.stop_addr)
        self.angle = self.angle + self.modes[self.last]
        move_angle(self.angle, self.stop_addr)
        time.sleep(.3)
        if(abs(self.angle) == 22 and self.last == 0):
            self.last = 5
