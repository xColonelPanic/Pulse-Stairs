import presets
import time

# presets.all_white()
# presets.danceparty()

# while True:
# 	presets.minor_pulse(1, 0, 150, 15, 255) 

# presets.calibrate_all()

# presets.spring_pulse(0, 25, 255)

# while True:
#	presets.treadmill(0, 65, 225, 5)
	# time.sleep(1)
#	presets.treadmill(255, 35, 0, 5)
	# time.sleep(1)


num_iterations = 1000

while True:
	presets.calibrate_all()

	time.sleep(1)

	for i in range(0, num_iterations):
		presets.treadmill(0, 65, 225, 5)
		presets.treadmill(255, 35, 0, 5)
		presets.treadmill(0, 255, 25, 5)

	time.sleep(1)

	for i in range(0, num_iterations):
		presets.minor_pulse(range(1, 17), 0, 65, 225, 255)	
		presets.minor_pulse(range(1, 17), 255, 35, 0, 255)
		presets.minor_pulse(range(1, 17), 0, 255, 25, 255)
	
	time.sleep(1)

	for i in range(0, num_iterations):
		presets.transition_rgb(range(1, 17), (0, 65, 225), (255, 35, 0), 20)
		presets.transition_rgb(range(1, 17), (255, 35, 0), (0, 255, 25), 20)
		presets.transition_rgb(range(1, 17), (0, 255, 25), (0, 65, 225), 20)


	time.sleep(5)
