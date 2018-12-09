class getout(Exception):
    pass
import time
import os
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)
global a
a=0
try:
    while True:
        i=GPIO.input(11)
        if i==0:
            print("No Intuders",i)
            GPIO.output(3, 0)
            time.sleep(0)
            a=0
        elif i==1:
            print("Intruder Detected",i)
            GPIO.output(3, 1)
            time.sleep(0)
            a=1
            if a==1:
                print("Mail .... The End")
                raise getout
except getout:
    import myemail
    pass
    
            
