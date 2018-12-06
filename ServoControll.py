from smbus2 import SMBusWrapper
import time

chip_addr = 0x40

def initialize(start_addr, stop_addr):
    with SMBusWrapper as bus:
            bus.write_word_data(chip_addr, start_addr, 0) # chl 0 start time = 0us                       
            time.sleep(.25)
            bus.write_word_data(chip_addr, stop_addr, 209) # chl 0 end time = 1.0ms (0 degrees)
            time.sleep(.25)

def move_angle(angle, addr):

    with SMBusWrapper(1) as bus:
        bus.write_word_data(chip_addr, addr, 209+angle)
    #time.sleep(.3)
