import cv2
import os
import rawpy
import numpy as np

folder = "/home/hosovluc/Documents/2025-10-17/im"
img_path = []
exposures = np.array([130, 1611, 19970, 247498, 3066985], dtype = np.float32)
exposures = exposures/1_000_000.0

# finds all the dng files in folder
for filename in os.listdir(folder):
    if filename.endswith(".dng"):
        full_path = os.path.join(folder, filename)
        #print(full_path)
        img_path.append(full_path)
print(img_path)
img_path.sort()
print(img_path)

# demosaic raws
images = []
for filepath in img_path:
    with rawpy.imread(filepath) as raw:
        rgb = raw.postprocess(
            use_auto_wb = False,
            no_auto_bright = True,
            output_bps = 16,
            gamma = (1,1)
        )
        #rgb_float = rgb.astype(np.float32) / 65535.0
        rgb_8bit = (rgb / 256).astype(np.uint8) 
        images.append(rgb_8bit)

#print(cv2.__version__)
#print([f for f in dir(cv2) if 'Merge' in f])
# 'createMergeDebevec' in dir(cv2)


#images = images.sort(
# camera response function
calibrate = cv2.createCalibrateDebevec()
response = calibrate.process(images, exposures)

# merge to hdr
merge = cv2.createMergeDebevec() # create object
hdr = merge.process(images, exposures, response)

# write results
cv2.imwrite('mergedDB.hdr', hdr)

# # Normalize the HDR image to the range [0, 1] before tone mapping
# hdr_normalized = cv2.normalize(hdr, None, 0, 1, cv2.NORM_MINMAX)
# tonemap = cv2.createTonemap(gamma=2.2)  # You can tweak the gamma to adjust contrast
# 
# # Apply tone mapping
# jpeg = tonemap.process(hdr_normalized.copy())
# 
# # Scale the output to 0-255 and convert to uint8 for saving as an image
# jpeg = np.clip(jpeg * 255, 0, 255).astype(np.uint8)
# 
# # Save the tone-mapped image
# cv2.imwrite('result_tonemap.jpg', jpeg)

print('done')
#         
# tonemap = cv2.createTonemap()
# jpeg = tonemap.process(hdr.copy())
# 
# cv2.imwrite('result_tonemap.jpg', jpeg)

        
#filename = f"captures/raw_{i}.dng"
#img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)