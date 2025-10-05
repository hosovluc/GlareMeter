import cv2
import os
import rawpy
import numpy as np

folder = "captures"
img_path = []
exposures = [4000000, 2000000, 500000, 125000, 31250, 8000, 2000, 500, 125]

# finds all the dng files in folder
for filename in os.listdir(folder):
    if filename.endswith(".dng"):
        full_path = os.path.join(folder, filename)
        print(full_path)
        img_path.append(full_path)
print(img_path[1])

images = []
for filepath in img_path:
    with rawpy.imread(filepath) as raw:
        rgb = raw.postprocess(
            use_auto_wb = False,
            no_auto_bright = True,
            output_bps = 16,
            gamma = (1,1)
        )
        rgb_float = rgb.astype(np.float32) / 65535.0
        images.append(rgb_float)
        
                              
        
    
        
#filename = f"captures/raw_{i}.dng"
#img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)