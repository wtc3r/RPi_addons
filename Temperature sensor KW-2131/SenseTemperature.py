#connect DS18B20 to 3.3V, GND and a GPIO pin
#place a 4700 Ohm resistor between 3.3V and the GPIO pin

#sudo raspi-config
#Interfacing options
#enable 1-wire interface
#reboot

#lsmod | grep -i w1_
#should show:
#w1_therm    28672 0
#w1_gpio     16384 0
#wire        36864 2 w1_gpio,w1_therm

#python script:

import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
while True:
    # infinite loop!
    print(read_temp())
    time.sleep(1)
    
def read_temp_raw():
    catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out,err = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines