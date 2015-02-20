# Chris Shroba
# Dance Party

import stairs
import random

while True:
     for stair in range(1,17):
          r = random.randint(0,255)
	  g = random.randint(0,255)
	  b = random.randint(0,255)
          stairs.set_stair_rgb(stair,r,g,b)
