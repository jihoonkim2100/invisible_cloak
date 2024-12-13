# Author: jihoonkim2100
# Last updated: 13 December 2024
# References: 
# https://github.com/kaustubh-sadekar/Invisibility_Cloak
# https://github.com/Aayushi-Mittal/Invisible-Cloak/blob/main/invisible_cloak.py

import cv2
import numpy as np
import time

print(f'{"#"*29}')
print('#   RUN INVISIBLE CLOAK     #')
print(f'{"#"*29}')

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0

for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while(cap.isOpened()):
    ret, img = cap.read()

    # flip the image (can be uncommented if needed)
    img = np.flip(img, axis=1)

    # convert image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)

    blurred = cv2.GaussianBlur(hsv, value,0)

    # define lower range for red color detection
    lower_red = np.array([0, 120, 70]) # 0, 120, 70
    upper_red = np.array([10, 255, 255]) # 10, 255, 255
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # define upper range for red color detection
    lower_red = np.array([170, 120, 70]) # 170, 120, 70
    upper_red = np.array([180, 255, 255]) # 180, 255, 255
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # combine both masks
    mask = cv2.bitwise_or(mask1, mask2)

    # morphological operation to remove small noise in the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # replace pixels corresponding to cloak with the background
    img[np.where(mask==255)] = background[np.where(mask==255)]

    # img[mask == 255] = [0, 255, 0]

    cv2.imshow('Invisible Cloak', img)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()