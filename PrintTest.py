import RPi.GPIO as GPIO
import time
import numpy as np

LedPin = 16 
T2000 = 2               #2 seconds
T1800 = 1.8             #1.8 seconds
T200 = 0.2              #200 milliseconds
T4p5 = 0.0045           #4.5 milliseconds
T3 = 0.003125              #3 milliseconds
T1p5 = 0.0015          #1.5 milliseconds
button_delay = 0.2
odd = 1
even = 0
pBit = 0
global pCount


def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led
    global pCount
    pCount = 0

def blink():
    GPIO.output(LedPin, GPIO.HIGH)
    time.sleep(T1800) 

def blink_init():
    GPIO.output(LedPin, GPIO.LOW)
    time.sleep(T200)
    for i in range(5):
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(T200)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(T200)    
        
def idle():
    i=1
    R = 20
    for i in range(R):
        if (i == (R-1)):
            GPIO.output(LedPin, GPIO.HIGH)
            time.sleep(T3)
            GPIO.output(LedPin, GPIO.LOW)
            time.sleep(T1p5)
        else:
            GPIO.output(LedPin, GPIO.HIGH)
            time.sleep(T3)
            GPIO.output(LedPin, GPIO.LOW)
            time.sleep(T3)
        

def sync1():
    num = bin(0x26)
    #num = bin(0x59)
    global pCount
    s = [int(z) for z in str(num)[2:].zfill(7)]
    i=0
    for i in range(len(s)):
        if i==0:
            if (s[i] == 1):
                #GPIO.output(LedPin, GPIO.LOW)
                #time.sleep(0.0015625)
                pCount += 1
                GPIO.output(LedPin, GPIO.LOW)           #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(T1p5)
            else:
                #GPIO.output(LedPin, GPIO.HIGH)
                #time.sleep(.003125)
                GPIO.output(LedPin, GPIO.HIGH)          #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(T1p5)
        elif i==6:
            if(s[i] == 0):
                #print " half "
                #GPIO.output(LedPin, GPIO.LOW)
                #time.sleep(0.0015625)
                GPIO.output(LedPin, GPIO.HIGH)          #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(T1p5)
            else:
                #print " whole "
                #GPIO.output(LedPin, GPIO.HIGH) 
                #time.sleep(0.003125)
                pCount += 1
                GPIO.output(LedPin, GPIO.LOW)           #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(T1p5)
        else:
            if (s[i]!= s[i-1]):
                #print " whole "
                if s[i] == 1:
                    #GPIO.output(LedPin, GPIO.HIGH)
                    #time.sleep(0.003125)
                    pCount += 1
                    time.sleep(T1p5)  #Transition mode 1
                    GPIO.output(LedPin, GPIO.HIGH)
                    time.sleep(T1p5)
                else:
                    #GPIO.output(LedPin, GPIO.LOW)
                    #time.sleep(0.003125)
                    time.sleep(T1p5)             #Transition mode 1
                    GPIO.output(LedPin, GPIO.LOW)
                    time.sleep(T1p5)
            else:
                if s[i] == 1:
                    #GPIO.output(LedPin, GPIO.HIGH)
                    #time.sleep(0.0015625)
                    pCount += 1
                    GPIO.output(LedPin, GPIO.LOW)           #Transition mode 2
                    time.sleep(T1p5)
                    GPIO.output(LedPin, GPIO.HIGH)
                    time.sleep(T1p5)
                else:
                    #GPIO.output(LedPin, GPIO.LOW)
                    #time.sleep(0.0015625)
                    GPIO.output(LedPin, GPIO.HIGH)          #Transition mode 2
                    time.sleep(T1p5)
                    GPIO.output(LedPin, GPIO.LOW)
                    time.sleep(T1p5)
        
            
    

def regBlink(x):
    num = bin(~np.uint8(x))
    global pCount
    y = [int(z) for z in str(num)[2:].zfill(8)]
    i=0
    for i in range(len(y)):
        if i==0:
            if (y[i] == 1):
                #print " half "
                ##GPIO.output(LedPin, GPIO.HIGH)
                ##time.sleep(0.0015625)
                pCount += 1
                GPIO.output(LedPin, GPIO.LOW)           #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(T1p5)              
            else:
                #print " whole "
                GPIO.output(LedPin, GPIO.HIGH)          #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(T1p5)
        elif i==7:
            if(y[i] == 0):
                #print " half "
                #pBit = 0
                #GPIO.output(LedPin, GPIO.LOW)
                #time.sleep(0.0015625)
                GPIO.output(LedPin, GPIO.HIGH)          #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(T1p5)
            else:
                #print " whole "
                #pBit = 1
                #GPIO.output(LedPin, GPIO.HIGH)
                #time.sleep(0.003125)
                pCount += 1
                GPIO.output(LedPin, GPIO.LOW)           #Transition mode 2
                time.sleep(T1p5)
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(T1p5)
        else:
            if (y[i]!= y[i-1]):
                #print " whole "
                if y[i] == 1:
                    #GPIO.output(LedPin, GPIO.HIGH)
                    #time.sleep(0.003125)
                    pCount += 1
                    time.sleep(T1p5)             #Transition mode 1
                    GPIO.output(LedPin, GPIO.HIGH)
                    time.sleep(T1p5)
                else:
                    #GPIO.output(LedPin, GPIO.LOW)
                    #time.sleep(0.003125)
                    time.sleep(T1p5)             #Transition mode 1
                    GPIO.output(LedPin, GPIO.LOW)
                    time.sleep(T1p5)
            else:
                if y[i] == 1:
                    #GPIO.output(LedPin, GPIO.HIGH)
                    #time.sleep(0.0015625)
                    pCount += 1
                    GPIO.output(LedPin, GPIO.LOW)       #Transition mode 2
                    time.sleep(T1p5)
                    GPIO.output(LedPin, GPIO.HIGH)
                    time.sleep(T1p5)
                else:
                    #GPIO.output(LedPin, GPIO.LOW)
                    #time.sleep(0.0015625)
                    GPIO.output(LedPin, GPIO.HIGH)      #Transition mode 2
                    time.sleep(T1p5)
                    GPIO.output(LedPin, GPIO.LOW)
                    time.sleep(T1p5)
                #time.sleep(.003125/2)
                #print " half "
                #time.sleep(0.5)

def parity():
##    if pBit == 0:
##        #GPIO.output(LedPin, GPIO.HIGH)
##        #time.sleep(0.003125)
##        #GPIO.output(LedPin, GPIO.LOW)
##        time.sleep(T1p5)             #Transition mode 1
##        GPIO.output(LedPin, GPIO.HIGH)
##        time.sleep(T1p5)
##        GPIO.output(LedPin, GPIO.LOW)
##    else:
        #GPIO.output(LedPin, GPIO.HIGH)
        #time.sleep(0.0015625)
        #GPIO.output(LedPin, GPIO.LOW)
    global pCount
    if (pCount % 2 != 0):               #Even parity = low
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(T1p5)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(T1p5)

    else:
        GPIO.output(LedPin, GPIO.LOW)   #Odd parity = high    
        time.sleep(T1p5)                #Transition mode 2
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(T1p5)

    pCount = 0

def FOBO():
    blink()
    blink_init()
    idle()
    sync1()
    regBlink(0x04)
    regBlink(0xff)
    parity()
    idle()
    sync1()
    regBlink(0x05)
    regBlink(0xff)
    parity()
    idle()
    sync1()
    regBlink(0x06)
    regBlink(0xe0)
    parity()
    idle()
    sync1()
    regBlink(0x07)
    regBlink(0x00)
    parity()
    idle()
    sync1()
    regBlink(0x08)
    regBlink(0x03)
    parity()
    idle()
    sync1()
    regBlink(0x09)
    regBlink(0xff)
    parity()
    idle()
    sync1()
    regBlink(0x13)
    regBlink(0x10)
    parity()
    idle()
    sync1()
    regBlink(0x14)
    regBlink(0x08)
    parity()
    GPIO.output(LedPin, GPIO.LOW) #test
    time.sleep(2)

def Sleep():
    blink()
    blink_init()
    idle()
    sync1()
    regBlink(0x00)
    regBlink(0x00)
    parity()
    GPIO.output(LedPin, GPIO.LOW) #test
    time.sleep(2)
    

def destroy():
  GPIO.output(LedPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  global pCount
  try:
    while True:
        FOBO()

  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    Sleep()
    destroy()  


