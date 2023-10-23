import supervisor
from time import sleep, monotonic
import board
import neopixel
import random

# Configure the setup
PIXEL_PIN = board.A1  # pin that the NeoPixel is connected to
ORDER = neopixel.RGB  # pixel color channel order
GREEN = (0,255,0)  # color to blink
RED = (255,0,0)
BLUE = (0,0,255)
COLOR = (255,255,255)
CLEAR = (0, 0, 0)  # clear (or second color)

#sample buddy maps
ERROR_SIGN = [52,53,54,55,43,42,41,40,30,29,65,66]


CELLS = {'H01' : 0 ,
'H02' : 1 ,
'H03' : 2 ,
'H04' : 3 ,
'H05' : 4 ,
'H06' : 5 ,
'H07' : 6 ,
'H08' : 7 ,
'H09' : 8 ,
'H10' : 9 ,
'H11' : 10 ,
'H12' : 11 ,
'G01' : 23 ,
'G02' : 22 ,
'G03' : 21 ,
'G04' : 20 ,
'G05' : 19 ,
'G06' : 18 ,
'G07' : 17 ,
'G08' : 16 ,
'G09' : 15 ,
'G10' : 14 ,
'G11' : 13 ,
'G12' : 12 ,
'F01' : 24 ,
'F02' : 25 ,
'F03' : 26 ,
'F04' : 27 ,
'F05' : 28 ,
'F06' : 29 ,
'F07' : 30 ,
'F08' : 31 ,
'F09' : 32 ,
'F10' : 33 ,
'F11' : 34 ,
'F12' : 35 ,
'E01' : 47 ,
'E02' : 46 ,
'E03' : 45 ,
'E04' : 44 ,
'E05' : 43 ,
'E06' : 42 ,
'E07' : 41 ,
'E08' : 40 ,
'E09' : 39 ,
'E10' : 38 ,
'E11' : 37 ,
'E12' : 36 ,
'D01' : 48 ,
'D02' : 49 ,
'D03' : 50 ,
'D04' : 51 ,
'D05' : 52 ,
'D06' : 53 ,
'D07' : 54 ,
'D08' : 55 ,
'D09' : 56 ,
'D10' : 57 ,
'D11' : 58 ,
'D12' : 59 ,
'C01' : 71 ,
'C02' : 70 ,
'C03' : 69 ,
'C04' : 68 ,
'C05' : 67 ,
'C06' : 66 ,
'C07' : 65 ,
'C08' : 64 ,
'C09' : 63 ,
'C10' : 62 ,
'C11' : 61 ,
'C12' : 60 ,
'B01' : 72 ,
'B02' : 73 ,
'B03' : 74 ,
'B04' : 75 ,
'B05' : 76 ,
'B06' : 77 ,
'B07' : 78 ,
'B08' : 79 ,
'B09' : 80 ,
'B10' : 81 ,
'B11' : 82 ,
'B12' : 83 ,
'A01' : 95 ,
'A02' : 94 ,
'A03' : 93 ,
'A04' : 92 ,
'A05' : 91 ,
'A06' : 90 ,
'A07' : 89 ,
'A08' : 88 ,
'A09' : 87 ,
'A10' : 86 ,
'A11' : 85 ,
'A12' : 84  }

# Create the NeoPixel object
pixels = neopixel.NeoPixel(PIXEL_PIN, 96, brightness=1,  pixel_order=ORDER)


def clear_pixels():
        for i in range(len(pixels)):
             pixels[i] = CLEAR


def new_input(cmd):
        print(cmd)
        clear_pixels()
        well = CELLS.get(cmd)
        if well is not None:
            pixels[well] = BLUE
            return
        
        if cmd == "ERROR":
             for i in ERROR_SIGN:
                  pixels[i] = RED
        


'''

Main loop start

'''

delay = 10

timer = monotonic()


while True:
    #clears the LEDs after no input for delay amount of time
    if timer < monotonic():
         clear_pixels()

    value = ''
    if supervisor.runtime.serial_bytes_available:
        value = input()
    if value == "":
        continue
    else:
        new_input(value.upper())
        timer = monotonic() + delay
    