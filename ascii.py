import curses
import cv2
import os
import sys

# TODO: Use less CPU

# Returns the number of rows and columns of characters
def get_winsize():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

def pixel_to_char(pixel):
    ramp = ' .:-=+*#%@'
    brightness = pixel/255.0
    ramp_index = int(len(ramp)*brightness)
    return ramp[ramp_index]

def main(arg):

    # Initialize curses and turn off blinking curser
    curses.initscr()
    curses.curs_set(0)

    rows, columns = get_winsize()
    win = curses.newwin(rows, columns, 0, 0)

    cap = cv2.VideoCapture(0)
    win.refresh()

    ret, img = cap.read()
    compression_factor = max(len(img)/rows, len(img[0])/columns)

    def draw(img):
        for row in range(len(img)/compression_factor):
            for col in range(len(img[0])/compression_factor):
                if curses.is_term_resized(rows, columns):
                    return
                try:
                    pixel = img[row*compression_factor][col*compression_factor]
                    char = pixel_to_char(pixel)
                    win.addch(row, col, char)
                except:
                    pass
        
    while True:
        ret, img = cap.read()
        draw(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        if curses.is_term_resized(rows, columns):
            rows, columns = get_winsize() 
            win = curses.newwin(rows, columns, 0, 0)
            compression_factor = max(len(img)/rows, len(img[0])/columns)
        win.refresh()

curses.wrapper(main)
