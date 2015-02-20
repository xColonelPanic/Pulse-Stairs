# Chris Shroba
# Flash All

import stairs
import random

while True:
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)
     for stair in range(1,17):
          stairs.set_stair_rgb(stair,r,g,b)
