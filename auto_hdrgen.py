import os
import subprocess

img_folder = "/home/hosovluc/Documents/GLARE METER/2025-11-30 Calibration Experiment/09_white_100"
output_name = os.path.basename(os.path.normpath(img_folder))
print(output_name)


cmds = [
    f'exiftool -overwrite_original -ISO=100 *.jpg',
    f'exiftool -overwrite_original -ISO -ApertureValue>FNumber *.jpg',
    f'exiftool -overwrite_original -FNumber=1.8 *.jpg'
]

for cmd in cmds:
    subprocess.run(cmd, cwd = img_folder, shell = True)
    

hdrgen_cmd = f'hdrgen ./test1_?.jpg -o {output_name}.hdr -r response_function.rsp -a -e -f -g'
subprocess.run(hdrgen_cmd, cwd = img_folder, shell = True)

print('Done')