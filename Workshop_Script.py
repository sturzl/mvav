import time
import RPi.GPIO as GPIO

mode = GPIO.getmode()

GPIO.cleanup()

left_forward = 26
left_backward = 19
right_forward = 16
right_backward = 13
sleep_time = 1
FORWARD = 'forward'
BACKWARD = 'backward'

pwm_frequency = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_forward, GPIO.OUT)
GPIO.setup(left_backward, GPIO.OUT)
GPIO.setup(right_forward, GPIO.OUT)
GPIO.setup(right_backward, GPIO.OUT)

'''
#######
Skip to line 74 (runExperiment)
You don't need to edit this section, but you can with a more advance group
'''
def forward(x):
    GPIO.output(left_forward, GPIO.HIGH)
    GPIO.output(right_forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(left_forward, GPIO.LOW)
    GPIO.output(right_forward, GPIO.LOW)


def reverse(x):
    GPIO.output(left_backward, GPIO.HIGH)
    GPIO.output(right_backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(left_backward, GPIO.LOW)
    GPIO.output(right_backward, GPIO.LOW)


def leftWheel(direction, x):
    pin = left_backward
    if direction == FORWARD:
        pin = left_forward

    GPIO.output(pin, GPIO.HIGH)
    print("left wheel " + direction)
    time.sleep(x)
    GPIO.output(pin, GPIO.LOW)


def rightWheel(direction, x):
    pin = right_backward
    if direction == FORWARD:
        pin = right_forward

    GPIO.output(pin, GPIO.HIGH)
    print("Right wheel " + direction)
    time.sleep(x)
    GPIO.output(pin, GPIO.LOW)


'''
#######
This is the only thing you should need to change
'''

def runExperiment():
    forward(1)
    reverse(1)
    leftWheel(FORWARD, 1)
    rightWheel(BACKWARD, 5)


while 1:
    runExperiment()
    GPIO.cleanup()
    break
