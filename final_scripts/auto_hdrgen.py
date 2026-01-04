import os
import subprocess
import cv2
import numpy as np

img_folder = os.getcwd()
output_name = "output_hdrgen"



cmds = [
    f'exiftool -overwrite_original -ISO=100 *.jpg',
    f'exiftool -overwrite_original -FNumber=1.8 *.jpg'
]

for cmd in cmds:
    subprocess.run(cmd, cwd = img_folder, shell = True)
    

hdrgen_cmd = f'hdrgen ./test1_?.jpg -o {output_name}.hdr -r "/home/hosovluc/Documents/GLARE METER/Scripts/my_resp_func.rsp" -a -e -f -g'
#hdrgen_cmd = f'hdrgen ./test1_?.jpg -o {output_name}.hdr -r my_resp_func.rsp -a -e -f -g'
subprocess.run(hdrgen_cmd, cwd = img_folder, shell = True)

K = 9.15
hdr_file = f"{output_name}.hdr"
img = cv2.imread(hdr_file, cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)
img_corrected = img * K
cv2.imwrite(f"{output_name}_K.hdr", img_corrected)

pfilt_cmd = f'pfilt -1 -x 1000 -y 1000 {output_name}_K.hdr > {output_name}_resized.hdr'
subprocess.run(pfilt_cmd, cwd = img_folder, shell = True)

eval_cmd  = f'evalglare -vta -vv 180 -vh 180 -c vystup.hdr {output_name}_resized.hdr'
subprocess.run(eval_cmd, cwd = img_folder, shell = True)




print('Done')
