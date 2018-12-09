from smbus2 import SMBus
from smbus2 import SMBusWrapper
from SpiderMoves import SpiderMoves

import time


if __name__ == "__main__":
    start = time.time()
    time.sleep(5)
    SMoves = SpiderMoves()
    #for i in range(1,200):
    #   SMoves.move_forward()
    #   time.sleep(.05)
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