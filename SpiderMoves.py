from smbus2 import SMBus
from smbus2 import SMBusWrapper
from PairOfLegs import PairOfLegs
from ServoControll import *
import time

class SpiderMoves():
    def __init__(self):            
            
        self.x = PairOfLegs([0x06, 0x0A, 0x0E], [0x08, 0x0C, 0x10])
        self.y = PairOfLegs([0x16, 0x1A, 0x1E], [0x18, 0x1C, 0x20])
        self.z = PairOfLegs([0x26, 0x2A, 0x2E], [0x28, 0x2C, 0x30])    
      
    def calibrate(self):

        self.x.calibrate()
        self.y.calibrate()
        self.z.calibrate()
        print('x: {} {} {}, y: {} {} {}, z: {} {} {}'.format(self.x.angle, self.x.lleg.angle, self.x.rleg.angle,self.y.angle,self.y.lleg.angle, self.y.rleg.angle,self.z.angle,self.z.lleg.angle, self.z.rleg.angle))        
            
    def recalibrate(self, up_down):
        if self.x.lleg.point_zero >= 260 and self.x.lleg.point_zero <= 290:
            move_angle(self.x.lleg.point_zero, self.x.lleg.angle + up_down*5, self.x.lleg.stop_addr)
            move_angle(self.x.rleg.point_zero, self.x.rleg.angle + up_down*5, self.x.rleg.stop_addr)
            move_angle(self.y.lleg.point_zero, self.y.lleg.angle + up_down*5, self.y.lleg.stop_addr)
            move_angle(self.y.rleg.point_zero, self.y.rleg.angle + up_down*5, self.y.rleg.stop_addr)
            move_angle(self.z.lleg.point_zero, self.z.lleg.angle + up_down*5, self.z.lleg.stop_addr)
            move_angle(self.z.rleg.point_zero, self.z.rleg.angle + up_down*5, self.z.rleg.stop_addr)
            self.x.lleg.point_zero = self.x.lleg.point_zero + up_down*5
            self.x.rleg.point_zero = self.x.rleg.point_zero + up_down*5
            self.y.lleg.point_zero = self.y.lleg.point_zero + up_down*5
            self.y.rleg.point_zero = self.y.rleg.point_zero + up_down*5
            self.z.lleg.point_zero = self.z.lleg.point_zero + up_down*5
            self.z.rleg.point_zero = self.z.rleg.point_zero + up_down*5     
        
    
    def move_forward(self):

        self.x.modes = [1, -1, -1, 1, 1, 1, 0]
        self.y.modes = [-1, -1, -1, 1, 1, -1, 0]
        self.z.modes = [1, -1, -1, 1, 1, 1, 0]
                
        self.x.move(1, 1)
        self.y.move(-1, 1)
        self.z.move(1, 1)
        
        #print('x: {} {} {}, y: {} {} {}, z: {} {} {}'.format(self.x.angle, self.x.lleg.angle, self.x.rleg.angle,self.y.angle,self.y.lleg.angle, self.y.rleg.angle,self.z.angle,self.z.lleg.angle, self.z.rleg.angle))
                
    def move_backwards(self):

        self.x.modes = [-1, -1, -1, 1, 1, -1, 0]
        self.y.modes = [1, -1, -1, 1, 1, 1, 0]
        self.z.modes = [-1, -1, -1, 1, 1, -1, 0]
        
        self.x.move(1, -1)
        self.y.move(-1, -1)
        self.z.move(1, -1)
       
        #print('x: {} {} {}, y: {} {} {}, z: {} {} {}'.format(self.x.angle, self.x.lleg.angle, self.x.rleg.angle,self.y.angle,self.y.lleg.angle, self.y.rleg.angle,self.z.angle,self.z.lleg.angle, self.z.rleg.angle))
   
    def turn_left(self):
        
        self.x.modes = [-1, -1, -1, 1, 1, -1, 0]
        self.y.modes = [-1, -1, -1, 1, 1, -1, 0]
        self.z.modes = [-1, -1, -1, 1, 1, -1, 0]

        while(self.x.angle != self.x.min):
            self.x.move_up(-1)           

        while(self.y.angle != self.y.min):
            self.y.move_up(-1)      

        while(self.z.angle != self.z.min):
            self.z.move_up(-1)

        self.move_down()


    def turn_right(self):

        self.x.modes = [1, -1, -1, 1, 1, 1, 0]
        self.y.modes = [1, -1, -1, 1, 1, 1, 0]
        self.z.modes = [1, -1, -1, 1, 1, 1, 0]

        while(self.x.angle != self.x.max):
            self.x.move_up(1)

        while(self.y.angle != self.y.max):
            self.y.move_up(1)
            
        while(self.z.angle != self.z.max):
            self.z.move_up(1)

        self.move_down()
        
    def move_down(self):

        self.x.lleg.angle = self.x.lleg.min
        move_angle(self.x.lleg.angle, self.x.lleg.stop_addr)
        self.x.rleg.angle = self.x.rleg.min
        move_angle(self.x.rleg.angle, self.x.rleg.stop_addr)
        self.y.lleg.angle = self.y.lleg.min
        move_angle(self.y.lleg.angle, self.y.lleg.stop_addr)
        self.y.rleg.angle = self.y.rleg.min
        move_angle(self.y.rleg.angle, self.y.rleg.stop_addr)
        self.z.lleg.angle = self.z.lleg.min
        move_angle(self.z.lleg.angle, self.z.lleg.stop_addr)
        self.z.rleg.angle = self.z.rleg.min
        move_angle(self.z.rleg.angle, self.z.rleg.stop_addr)

        self.calibrate()