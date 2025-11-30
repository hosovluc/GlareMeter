# === Capture bracketing RAWs ===
# Author: Lucie Hosova
# Date: 17-10-2025

from picamera2 import Picamera2
from pprint import *
import os
import time
import cv2

# Folder for raw data
dirname = "imgs"
os.makedirs(dirname, exist_ok = True) # create dir if doesnt exist

# Camera settings
picam2 = Picamera2() # creating the object
mode = picam2.sensor_modes[3]
config = picam2.create_still_configuration(raw={'format': 'SRGGB10'},
                                           sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']},
                                           controls={
                                                "AwbEnable": False, # disables automatic white balance
                                                "AeEnable": False, # disables automatic exposure
                                                "ExposureTime": 1000, # in microseconds, (130, 3066985, 20000) referes to settings in mode 
                                                "AnalogueGain": 1.0 }) # equivalent to a ISO, without any amplification                                         
picam2.configure(config)

# config = picam2.create_preview_configuration(raw={"size":picam2.sensor_resolution}) #  use configuration for still img

picam2.start()
time.sleep(2) # stabilize the camera, sleep always in seconds

num_img = 5
# ex = [140, 1703, 20721, 252095, 3066975] # exposure times in microseconds
exp = [130, 1611, 19970, 247498, 3066985]

for i in range(0, num_img):
    picam2.set_controls({"ExposureTime":exp[i]})
    #time.sleep(2*exp[i]/1e6) # wait 2-3 frames to apply the changes
    time.sleep(4)
    #print(2*exp[i]/1e6)
    print("Exp:",exp[i])
    
    # Capture and save RAW (.dng)   
    filename = f"TEST_{i}.dng"
    full_path = os.path.join(dirname, filename)
    picam2.capture_file(full_path, name="raw")
#   raw_array = picam2.capture_array("raw")
#   cv2.imwrite(filename, raw_array)
    print("Saved:", filename)
    
    meta = picam2.capture_metadata()
    print("ExposureTime:", meta["ExposureTime"])
    
    # Capture and save JPEG
    filename = f"test1_{i}.jpg"
    full_path = os.path.join(dirname, filename)
    picam2.capture_file(full_path)
    print("Saved:", filename)
    
    meta = picam2.capture_metadata()
    print("ExposureTime:", meta["ExposureTime"])



