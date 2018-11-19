import RPi.GPIO as GPIO
import time
def SetAngle(pwm, pin, angle, a):
    duty=1./18.*angle+2
    #GPIO.output(pin,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(.01)
    #GPIO.output(pin,False)
    #pwm.ChangeDutyCycle(0)
def step_one(pwmh):
    for i in range(90,180,1):
        SetAngle(pwmh, 5, i, 2)
def step_two(pwmh):
    for i in range(180,90,-1):
        SetAngle(pwmh, 5, i, 2)
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
pwmh=GPIO.PWM(5, 50)
pwmh.start(7)
while(1):
    step_one(pwmh)
    step_two(pwmh)
pwmh.stop()
GPIO.cleanup()

