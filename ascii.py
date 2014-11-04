# -*- coding: utf-8 -*-

import cv2
import sys

# Two different ramps
ramp = ' .:-=+*#%@'
ramp = u'█▓▒░ '

def pixel_to_char(pixel):
    brightness = pixel/255.0
    ramp_index = int(len(ramp)*brightness)
    return ramp[ramp_index]

compression_factor = 12
cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for row in range(len(img)/compression_factor):
        for col in range(len(img[0])/compression_factor):
            pixel = img[row*compression_factor][col*compression_factor]
            sys.stdout.write(pixel_to_char(pixel) * 2)
        sys.stdout.write('\n')
