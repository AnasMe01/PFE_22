import curses,serial,time,os,subprocess
import json,rpc,serial.tools.list_ports,struct,sys
from datetime import datetime
from curses.textpad import Textbox, rectangle


def portUsB():
  print("\nAvailable Ports:\n")
  for port, desc, hwid in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(port, desc, hwid))


portUsB()
arduino = serial.Serial(port=input(),baudrate=115200,time=.1)
input = curses.initscr()
curses.noecho()
curses.cbreak()
input.keypad(True)
#set Remot Text
input.addstr(0,0,"Welcome to the remot control over our zumo robot :")
input.addstr(1,2,"Moving forward : KEY_UP or 'i' key")
input.addstr(2,2,"Moving backward : KEY_DOWN or 'k' key")
input.addstr(3,2,"A left turn : KEY_LEFT or 'j' key")
input.addstr(4,2,"A right turn : KEY_RIGHT or 'l' key")
input.addstr(5,2,"Stop : 'a' key")
input.addstr(6,2,"Capture an image : 'w' key")
input.addstr(7,2,"Increase speed by 50 : 'z' key")
input.addstr(8,2,"Decrease speed by 50 : 'e' key")
input.addstr(9,2,"turn right until stopped : 's' key")
input.addstr(10,2,"turn left until stopped : 'd' key")
input.addstr(11,2,"Quit : 'q' key")
input.addstr(12,2,"the chosen option")

while True:
    c = input.getch()
    if c == curses.KEY_UP or c == ord('i'):
        arduino.write(bytes("1","utf-8"))
        input.addstr(15,0,"UP")
    elif c == curses.KEY_DOWN or c == ord('k'):
        arduino.write(bytes("2","utf-8"))
        input.addstr(15,0,"DOWN")
    elif c == curses.KEY_LEFT or c == ord('j'):
        arduino.write(bytes("3","utf-8"))
        input.addstr(15,0,"LEFT")
    elif c == curses.KEY_RIGHT or c == ord('l'):
        input.addstr(15,0,"RIGHT")
        arduino.write(bytes("4","utf-8"))
    elif  c == ord('s'):
        input.addstr(15,0,"Turn right")
        arduino.write(bytes("8","utf-8"))
    elif  c == ord('d'):
        input.addstr(15,0,"Turn left")
        arduino.write(bytes("9","utf-8"))
    elif  c == ord('w'):
         input.addstr(15,0,"choise one of the available ports")
         input.addstr(16,0,"Available Ports : ")

         for port, desc, hwid in serial.tools.list_ports.comports():
             input.addstr(17,0,"{} : {} [{}]".format(port, desc, hwid))
         editwin = curses.newwin(5,30,18,2)

         input.refresh()
         box = Textbox(editwin)
         #let the user edit until Ctrl-G is Struck
         box.edit()
         #Get resulting contents
         port_ = box.gather()
         snapshot.exe_jpeg_snaphot(port_)
         

    #Speed Part 
    elif  c == ord('a'):
        arduino.write(bytes("5","utf-8"))
        input.addstr(15,0,"Stop")
    elif  c == ord('z'):
        arduino.write(bytes("6","utf-8"))
        input.addstr(15,0,"Speed Increased")
    elif  c == ord('e'):
        arduino.write(bytes("7","utf-8"))
        input.addstr(15,0,"Speed Increased")
    elif  c == ord('q'):
        break # Exit the While loop
    elif c == curses.KEY_HOME:
        x = y = 0
        
  


