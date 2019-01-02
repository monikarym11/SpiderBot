from smbus2 import SMBus
from smbus2 import SMBusWrapper
from ServoControll import initialize, move_angle
import time
class ILeg():
    def __init__(self, side, start_addr, stop_addr):

        self.angle = 0
        self.start_addr = start_addr
        self.stop_addr = stop_addr

        initialize(self.start_addr, self.stop_addr)

        if(side == 'left'):
            self.mode = 1
        elif(side =='right'):
            self.mode = -1

        self.lock = True
        self.modes = [1,-1, 1, 1, -1, 1]
        self.max = 22
        self.min = -10
        self.addr = 0

class Leg():

    def __init__(self, side, start_addr, stop_addr):

        self.angle = 0
        self.start_addr = start_addr
        self.stop_addr = stop_addr

#        initialize(self.start_addr, self.stop_addr)

        if(side == 'left'):
            self.mode = 1
        elif(side =='right'):
            self.mode = -1

        self.lock = True
        self.modes = [1,-1, 1, 1, -1, 1]
        self.max = 22
        self.min = -10
        self.addr = 0

    def move(self, last, mode):        
        if(last != 0 and last != 5 and last !=6):
            self.angle = self.angle + 2*(self.modes[last]*self.mode)
        elif(last == 0):
            self.angle = self.angle + 2*(mode * self.mode)
        elif(last == 5):
            self.angle = self.angle - 2*(mode * self.mode)

        if(self.angle == self.min):
            self.lock = False
        move_angle(self.angle, self.stop_addr)
#or self.angle == self.max
    def calibrate(self):
        self.angle = self.angle + (0-self.angle)/abs(self.angle)
        move_angle(self.angle, self.stop_addr)
        