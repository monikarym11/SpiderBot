import RPi.GPIO as GPIO
import time
def SetAngle(pwm, pin, angle, a):
    duty=1./18.*angle+a
    pwm.ChangeDutyCycle(duty)
    
def step_one():
    for i in range(90,180,1):
        SetAngle(pwmh, 3, i, 2)
        SetAngle(pwmv, 5, i-40, 4)
        time.sleep(.01)
        
def step_two():
    for i in range(180,90,-1):
        SetAngle(pwmh, 3, i, 2)
        SetAngle(pwmv, 5, i-40, 4)
        time.sleep(.01)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
pwmh=GPIO.PWM(3, 50)
pwmv=GPIO.PWM(5, 50)
pwmh.start(7)
pwmv.start(7)

i=0
while(i!=10):
    step_one()
    step_two()    
    i+=1
    
SetAngle(pwmh, 3, 100, 2)
SetAngle(pwmv, 5, 90, 4)

pwmh.stop()
pwmv.stop()       
GPIO.cleanup()
