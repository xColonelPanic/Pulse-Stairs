#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import helpers
import stairvalues

chips = [PWM(0x40), PWM(0x41), PWM(0x42)]
stairs = stairvalues.stairs


# transition()
# args:
# 	stair: 1-16, bottom step is 1, top step is 16
# 	rgb1: 3-ple of red, green, blue value for initial color
# 	rgb2: 3-ple of red, green, blue value for ending color
# 	speed: number of steps to reach the ending color
def transition(stair, rgb1, rgb2, speed):
	helpers.set_stair(stair, rgb1[0], rgb1[1], rgb1[2])
	rgbpwm1 = helpers.convert_to_pwm(rgb1[0], rgb1[1], rgb1[2])
	rgbpwm2 = helpers.convert_to_pwm(rgb2[0], rgb2[1], rgb2[2])
	rgbratio = rgbpwm1/rgbpwm2