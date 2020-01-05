import errno, sys
import RPi.GPIO as GPIO

MonitorSwitchGPIO = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(MonitorSwitchGPIO, GPIO.IN,pull_up_down=GPIO.PUD_UP)

inputValue = GPIO.input(MonitorSwitchGPIO)
if (inputValue == False):
    print('Vertical')
    sys.exit(0)
else:
    print('Horizontal')
    sys.exit(1)
    