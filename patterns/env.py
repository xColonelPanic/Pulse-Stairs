# All
# Pattern Cycle


import stairs
import time
import sinewave_green_orange  # move this to presets

# stairs.all_white()
# stairs.danceparty()

# while True:
# 	stairs.minor_pulse(1, 0, 150, 15, 255) 

# stairs.calibrate_all()

# stairs.spring_pulse(0, 25, 255)

# while True:
#	stairs.treadmill(0, 65, 225, 5)
    # time.sleep(1)
#	stairs.treadmill(255, 35, 0, 5)
    # time.sleep(1)


num_iterations = 15

while True:
    stairs.calibrate_all()

    time.sleep(1)

    for i in range(0, num_iterations):
 	sinewave_green_orange.sin_pulse()

    for i in range(0, num_iterations):
        stairs.treadmill(0, 65, 225, 5)
        stairs.treadmill(255, 35, 0, 5)
        stairs.treadmill(0, 255, 25, 5)

    time.sleep(1)

    for i in range(0, num_iterations):
        stairs.minor_pulse(range(1, 17), 0, 65, 225, 255)
        stairs.minor_pulse(range(1, 17), 255, 35, 0, 255)
        stairs.minor_pulse(range(1, 17), 0, 255, 25, 255)

    time.sleep(1)

    for i in range(0, num_iterations):
        stairs.transition_rgb(range(1, 17), (0, 65, 225), (255, 35, 0), 20)
        stairs.transition_rgb(range(1, 17), (255, 35, 0), (0, 255, 25), 20)
        stairs.transition_rgb(range(1, 17), (0, 255, 25), (0, 65, 225), 20)


    time.sleep(5)
