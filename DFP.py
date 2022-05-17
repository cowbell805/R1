from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery)
me.takeoff()
me.move_up(140)
sleep(.5)
# the drone will take off to a specific height and wait until further instructions
me.move_forward(470)
sleep(.5)
# the drone moves forward then pauses before traveling the rest of the given distance
me.rotate_counter_clockwise(90)
sleep(.5)
me.move_forward(300)
sleep(.5)
# drone will rotate and then continue forward
me.rotate_counter_clockwise(90)
sleep(.5)
me.move_forward(200)
me.move_forward(200)
me.move_forward(200)
sleep(.5)
# the drone will turn and move forward again
me.rotate_counter_clockwise(90)
sleep(.5)
me.move_forward(300)
sleep(.5)
# drone will take its final turn and lower its self to the landing pad and land
me.rotate_counter_clockwise(90)
sleep(.5)
me.land()
