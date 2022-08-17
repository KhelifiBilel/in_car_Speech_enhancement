import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(7,gpio.OUT)
	gpio.setup(11,gpio.OUT)
	gpio.setup(33,gpio.OUT)
	gpio.setup(35,gpio.OUT)


def fwd():
	init()
	gpio.output(7,False)
	gpio.output(11,True)
	gpio.output(33,True)
	gpio.output(35,False)
	time.sleep(1)
	gpio.cleanup()


def bwd():
	init()
	gpio.output(7,True)
	gpio.output(11,False)
	gpio.output(33,False)
	gpio.output(35,True)
	time.sleep(0.5)
	gpio.cleanup()

def left():
	init()
	gpio.output(7,False)
	gpio.output(11,False)
	gpio.output(33,False)
	gpio.output(35,True)
	time.sleep(1.5)
	gpio.cleanup()

def right():
	init()
	gpio.output(7,True)
	gpio.output(11,False)
	gpio.output(33,False)
	gpio.output(35,False)
	time.sleep(1.5)
	gpio.cleanup()

def stop():
    init()
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(33,False)
    gpio.output(35,False)
    gpio.cleanup()

def blue():
    gpio.setmode(gpio.BOARD)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.output(22,False)
    gpio.output(18,True)
    time.sleep(4)
    gpio.cleanup()
    
def green():
    gpio.setmode(gpio.BOARD)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.output(18,False)
    gpio.output(22,True)
    time.sleep(4)
    gpio.cleanup()
    
def light_off():
    gpio.setmode(gpio.BOARD)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.output(18,False)
    gpio.output(22,False)
    gpio.cleanup()    
