#!/usr/bin/python

import time
import helpers
import stairvalues
from Adafruit.Adafruit_PWM_Servo_Driver import PWM

chips = [PWM(0x40), PWM(0x41), PWM(0x42)]
stairs = stairvalues.stairs

def minor_pulse(stairs, r, g, b, max_value):
	# set_stair(stair, r, g, b)
	counter = 0
	while counter < max_value:
		for stair in stairs:
			helpers.set_stair(stair, r, g, b, counter)
		counter += 10
	while counter > 0:
		for stair in stairs:
			helpers.set_stair(stair, r, g, b, counter)
		counter -= 10
	# 	time.sleep(1)

while True:
	minor_pulse(range(1,17), 0, 150, 15, 255)
	# time.sleep(.1)
	minor_pulse(range(1,17), 255, 35, 0, 255)
	# time.sleep(.1)
	minor_pulse(range(1,17), 0, 5, 65, 255)

