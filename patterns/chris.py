import stairs
import math
import sys

import datetime


a = (0,65,225)
b = (255,35,0)
c = (0, 255, 25)


def get_color1():
     return c

def get_color2():
     return b

def get_stair_value(stair):
     sin_value = .5+.5*math.sin(.5*stair -2*stairs.timestamp())
     rat = sin_value
     r1, g1, b1 = get_color1()
     r2, g2, b2 = get_color2()
     r = r1 + rat*(r2-r1)
     g = g1 + rat*(g2-g1)
     b = b1 + rat*(b2-b1)
     return r,g,b

def sin_pulse():
     global start_time
     start_time = stairs.timestamp()
     while stairs.timestamp()-start_time < 4 * math.pi: 
         for i in range(1,17):
             r,g,b = get_stair_value(i)
             stairs.set_stair_rgb(i, r, g, b)
     

if __name__ == "__main__":
     while True:
          sin_pulse()
