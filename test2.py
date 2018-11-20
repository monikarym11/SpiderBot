#from smbus2 import SMBus
from smbus2 import SMBusWrapper
import time

class SpiderMoves():
    def __init__(self):
        #self.angles = list(range(1,90))+list(range(90,1,-1))
        self.addr = 0x40
        #self.legs = Legs()
        self.x = Pair()
        self.y = Pair()
        self.z = Pair()
        with SMBusWrapper(1) as bus:
            bus.write_byte_data(self.addr, 0, 0x20) # enable the chip
            time.sleep(.25)
            bus.write_byte_data(self.addr, 0, 0x10) # enable Prescale change as noted in the datasheet
            time.sleep(.25) # delay for reset
            bus.write_byte_data(self.addr, 0xfe, 0x79) #changes the Prescale register value for 50 Hz, using the equation in the datasheet.
            bus.write_byte_data(self.addr, 0, 0x20) # enables the chip

            time.sleep(.25)
            bus.write_word_data(self.addr, 0x06, 0) # chl 0 start time = 0us
                       
            time.sleep(.25)
            bus.write_word_data(self.addr, 0x08, 209) # chl 0 end time = 1.0ms (0 degrees)        
    
    #bus = smbus2.SMBus
    def calibrate(self):
        self.x.calibrate()
        self.y.calibrate()
        self.z.calibrate()
            
    def move_forward(self):
        while(true):
            self.x.move(1)
            self.y.move(-1)
            self.x.move(1)
    def move_round(self):

def move(self):        
        #for angle in self.angles:
        for angle in angles:
            time.sleep(.005) #time delay
            self.move_angle(angle)
def move_angle(angle, addr):
        with SMBusWrapper(1) as bus:
            bus.write_word_data(self.addr, 0x08, 209+angle)

class Pair():
    def __init__(self):
        self.angle = 0
        #self.angles = list(range(-45,45))+list(range(45,-45,-1))
        self.angles = [-45, 0, 45]
        self.addr = 0
        self.lleg = Leg()
        self.rleg = Leg()    
    def calibrate(self):
        while(self.angle != 0):
            self.lleg.move(up)
            self.rleg.move(up)
            move_angle(self.addr)
    def move(self, mode):
        self.angle = self.angle + mode          
        self.lleg.move(up)
        self.rleg.move(down)
        move_angle(self.angle, self.addr)

class Leg():
    def __init__(self):
        self.angle = 0
        #self.angles = list(range(-1,90))+list(range(90,-1,-1))
        self.angles = [-1, 0, 90]
        self.addr = 0
    def move(self, mode):
        
    

      

    ## Running this program will move the servo to 0, 45, and 90 degrees with 5 second pauses in between with a 50 Hz PWM signal.
if __name__ == "__main__":
    SMoves = SpiderMoves()
    
    #servo movement testing:
    for i in range(1,5):
        SMoves.move()
    #time.sleep(5)
    #bus.write_word_data(addr, 0x08, 312) # chl 0 end time = 1.5ms (45 degrees)
    #time.sleep(5)
    #bus.write_word_data(addr, 0x08, 416) # chl 0 end time = 2.0ms (90 degrees)