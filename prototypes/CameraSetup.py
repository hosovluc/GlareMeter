# === Camera Setup - usefull commands to get know your device ===
# Author: Lucie Hosova
# Date: 17-10-2025

from pprint import *
from picamera2 import Picamera2

picam2 = Picamera2()

# write into shell or use pprint
pprint(picam2.sensor_modes)
mode
picam2.camera_configuration()['raw']
pprint(picam2.camera_controls) # see all the camera controls

# packed version of configuration
mode = picam2.sensor_modes[3]
config = picam2.create_still_configuration(sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']})
picam2.configure(config)

# unpacked version, more detailed 
mode = picam2.sensor_modes[3]
config = picam2.create_still_configuration(raw={'format': 'SRGGB10'},
                                           sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']},
                                           controls={
                                                "AwbEnable": False, # disables automatic white balance
                                                "AeEnable": False, # disables automatic exposure
                                                "ExposureTime": 1000, # in microseconds, (130, 3066985, 20000) referes to settings in mode 
                                                "AnalogueGain": 1.0 }) # equivalent to a ISO, without any amplification
                                                
picam2.configure(config)

