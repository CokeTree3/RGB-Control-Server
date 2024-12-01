import pigpio
import json
import time
import argparse

PIN_BLUE = 19
PIN_GREEN = 18
PIN_RED = 13

def set_col(red, green, blue):
  pi.set_PWM_dutycycle(PIN_BLUE, blue)
  pi.set_PWM_dutycycle(PIN_GREEN, green)
  pi.set_PWM_dutycycle(PIN_RED, red)

def set_off():
  set_col(0,0,0)

def parseJSON(fileName):
   with open(fileName, 'r') as file:
      return json.load(file)

pi = pigpio.pi()

if not pi.connected:
    exit()



pi.set_PWM_frequency(PIN_BLUE, 255)
pi.set_PWM_frequency(PIN_GREEN, 255)
pi.set_PWM_frequency(PIN_RED, 255)

startupData = parseJSON('lastMode.json')

print(startupData['data']['red'])
set_col(startupData['data']['red'], startupData['data']['green'], startupData['data']['blue'])
'''
set_col(255,255,255)
time.sleep(1)
set_col(100,255,255)
time.sleep(1)
set_col(25,255,255)
time.sleep(4)
set_col(0,255,0)

set_off()

pi.stop()
'''

