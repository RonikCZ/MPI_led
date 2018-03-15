import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
 while True:
  pwmRed = GPIO.PWM(18, 500)
  pwmRed.start(100)

  pwmGreen = GPIO.PWM(23, 500)
  pwmGreen.start(100)

  pwmBlue = GPIO.PWM(24, 500)
  pwmBlue.start(100)

  GPIO.output(23,True)
except KeyboardInterrupt:
 GPIO.output(23,False)
 GPIO.cleanup()
