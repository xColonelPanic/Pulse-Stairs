#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import stairvalues
import random

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

def set_stair(stair, r, g, b, alpha=255):
	rgb = convert_rgb_to_pwm(r,g,b, alpha)

	# pwm = PWM(stairs[stair]['r'][0])
	chips[stairs[stair]['r'][0]].setPWM( stairs[stair]['r'][1], 0, rgb[0])

	# pwm = PWM(stairs[stair]['g'][0])
	chips[stairs[stair]['g'][0]].setPWM( stairs[stair]['g'][1], 0, rgb[1])
	
	# pwm = PWM(stairs[stair]['b'][0])
	chips[stairs[stair]['b'][0]].setPWM( stairs[stair]['b'][1], 0, rgb[2])
	
def danceparty():
	while True:
		for s in range(1,17):
			set_stair(s,random.randint(0,255), random.randint(0,255),random.randint(0,255))
			# time.sleep(0.001)

def test_convert():
	print "Testing convert_rgb_to_pwm function..."
	print "TEST 1: 255,255,255"
	rgb = convert_rgb_to_pwm(255,255,255)
	print rgb

	print "TEST 2: 127,127,127"
	rgb2 = convert_rgb_to_pwm(127,127,127)
	print rgb2

	print "TEST 3: 0,127,255"
	rgb3 = convert_rgb_to_pwm(0,127,255)
	print rgb3

	print "Test Finished"

def test_set_stair():
	print "Testing set_stair function..."
	print "setting stair 0"
	set_stair(1, 255, 255, 255)
	print "setting stair 1"
	set_stair(2, 255, 255, 255)
	print "setting stair 2"
	set_stair(3, 255, 255, 255)
	print "Test Finished"

def test_stair_colors():
	for x in range(1,16):
		set_stair(x, 255, 0, 0)
		time.sleep(1)
		set_stair(x, 0, 255, 0)
		time.sleep(1)
		set_stair(x, 0, 0, 255)
		time.sleep(1)
		set_stair(x, 0, 0, 0)
		time.sleep(1)

def pulsecolor(stairs, color, pulserate):
	c = 0
	while True:
		c+=pulserate
		if c > 250 or c < 5:
			pulserate*=-1

		for stair in stairs:
			if color == 0:
				set_stair(stair, c, 0, 0)
			if color == 1:
				set_stair(stair, 0, c, 0)
			if color == 2:
				set_stair(stair, 0, 0, c)



		# time.sleep(0.1)

def pulse_rgb_color(stairs, color1, color2, color3, pulserate):
	# color = 0
	c = 5
	while True:

		c+=pulserate
		if c > 255:
			c = 255
			pulserate*=-1
			# color+=1
			# color%=3
		elif c < 5:
			c = 5
			pulserate*=-1
			# color+=1
			# color%=3

		for stair in stairs:
			set_stair(stair, color1/c + c, color2/c + c, color3/c + c)
			# if color == 1:
			# set_stair(stair, 0, color/c + c, 0)
			# if color == 2:
			# set_stair(stair, 0, 0, color/c + c)

def pulsecolors(stairs, pulserate):
	color = 0
	c = 0
	while True:

		c+=pulserate
		if c > 255:
			c = 255
			pulserate*=-1
			# color+=1
			# color%=3
		elif c < 0:
			c = 0
			pulserate*=-1
			color+=1
			color%=3

		for stair in stairs:
			if color == 0:
				set_stair(stair, c, 0, 0)
			if color == 1:
				set_stair(stair, 0, c, 0)
			if color == 2:
				set_stair(stair, 0, 0, c)


def run_stairs(values):
	while True:
		v_index = 0
		for stair_num in values.keys():
			set_stair(stair_num, values[stair_num][0][v_index], values[stair_num][1][v_index], values[stair_num][2][v_index])
			v_index+=1
			v_index%=len(values[stair_num][0])


v_in = {}
for s in range(1,17):
	for color in xrange(3):
		for x in range(1,100):
			r_pattern_set = []
			g_pattern_set = []
			b_pattern_set = []

			r_pattern_set.append(5*x % 255)
			g_pattern_set.append(255)
			b_pattern_set.append(255)
			v_in[s] = { 0: r_pattern_set, 1: g_pattern_set, 2: b_pattern_set}


def test_channels():
	for i in xrange(3):
		for y in xrange(16):
			chips[i].setPWM(y,0,255)
			# print i + " " + y
			# time.sleep(5)
			# chips[i].setPWM(y,0,0)
def calibrate(x):
	# for stair in range(1,17):
		set_stair(x,255,0,0)
		time.sleep(.1)
		set_stair(x,0,0,0)
		set_stair(x,0,255,0)
		time.sleep(.1)
		set_stair(x,0,0,0)
		set_stair(x,0,0,255)
		time.sleep(.1)
		set_stair(x,0,0,0)
		set_stair(x,255,255,255)
		# set_stair(x,random.randint(1,255),random.randint(1,255),random.randint(1,255))
def calibrate2(x):
	# for stair in range(1,17):
		set_stair(x,255,0,0)
		time.sleep(.1)
		set_stair(x,0,0,0)
		set_stair(x,0,255,0)
		time.sleep(.1)
		set_stair(x,0,0,0)
		set_stair(x,0,0,255)
		time.sleep(.1)
		set_stair(x,0,0,0)

def calibrate_all():
	for x in range(1,17):
		calibrate(x)
	time.sleep(1)
	for x in range(1,17):
		calibrate2(17-x)
		# calibrate(17-x)

def all_white():
	for x in range(1,17):
		set_stair(x,255,255,255)

# test_channels()
# pulsecolors(range(1,16), 5)

# calibrate_all()
# calibrate(10)
# all_white()
# danceparty()
# while True:
# 	minor_pulse(1, 0, 150, 15, 255)

# set_stair(1,255,35,0)
# set_stair(2,255,35,0)
# set_stair(3,255,35,0)
# set_stair(4,255,35,0)
# set_stair(5,255,35,0)
# set_stair(6,0,5,65)
# set_stair(7,0,5,65)
# set_stair(8,0,5,65)
# set_stair(9,0,5,65)
# set_stair(10,0,5,65)
# set_stair(11,0,5,65)
# set_stair(12,0,150,15)
# set_stair(13,0,150,15)
# set_stair(14,0,150,15)
# set_stair(15,0,150,15)
# set_stair(16,0,150,15)

# set_stair(4,255,255,255)
# set_stair(5,255,255,255)
# set_stair(6,255,255,255)
# set_stair(7,255,255,255)
# set_stair(8,255,255,255)
# set_stair(9,255,255,255)
# set_stair(10,255,255,255)
# set_stair(11,255,255,255)
# set_stair(12,255,255,255)
# set_stair(13,255,255,255)
# set_stair(14,255,255,255)
# set_stair(15,255,255,255)
# set_stair(16,255,255,255)
# set_stair(1,197,56,48)
# set_stair(2,233,123,55)
# set_stair(3,51,74,93)


