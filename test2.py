from smbus2 import SMBus
from smbus2 import SMBusWrapper
import time

chip_addr = 0x40

class SpiderMoves():
    def __init__(self):            
        
        self.x = Pair([0x06, 0x0A, 0x0E], [0x08, 0x0C, 0x10])
        self.y = Pair([0x12, 0x16, 0x1A], [0x14, 0x18, 0x1C])
        self.z = Pair([0x1E, 0x22, 0x26], [0x20, 0x24, 0x28])

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
        time.sleep(.3)
        
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

def move_angle(angle, addr):

    with SMBusWrapper(1) as bus:
        bus.write_word_data(chip_addr, addr, 209+angle)
    #time.sleep(.3)

class Pair():

    def __init__(self, start_addr, stop_addr):

        self.angle = 0
        self.start_addr = start_addr[0]
        self.stop_addr = stop_addr[0]              
        self.min = -44
        self.max = 44
        self.mode = 1
        self.modes = []
        self.last = 0

        with SMBusWrapper as bus:
            bus.write_word_data(self.addr, self.start_addr, 0) # chl 0 start time = 0us                       
            time.sleep(.25)
            bus.write_word_data(self.addr, self.stop_addr, 209) # chl 0 end time = 1.0ms (0 degrees)
            time.sleep(.25)

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
                    time.sleep(.3)
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
            time.sleep(.3)
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

class Leg():

    def __init__(self, side, start_addr, stop_addr):

        self.angle = 0
        self.start_addr = start_addr
        self.stop_addr = stop_addr

        with SMBusWrapper as bus:
            bus.write_word_data(self.addr, self.start_addr, 0) # chl 0 start time = 0us                       
            time.sleep(.25)
            bus.write_word_data(self.addr, self.stop_addr, 209) # chl 0 end time = 1.0ms (0 degrees)
            time.sleep(.25)

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
    
if __name__ == "__main__":
    start = time.time()
    SMoves = SpiderMoves()
    #for i in range(1,200):
    #   SMoves.move_forward()
    #   time.sleep(.3)
    #SMoves.calibrate()
    #SMoves.move_backwards()
    #SMoves.calibrate()
    for i in range(1,5):
        SMoves.turn_right()
    end = time.time()
    print(end-start)
    #servo movement testing:
    # for i in range(1,5):
    #     SMoves.move_forward()
    #time.sleep(5)


###############################################################3   
#useful commends for testing:

#print('x: {} {} {}, y: {} {} {}, z: {} {} {}'.format(self.x.angle, self.x.lleg.angle, self.x.rleg.angle,self.y.angle,self.y.lleg.angle, self.y.rleg.angle,self.z.angle,self.z.lleg.angle, self.z.rleg.angle))

#bus.write_word_data(addr, 0x08, 312) # chl 0 end time = 1.5ms (45 degrees)
#time.sleep(5)
#bus.write_word_data(addr, 0x08, 416) # chl 0 end time = 2.0ms (90 degrees)

#print('last: {}, side: {}, angle: {}'.format(last, self.mode, self.angle))

# def move(self):        
#         #for angle in self.angles:
#         for angle in angles:
#             time.sleep(.005) #time delay
#             self.move_angle(angle)