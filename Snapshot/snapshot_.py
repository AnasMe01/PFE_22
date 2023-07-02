import json,rcpRPI,serial,serial.tools.list_ports,struct,sys
from unittest import result
from datetime import datetime

print("\nAvailable Ports:\n")
for port, desc, hwid in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(port, desc, hwid))
sys.stdout.write("\nPlease enter a port name: ")
sys.stdout.flush()

interface = rcpRPI.rcp_usb_vcp_master(port=input())
print("")
sys.stdout.flush

def exe_jpeg_snapshot():
    result = interface.call("jpeg.snapshot")
    if result is not None:
        name ="snapshot-%s.jpg"%datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
        print("writing jpeg %s..." % name)
        with open(name, "wb") as snap:
            snap.write(result)

while(True):
    exe_jpeg_snapshot()