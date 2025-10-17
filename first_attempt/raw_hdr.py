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
images1 = []

for i, exp in enumerate(exposures):
    # Set exposure time and gain
    controls = {"ExposureTime": exp, "AnalogueGain": 1.0}
    # print(exp, i)
    picam2.set_controls(controls)
    time.sleep(0.5)  # short pause to apply exposure settings

    # Capture RAW image
    filename = f"captures/Tadyraw_{i}.dng"
    picam2.capture_file(filename, name="raw")
    print(f"Saved {filename}")
    
picam2.stop()


# Load the captured image into OpenCV
#img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
#print(filename, np.size(img))

# rawko = np.fromfile(filename, dtype=np.uint16)
# print(rawko.shape)
for file in range (0, len(exposures)):
    print(file)
    filename = f"captures/Tadyraw_{file}.dng"
    with rawpy.imread(filename) as raw:
        img_16bit = raw.postprocess(use_auto_wb=False, no_auto_bright=True, output_bps=16, gamma = (1,1))  # 16-bit array
        print(np.shape(img_16bit)) # (1944, 2592, 3)
        #rgb = img.astype(np.float32) / 65535.0
        #images.append(rgb)
        #print(np.shape(rgb))
        img_8bit = (img_16bit / 256).astype(np.uint8)  # 65535 / 256 = 255
        images.append(img_8bit)
        print(np.shape(images))
        images1.append(img_16bit.astype(np.uint16))  # OK
# 
# picam2.stop()
# 
# # # Convert RAW images to 8-bit (normalization)
# # ldr_images = []
# # for img in images:
# #     img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
# #     img_8bit = np.uint8(img_norm)
# #     ldr_images.append(img_8bit)
# 
# 
# ldr_images = images



# Merge exposures into HDR image (Debevec algorithm)
merge_debevec = cv2.createMergeDebevec()
hdr = merge_debevec.process(images, times=np.array([1.0/e for e in exposures], dtype=np.float32))
# 
cv2.imwrite('halooo.hdr', hdr)
# 
# # Tonemapping: convert HDR to 8-bit displayable image
# tonemap = cv2.createTonemap(gamma=2.2)
# ldr = tonemap.process(hdr)
# ldr_8bit = np.clip(ldr * 255, 0, 255).astype('uint8')
# 
# # Save the final HDR result
# cv2.imwrite("hdr_result.jpg", ldr_8bit)
# print("HDR image saved as hdr_result.jpg")


