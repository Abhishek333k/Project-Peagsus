import RPI.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
GPIO.setup(07, GPIO.OUT)
pwm=GPIO.pwm(07, 100)

pwm.start(0)
GPIO.output(03, Ture)
GPIO.output(05, False)

pwm.ChangeDutyCycle(50)
GPIO.output(07, False)
sleep(2)

GPIO.output(07, False)
GPIO.output(03, False)
GPIO.output(05, True)
pwm.ChangeDutyCycle(75)

GPIO.output(07, True)
sleep(3)
GPIO.output(07, False)
pwm.stop()
GPIO.cleanup()
