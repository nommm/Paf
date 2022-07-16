    
    import ir
    import analog_controls
    import RaspConfig
    import RPi.GPIO as GPIO
    import time
    import sys
    import math
    import controls
#importing the necessary modules
analog = analog_controls.analog()
ir = ir.IR()
bot = controls.Controls()
#assigning objects to various classes from different modules
class odometer:
    
    try:
        def __init__(self):
            """
            """

        def measure(self):
            count = 0
            while True:
               bot.Forward()
               #makes the bot move forward
               #ir.Get() is used to return the value of the ir sensor module which is either 0 or 1
               while (ir.Get() == 0):
                    print("Detected\nIr value : ", ir.Get())
                    print(count)
                    if (ir.Get() == 0):
                        count = count
                    else:
                        count += 1
               if count>10:
                    bot.Stop()
                    # used to stop the bot
                    break
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()



if __name__ == '__main__':
    odo = odometer()
    odo.measure()
        
    GPIO.cleanup()


GPIO.cleanup()