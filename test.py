#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

rgbpwm = [
	(0,1,2), # step 0
	(3,4,5), # step 1
	(6,7,8), # step 2
	(9,10,11) # step 3
]
counter = 0;
pwm.setPWM(rgbpwm[0][0], 0, 4095)
#while True:
#	pwm.setPWM(rgbpwm[0][0], 0, counter % 4096)
#	pwm.setPWM(rgbpwm[0][1], counter % 4096, (counter + 1024) % 4096 )
#	pwm.setPWM(rgbpwm[0][2], (counter + 1024)% 4096, (counter + 2048) % 4096 )
#	pwm.setPWM(rgbpwm[0][0], 0, 2048)
#	pwm.setPWM(rgbpwm[0][1], 0, 2048)
#	pass
