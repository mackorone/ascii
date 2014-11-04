# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys

# Two different ramps
ramp = ' .:-=+*#%@'
ramp = u' ░▒▓█'

def char_array_to_string(array):
    out = ''
    for r in range(len(array)):
        for c in range(len(array[0])):
            out += array[r][c] * 2
        out += '\n'
    return out

def get_char_from_ramp(pixel_array):
    percent_bright = np.mean(pixel_array)/255.0
    index = int(len(ramp)*percent_bright)
    return ramp[index]

# Specify the window size
window_rows = 12
window_cols = 12

# Infinity
cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read()
    output_rows = len(img)/window_rows
    output_cols = len(img[0])/window_cols
    output_array = [['0'] * output_cols for i in range(output_rows)]
    for r in range(output_rows):
        for c in range(output_cols):
            output_array[r][c] = get_char_from_ramp(img[r*window_rows, c*window_cols])
    print char_array_to_string(output_array)
