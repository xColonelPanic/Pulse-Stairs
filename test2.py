#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

# rgbpwm:
#	rgbpwm[strip][rgb]
#	(b, r, g)

rgbpwm = [
	(0,1,2), # step 0
	(3,4,5), # step 1
	(6,7,8), # step 2
	(9,10,11) # step 3
]
# rgbpwm = [];
# for x in xrange():





for rgb in rgbpwm:
	for c in rgb:
		pwm.setPWM(c, 0, 0)
pwm.setPWM(rgbpwm[0][0], 0, 0)



def puretransition(color1, color2, rate):
	pwm.setPWM(rgbpwm[0][color1],0,4095)
	pwm.setPWM(rgbpwm[0][color2],0,0)
	for x in xrange(4095/10):
		pwm.setPWM(rgbpwm[0][color1],0,4095 - 10*x)
		pwm.setPWM(rgbpwm[0][color2],0,0 + 10*x)

def setstair(stair,r,g,b):
	pwm.setPWM(rgbpwm[stair][0], 0, b)
	pwm.setPWM(rgbpwm[stair][1], 0, r)
	pwm.setPWM(rgbpwm[stair][2], 0, g)

# latentseizure(0,0,1,2)
#latentseizure(1)
#latentseizure(2)

# pulsecolor(0,5)


# pwm.setPWM(rgbpwm[0][0], 1000, 2000)
# time.sleep(1)
# pwm.setPWM(rgbpwm[0][0], 0, 0)

# pwm.setPWM(rgbpwm[0][1], 2000, 3000)
# time.sleep(1)
# pwm.setPWM(rgbpwm[0][1], 0, 0)

# pwm.setPWM(rgbpwm[0][2], 3000, 4000)
# time.sleep(1)
# pwm.setPWM(rgbpwm[0][2], 0, 0)


# pulsecolor(0, 5)
# time.sleep(1)
# pulsecolor(1, 5)
# time.sleep(1)
# pulsecolor(2, 5)
