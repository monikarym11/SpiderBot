from smbus2 import SMBusWrapper
import time

chip_addr = 0x40
#point_zero = 280

def bus_initialize():
    with SMBusWrapper(1) as bus:
            bus.write_byte_data(chip_addr, 0, 0x20) # enable the chip
            time.sleep(.25)
            bus.write_byte_data(chip_addr, 0, 0x10) # enable Prescale change as noted in the datasheet
            time.sleep(.25) 
            bus.write_byte_data(chip_addr, 0xfe, 0x79) #changes the Prescale register value for 50 Hz, using the equation in the datasheet.
            bus.write_byte_data(chip_addr, 0, 0x20) # enables the chip
            time.sleep(.25)        

def initialize(point_zero, start_addr, stop_addr):
    with SMBusWrapper(1) as bus:
            bus.write_word_data(chip_addr, start_addr, 0) # start time = 0us                       
            time.sleep(.25)            
            bus.write_word_data(chip_addr, stop_addr, point_zero) # end time = 1.5ms (45 degrees)
    
def move_angle(point_zero, angle, addr):

    with SMBusWrapper(1) as bus:
        bus.write_word_data(chip_addr, addr, int(point_zero+angle))
        
def reset_servos():
    with SMBusWrapper(1) as bus:
        bus.write_byte(0x00, 0x06)
    print("reset")