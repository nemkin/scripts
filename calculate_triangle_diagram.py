import numpy as np 
import cv2 

width = 400
height = 300
  
img = np.zeros((height, width, 3), np.uint8) 
 
length = 200
ax, ay = 0, 0
a_count_min = 6
b_count_min = 5
c_count_min = 3
max_count = 20


a_count_max = max_count - b_count_min - c_count_min
b_count_max = max_count - a_count_min - c_count_min
c_count_max = max_count - a_count_min - b_count_min

a_dist_min = a_count_min / max_count * length * np.sqrt(3) / 2
b_dist_min = b_count_min / max_count * length * np.sqrt(3) / 2
c_dist_min = c_count_min / max_count * length * np.sqrt(3) / 2

a_dist_max = a_count_max / max_count * length * np.sqrt(3) / 2
b_dist_max = b_count_max / max_count * length * np.sqrt(3) / 2
c_dist_max = c_count_max / max_count * length * np.sqrt(3) / 2

bx = ax + length
by = ay

cx = ax + length / 2
cy = ay + np.sqrt(3) / 2 * length

kx = ax + c_dist_min / np.sqrt(3) + b_dist_min / np.sqrt(3) * 2
ky = ay + c_dist_min 

lx = bx - c_dist_min / np.sqrt(3) - a_dist_min / np.sqrt(3) * 2
ly = ay + c_dist_min 

jx = (kx + lx) / 2
jy = ay + c_dist_max


cv2.fillPoly(img, pts = np.array([[(int(ax), int(ay)),(int(bx), int(by)), (int(cx), int(cy))]], dtype=np.int32), color=(255,0,0)) 
cv2.fillPoly(img, pts = np.array([[(int(kx), int(ky)),(int(lx), int(ly)), (int(jx), int(jy))]], dtype=np.int32), color=(0,255,0)) 

cv2.imwrite('/mnt/c/Users/vikto/Desktop/image.jpg', img)
