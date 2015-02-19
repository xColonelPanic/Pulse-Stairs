import stairs
import math
import sys

import datetime

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0

start_time = unix_time_millis(datetime.datetime.now())

def time():
     dif = unix_time_millis(datetime.datetime.now()) - start_time
     return dif/1000.0

def get_color1():
     return (0,65,225)

def get_color2():
     return (255,35,0)

def get_stair_value(stair):
     sin_value = .5+.5*math.sin(.5*stair - 1*time())
     rat = sin_value
     r1, g1, b1 = get_color1()
     r2, g2, b2 = get_color2()
     r = r1 + rat*(r2-r1)
     g = g1 + rat*(g2-g1)
     b = b1 + rat*(b2-b1)
     return r,g,b

def sin_pulse():
     global start_time
     start_time = unix_time_millis(datetime.datetime.now())
     while time() < 4 * math.pi: 
         for i in range(1,17):
             r,g,b = get_stair_value(i)
             stairs.set_stair_rgb(i, r, g, b)
     

if __name__ == "__main__":
   while True:
       sin_pulse()
