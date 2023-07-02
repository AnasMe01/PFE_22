import serial
import string
import time

class OpenMV(object):

def init(self):
    self.ser = serial.Serial(’/dev/ttyAMA0’,baudrate=115200, timeout = 0.5)
    self.ser.flushInput();

def blob_xysize(self):

    blob_found = False
    blob_x = 0
    blob_y = 0
    blob_radius = 0
    w = 0

    self.ser.flushInput();
    line = self.ser.readline()
    words = string.split(line , “;”)
    if len(words) > 3:
        blob_found = True
        blob_x = int (words [0])
        blob_y = int (words [1])
        w = int (words [2])
        blob_radius = w

    else:
        blob_found = False
        blob_x = 0
        blob_y = 0
        blob_radius = 0
        w = 0


print(blob_found, blob_x, blob_y, blob_radius)

def main(self):
while True:
self.blob_xysize()

exit(1)
self.ser.close()
open_mv = OpenMV()
if name == “main”:
    open_mv.main()