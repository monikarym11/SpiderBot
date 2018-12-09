from smbus2 import SMBus
from smbus2 import SMBusWrapper
from PairOfLegs import PairOfLegs
from ServoControll import *
import time

#chip_addr = 0x40

class SpiderMoves():
    def __init__(self):            
        
        self.x = PairOfLegs([0x06, 0x0A, 0x0E], [0x08, 0x0C, 0x10])
        self.y = PairOfLegs([0x12, 0x16, 0x1A], [0x14, 0x18, 0x1C])
        self.z = PairOfLegs([0x1E, 0x22, 0x26], [0x20, 0x24, 0x28])

        self.calibrate()
        
        with SMBusWrapper(1) as bus:
            bus.write_byte_data(chip_addr, 0, 0x20) # enable the chip
            time.sleep(.25)
            bus.write_byte_data(chip_addr, 0, 0x10) # enable Prescale change as noted in the datasheet
            time.sleep(.25) # delay for reset
            bus.write_byte_data(chip_addr, 0xfe, 0x79) #changes the Prescale register value for 50 Hz, using the equation in the datasheet.
            bus.write_byte_data(chip_addr, 0, 0x20) # enables the chip
            time.sleep(.25)        
        
    def calibrate(self):

        self.x.calibrate()
        self.y.calibrate()
        self.z.calibrate()    
        
            
    def move_forward(self):

        self.x.modes = [1, -1, -1, 1, 1, 1, 0]
        self.y.modes = [-1, -1, -1, 1, 1, -1, 0]
        self.z.modes = [1, -1, -1, 1, 1, 1, 0]
        
        #for i in range(1,200):
        self.x.move(1)
        self.y.move(-1)
        self.z.move(1)
        print('x: {} {} {}, y: {} {} {}, z: {} {} {}'.format(self.x.angle, self.x.lleg.angle, self.x.rleg.angle,self.y.angle,self.y.lleg.angle, self.y.rleg.angle,self.z.angle,self.z.lleg.angle, self.z.rleg.angle))
        #time.sleep(.3)
        
    def move_backwards(self):

        self.x.modes = [-1, -1, -1, 1, 1, -1, 0]
        self.y.modes = [1, -1, -1, 1, 1, 1, 0]
        self.z.modes = [-1, -1, -1, 1, 1, -1, 0]

        #for i in range(1,200):
        self.x.move(1)
        self.y.move(-1)
        self.z.move(1)
         
        #self.calibrate()
   
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