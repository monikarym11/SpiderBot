#from smbus2 import SMBus
#from smbus2 import SMBusWrapper
import time

class SpiderMoves():
    def __init__(self):
        #self.angles = list(range(1,90))+list(range(90,1,-1))
        self.addr = 0x40
        #self.legs = Legs()
        self.x = Pair()
        self.y = Pair()
        self.z = Pair()
        # with SMBusWrapper(1) as bus:
        #     bus.write_byte_data(self.addr, 0, 0x20) # enable the chip
        #     time.sleep(.25)
        #     bus.write_byte_data(self.addr, 0, 0x10) # enable Prescale change as noted in the datasheet
        #     time.sleep(.25) # delay for reset
        #     bus.write_byte_data(self.addr, 0xfe, 0x79) #changes the Prescale register value for 50 Hz, using the equation in the datasheet.
        #     bus.write_byte_data(self.addr, 0, 0x20) # enables the chip

        #     time.sleep(.25)
        #     bus.write_word_data(self.addr, 0x06, 0) # chl 0 start time = 0us
                       
        #     time.sleep(.25)
        #     bus.write_word_data(self.addr, 0x08, 209) # chl 0 end time = 1.0ms (0 degrees)        
    
    #bus = smbus2.SMBus
    def calibrate(self):
        self.x.calibrate()
        self.y.calibrate()
        self.z.calibrate()
            
    def move_forward(self):
        #while(True):
        self.x.modes= [1, -1, -1, 1, 1, 1]
        self.y.modes = [-1, -1, -1, 1, 1, -1]
        self.z.modes = [1, -1, -1, 1, 1, 1]
        for i in range(1,200):
            self.x.move(1)
            self.y.move(-1)
            self.z.move(1)
            print('x: {} {} {}, y: {} {} {}, z: {} {} {}'.format(self.x.angle, self.x.lleg.angle, self.x.rleg.angle,self.y.angle,self.y.lleg.angle, self.y.rleg.angle,self.z.angle,self.z.lleg.angle, self.z.rleg.angle))
            
        #self.calibrate()
   # def move_round(self):

# def move(self):        
#         #for angle in self.angles:
#         for angle in angles:
#             time.sleep(.005) #time delay
#             self.move_angle(angle)
# def move_angle(angle, addr):
#         with SMBusWrapper(1) as bus:
#             bus.write_word_data(self.addr, 0x08, 209+angle)

class Pair():
    def __init__(self):
        self.angle = 0
        #self.angles = list(range(-45,45))+list(range(45,-45,-1))
        self.mode = 1
        self.modes = []
        self.last = 0
        self.prev = 0        
        self.addr = 0
        self.lleg = Leg('left')
        self.rleg = Leg('right')
        
    def calibrate(self):
        while(self.angle != 0):
            self.lleg.move(1)
            self.rleg.move(1)
            #move_angle(self.addr)
    def move(self, mode):  
        # if(self.angle != 0):
        #     self.lleg.move(self.last, mode)
        #     self.rleg.move(self.last, -mode)
        if(self.lleg.lock):
            self.lleg.move(self.last, mode)
        if(self.rleg.lock):
            self.rleg.move(self.last, mode)
        self.angle = self.angle + self.modes[self.last]
        
        #move_angle(self.angle, self.addr)   
        if(self.angle >= 44):
            self.last = 1            
        elif(self.angle <= -44):
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
        
        
        

class Leg():
    def __init__(self, side):
        self.angle = 0        
        if(side == 'left'):
            self.mode = 1
        elif(side =='right'):
            self.mode = -1
        self.lock = True
        self.modes = [1,-self.mode, self.mode, self.mode, -self.mode, 1]
        #self.max = 
        self.min = -1
        self.addr = 0
    def move(self, last, mode):
        
        if(last != 0 and last != 5):
            self.angle = self.angle + self.modes[last]*mode
        elif(last == 0):
            self.angle = self.angle + (mode * self.mode)
        elif(last == 5):
            self.angle = self.angle - (mode * self.mode)
            #move_angle(self.angle, self.addr)
        #print last + self.angle
        #print('last: {}, side: {}, angle: {}'.format(last, self.mode, self.angle))
        if(self.angle == -5):
            self.lock = False

    ## Running this program will move the servo to 0, 45, and 90 degrees with 5 second pauses in between with a 50 Hz PWM signal.
if __name__ == "__main__":
    start = time.time()
    SMoves = SpiderMoves()
    SMoves.move_forward()
    end = time.time()
    print(end-start)
    #servo movement testing:
    # for i in range(1,5):
    #     SMoves.move_forward()
    #time.sleep(5)
    #bus.write_word_data(addr, 0x08, 312) # chl 0 end time = 1.5ms (45 degrees)
    #time.sleep(5)
    #bus.write_word_data(addr, 0x08, 416) # chl 0 end time = 2.0ms (90 degrees)
