from smbus2 import SMBus
from smbus2 import SMBusWrapper
from SpiderMoves import SpiderMoves
import SpiderInit
import time


if __name__ == "__main__":
    start = time.time()
    time.sleep(5)
    SMoves = SpiderMoves()
    #Smoves = SpiderInit.SMoves
    #SMoves.calibrate()
    for i in range(1,500):
       SMoves.move_forward()
       time.sleep(.0001)
    SMoves.calibrate()
    #SMoves.move_backwards()
    #SMoves.calibrate()
    #for i in range(1,5):
    #    SMoves.turn_right()
    end = time.time()
    print(end-start)
    #servo movement testing:
    # for i in range(1,5):
    #     SMoves.move_forward()
    #time.sleep(5)
    print("reset")
    #with SMBusWrapper(1) as bus:
    #    bus.write_byte(0x00, 0x06)