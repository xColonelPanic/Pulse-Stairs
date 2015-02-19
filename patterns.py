from helpers import *
ORANGE_R=R=255
ORANGE_G=G=35
ORANGE_B=B=0

DULL_BLUE_R=0
DULL_BLUE_G=5
DULL_BLUE_B=65

PULSERATE=10
r=10
g=10
b=10
stairs = range(1,17)
while True:
#	if r <= ORANGE_R:
#		r+=PULSERATE
#	
#	if g <= ORANGE_G:
#		g+=PULSERATE
#	if r > ORANGE_R and g >= ORANGE_G:
#		PULSERATE*=-1
#		r=ORANGE_R
#		G=ORANGE_G	
#	if r < 10 and g < 10:
#		r=10
#		g=10
#		PULSERATE*=-1
#	r+=255/PULSERATE
#	g+=35/PULSERATE
#	if r > 255:
#		PULSERATE*=-1
#		r=255
#		g=35
#	if r < 9 or g < 9:
#		r=10
#		g=10			
#	for stair in stairs:
#		set_stair(stair, r, g, b)
	set_stair(random.randint(1,16),random.randint(240,255),random.randint(25,35),0,random.randint(0,255))		
	time.sleep(0.5)
	set_stair(random.randint(1,16), 0 ,random.randint(10,20),random.randint(0,240),random.randint(0,255))           
	time.sleep(0.5)














