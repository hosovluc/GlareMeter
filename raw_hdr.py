from picamera2 import Picamera2
import cv2
import numpy as np
import time
import os
import rawpy


# Create a directory to save captured images
os.makedirs("captures", exist_ok=True)

# initialize the camera 
picam2 = Picamera2()

# Configure camera with RAW output
camera_config = picam2.create_still_configuration(raw={"size": (2592, 1944)})  # adjust resolution if needed
picam2.configure(camera_config)
picam2.start()
time.sleep(2)  # give the camera time to initialize

# Define exposure times in microseconds
exposures = [500, 2000, 8000, 32000]  # 0.5ms, 2ms, 8ms, 32ms
images = []

for i, exp in enumerate(exposures):
    # Set exposure time and gain
    controls = {"ExposureTime": exp, "AnalogueGain": 1.0}
    picam2.set_controls(controls)
    time.sleep(0.5)  # short pause to apply exposure settings

    # Capture RAW image
    filename = f"captures/raw_{i}.dng"
    picam2.capture_file(filename, name="raw")
    print(f"Saved {filename}")

    # Load the captured image into OpenCV
    #img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    with rawpy.imread(filename) as raw:
        img = raw.postprocess(use_auto_wb=True, no_auto_bright=True, output_bps=16)  # 16-bit array
    images.append(img)

picam2.stop()

# Convert RAW images to 8-bit (normalization)
ldr_images = []
for img in images:
    img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    img_8bit = np.uint8(img_norm)
    ldr_images.append(img_8bit)

# Merge exposures into HDR image (Debevec algorithm)
merge_debevec = cv2.createMergeDebevec()
hdr = merge_debevec.process(ldr_images, times=np.array([1.0/e for e in exposures], dtype=np.float32))

# Tonemapping: convert HDR to 8-bit displayable image
tonemap = cv2.createTonemap(gamma=2.2)
ldr = tonemap.process(hdr)
ldr_8bit = np.clip(ldr * 255, 0, 255).astype('uint8')

# Save the final HDR result
cv2.imwrite("hdr_result.jpg", ldr_8bit)
print("HDR image saved as hdr_result.jpg")


