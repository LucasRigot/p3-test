from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0 ,0)
for i in range(20):
    sense.clear()
    sleep(0.5)
    sense.clear(red)
    sleep(0.5)
    sense.clear