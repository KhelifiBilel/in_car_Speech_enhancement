import RPi.GPIO as gpio
from time import sleep
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(3,gpio.OUT)
    pwm=gpio.PWM(3,50)
    pwm.start(0)

def fwd(angle):
    gpio.setmode(gpio.BOARD)
    gpio.setup(3,gpio.OUT)
    pwm=gpio.PWM(3,50)
    pwm.start(0)
    d=angle/18+2
    gpio.output(3,True)
    pwm.ChangeDutyCycle(d)
    sleep(1)
    gpio.output(3,False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    gpio.cleanup()

def led():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11,gpio.OUT)
    gpio.output(11,True)
    sleep(3)
    gpio.cleanup()