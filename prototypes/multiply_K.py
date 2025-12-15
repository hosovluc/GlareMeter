import cv2
import numpy as np

K = 9.15

img = cv2.imread("04_100.hdr", cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)

img_corrected = img * K

cv2.imwrite("outputPy.hdr", img_corrected)
