from smbus2 import SMBus
from smbus2 import SMBusWrapper
from ServoControll import initialize, move_angle
import time

class Leg():

    def __init__(self, side, start_addr, stop_addr):

        self.angle = 0
        self.start_addr = start_addr
        self.stop_addr = stop_addr

        initialize(self.start_addr, self.stop_addr)
        # with SMBusWrapper as bus:
        #     bus.write_word_data(self.addr, self.start_addr, 0) # chl 0 start time = 0us                       
        #     time.sleep(.25)
        #     bus.write_word_data(self.addr, self.stop_addr, 209) # chl 0 end time = 1.0ms (0 degrees)
        #     time.sleep(.25)

        if(side == 'left'):
            self.mode = 1
        elif(side =='right'):
            self.mode = -1

        self.lock = True
        self.modes = [1,-1, 1, 1, -1, 1]
        #self.max = 44
        self.min = -5
        self.addr = 0

    def move(self, last, mode):
        
        if(last != 0 and last != 5 and last !=6):
            self.angle = self.angle + self.modes[last]*self.mode
        elif(last == 0):
            self.angle = self.angle + (mode * self.mode)
        elif(last == 5):
            self.angle = self.angle - (mode * self.mode)

        if(self.angle == self.min):
            self.lock = False

    def calibrate(self):

        self.angle = self.angle + (0-self.angle)/abs(self.angle)
        move_angle(self.angle, self.stop_addr)