#! /user/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

def startLED():
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.HIGH)
	time.sleep(1)
def endLED():
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	time.sleep(1)

