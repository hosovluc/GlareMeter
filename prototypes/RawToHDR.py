# === Creating HDR file from multiple RAW images with different exposure  ===
# Author: Lucie Hosova
# Date: 17-10-2025
# ======================
import rawpy
import os 
import numpy as np
import exifread
import cv2
import re

dirname = "img_files"

img_path = []
# Find all .dng files
for filename in os.listdir(dirname):
    if filename.endswith(".dng"):
        full_path = os.path.join(dirname, filename)
        img_path.append(full_path)
img_path.sort()


# Load RAw data and demosaic
images = []
exposures = []
for filepath in img_path:
    with rawpy.imread(filepath) as raw:
#         bayer = raw.raw_image
#         print(bayer.shape, bayer.dtype)
    
        demosaiced = raw.postprocess(
                use_auto_wb = False,
                no_auto_bright = True,
                output_bps = 16,
                gamma = (1,1)
                )
        print(demosaiced.shape, demosaiced.dtype)
        rgb_8bit = (demosaiced / 256).astype(np.uint8) # from 16 bit to 8 bit
        images.append(rgb_8bit)
        
#     with open(filepath, "rb") as f:
#         tags = exifread.process_file(f)
#         #print(tags)
#         expo = tags.get("Image ExposureTime", "N/A")
#         exposures.append(float(expo.values[0])) # exposures in seconds
# nespolehlive !!!  -> vezmu z fotku capture pozdeji
        
exp = [140, 1703, 20721, 252095, 3066975] # exposure times in microseconds
exp_seconds = np.array(exp)/1e6
#print(exp)
# Preprocessing

# Merge to HDR
debevec = cv2.createMergeDebevec() # create object
merged_hdr = debevec.process(images, exp_seconds)
#print(type(merged_hdr))

# Save HDR file
filename = 'merge.hdr'
full_path = os.path.join(dirname, filename)

cv2.imwrite(full_path, merged_hdr)




