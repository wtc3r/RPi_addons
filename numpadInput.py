import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# define numpad layout matrix
MATRIX = [['1','2','3'],
          ['4','5','6'],
          ['7','8','9'],
          ['*','0','#']]
# used pins
col = [16,20,21]
row = [6,13,19,26]
# set row pins as input
for j in range(4):
    GPIO.setup(row[j], GPIO.IN, pull_up_down = GPIO.PUD_UP)
# set col pins high
for i in range(3):
    GPIO.setup(col[i], GPIO.OUT)
    GPIO.output(col[i], 1)
# scroll through columns and when a column pin is pulled low do some action
try:
    while(True):
        for j in range(3):
            GPIO.output(col[j],0)
            
            for i in range(4):
                if GPIO.input(row[i]) == 0:
                    # some action
                    print(MATRIX[i][j])
                    # while the button is pressed don't do anyting (pass)
                    while(GPIO.input(row[i]) == 0):
                        pass
            # reset status of column pin to high        
            GPIO.output(col[j],1)
# reset GPIO pins        
except KeyboardInterrupt:
    GPIO.cleanup()