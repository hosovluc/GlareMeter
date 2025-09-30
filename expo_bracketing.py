from picamera2 import Picamera2
from pprint import *
import os
import time

dir_name = "captures"
os.makedirs(dir_name, exist_ok = True) # create dir if doesnt exist

picam2 = Picamera2() # creating the object
config = picam2.create_preview_configuration(raw={"size":picam2.sensor_resolution}) #  use configuration for still img
picam2.configure(config)

# print(picam2.sensor_resolution) # get the possible resolution

# pprint(picam2.sensor_modes) # get more details about modes

picam2.start()
time.sleep(2) # stabilize the camera

num_img = 5
exposures = [4000000, 2000000, 500000, 125000, 31250, 8000, 2000, 500, 125]

for i , exp in enumerate(exposures):
    picam2.set_controls({"ExposureTime":exp, "AnalogueGain": 1.0})
    time.sleep(0.1)
        
    filename = f"captures/raw_{i}.dng"
    picam2.capture_file(filename, name="raw")
    print("Saved:", filename)


