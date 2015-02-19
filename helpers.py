#!/usr/bin/python

from Adafruit.Adafruit_PWM_Servo_Driver import PWM
import time
import stairvalues
import random
import colorsys

# pwm = PWM(0x40)

chips = [PWM(0x40), PWM(0x41), PWM(0x42)]
stairs = stairvalues.stairs


def convert_rgb_to_pwm(r, g, b, a=255):
	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255
	if r < 0:
		r = 0
	if g < 0:
		g = 0
	if b < 0:
		b = 0
	if a > 255:
		a = 255
	if a < 0:
		a = 0
	alpha = (a / 255.)
	red = 4095. * (r / 255.) * alpha
	green = 4095. * (g / 255.) * alpha
	blue = 4095. * (b / 255.) * alpha
	return (int(red), int(green), int(blue))

def set_stair_rgb(stair, r, g, b, alpha=255):
	rgb = convert_rgb_to_pwm(r,g,b, alpha)

	# pwm = PWM(stairs[stair]['r'][0])
	chips[stairs[stair]['r'][0]].setPWM( stairs[stair]['r'][1], 0, rgb[0])

	# pwm = PWM(stairs[stair]['g'][0])
	chips[stairs[stair]['g'][0]].setPWM( stairs[stair]['g'][1], 0, rgb[1])

	# pwm = PWM(stairs[stair]['b'][0])
	chips[stairs[stair]['b'][0]].setPWM( stairs[stair]['b'][1], 0, rgb[2])

def set_stair_hsv(stair, h, s, v):
	rgb = colorsys.hsv_to_rgb(h,s,v)
	set_stair_rgb(stair, rgb[0], rgb[1].rgb[2])
