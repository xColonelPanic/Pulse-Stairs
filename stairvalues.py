#!/usr/bin/python

# rgbpwm = [
# 	(0,1,2), # step 0
# 	(3,4,5), # step 1
# 	(6,7,8), # step 2
# 	(9,10,11), # step 3
# 	(12,13,14) # step 4
# ]

# 0x40:
# 1		0,1,2
# 2		3,4,5
# 3		6,7,8
# 4		9,10,11
# 5		12,13,14
# 6		15,x,x
# 0x41:
# 6		x,0,1
# 7		2,3,4
# 8		5,6,7
# 9		8,9,10
# 10	11,12,13
# 11	14,15,x
# 0x42:
# 11	x,x,0
# 12	1,2,3
# 13	4,5,6
# 14	7,8,9
# 15	10,11,12
# 16	13,14,15

stairs = {
	1:{'g': (0, 4), 'b': (0, 3), 'r': (0, 5)},
	2:{'r': (0, 9), 'b': (0, 6), 'g': (0, 7)},
	3:{'g': (0, 11), 'r': (0, 8), 'b': (0, 10)},
	4:{'r': (0, 14), 'b': (0, 12), 'g': (0, 13)},
	5:{'r': (0, 1), 'b': (0, 0), 'g': (0, 2)},
	6:{'r': (1, 1), 'g': (1, 0), 'b': (0, 15)},
	7:{'g': (1, 4), 'b': (1, 2), 'r': (1, 3)},
	8:{'r': (1, 7), 'b': (1, 5), 'g': (1, 6)},
	9:{'g': (1, 10), 'b': (1, 8), 'r': (1, 9)}, # pwm bug, fix it
	10:{'r': (1, 13), 'b': (1, 11), 'g': (1, 12)}, # blue channel turns on with 2's blue channel
	11:{'g': (2, 0), 'b': (1, 14), 'r': (1, 15)},
	12:{'g': (2, 3), 'b': (2, 1), 'r': (2, 2)},
	13:{'g': (2, 5), 'b': (2, 4), 'r': (2, 6)},
	14:{'b': (2, 9), 'r': (2, 7), 'g': (2, 8)},
	15:{'r': (2, 12), 'b': (2, 10), 'g': (2, 11)},
	16:{'g': (2, 15), 'b': (2, 14), 'r': (2, 13)}
}








# cur_chip = 0
# cur_channel = 0
# for s in range(1,17):
	
# 	r_pair = (cur_chip, cur_channel)
# 	cur_channel+=1
# 	cur_channel%=16
# 	cur_chip = cur_chip+1 if cur_channel == 0 else cur_chip
	
# 	g_pair = (cur_chip, cur_channel)
# 	cur_channel+=1
# 	cur_channel%=16
# 	cur_chip = cur_chip+1 if cur_channel == 0 else cur_chip
	
# 	b_pair = (cur_chip, cur_channel)
# 	cur_channel+=1
# 	cur_channel%=16
# 	cur_chip = cur_chip+1 if cur_channel == 0 else cur_chip
# 	stairs[s] = {'r': r_pair, 'g': g_pair, 'b': b_pair}


# print stairs