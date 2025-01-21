import pigpio
import json
import time
import argparse

PIN_BLUE = 19
PIN_GREEN = 18
PIN_RED = 13

JSON_DATA = None

def set_col(red, green, blue):
  pi.set_PWM_dutycycle(PIN_BLUE, blue)
  pi.set_PWM_dutycycle(PIN_GREEN, green)
  pi.set_PWM_dutycycle(PIN_RED, red)

def save_col_to_file(red, green, blue):
  JSON_DATA['data']['red'] = red
  JSON_DATA['data']['green'] = green
  JSON_DATA['data']['blue'] = blue
  writeJSON('lastMode.json', JSON_DATA)


def set_off():
  set_col(0,0,0)

def parseJSON(fileName):
   with open(fileName, 'r') as file:
      return json.load(file)

def writeJSON(filename, data):
  with open(filename, 'w') as file:
    json.dump(data, file, indent=4)


pi = pigpio.pi()

if not pi.connected:
    exit()



pi.set_PWM_frequency(PIN_BLUE, 255)
pi.set_PWM_frequency(PIN_GREEN, 255)
pi.set_PWM_frequency(PIN_RED, 255)

startupData = parseJSON('lastMode.json')
JSON_DATA = startupData

print("Starting with values: ", startupData['data']['red'], " ", startupData['data']['green'], " ", startupData['data']['blue'])
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

