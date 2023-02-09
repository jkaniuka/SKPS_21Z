#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ------------------------------------- Import required libraries ------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import arange, sin, pi
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal
from datetime import datetime
import socket
import sys
import threading
import logging
import time

# ------------------------------------------- Socket init connection --------------------------------------------------
IP = '192.168.18.94'
PORT = 8080

hostName = socket.gethostbyname( '0.0.0.0' )

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = (IP, PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind( ('', PORT) )

# sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)


# Wait for a connection ( BLOCKING )
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

print >>sys.stderr, 'connection from', client_address


# ------------------------------------- Global vars, settings, color, title, window dimensions ---------------------------
COLOR = '#e6e8eb'
global duty_cycle 
duty_cycle = 0.3 # initial duty_cycle value

win= Tk()
win.geometry("1250x550")
win.configure(background=COLOR)
win.title('SKPS 21Z - Kaniuka, Krasnodębski')

current_value = DoubleVar()

# ------------------------------------------------- Callbacks (PC -> RPi) --------------------------------------------------

def turn_led_on():
   connection.sendall("LED_ON")

def turn_led_off():
   connection.sendall("LED_OFF")

def set_new_PWM_val():
   msg = "PWM="+str(slider.get())
   connection.sendall(msg)

def pc_control():
   connection.sendall("PC_control")

def keypad_control():
   connection.sendall("Keypad_control")


# ------------------------------------------------- Thread for receiving data ----------------------------------------------

def read_socket():
   global duty_cycle
   while True:
      data = connection.recv(2) # Number of bytes to receive
      now = datetime.now() # timestamp
      date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

      # Otrzymujemy z RPI 2 znaki. RPi może wysłać 2 rodzaje wiadomości:
      # - aktualne wypełnienie PWM (2 znaki)
      # - powiadomienie o wciśnięciu przycisku (wciśnięty znak z klawiatury 4x4 + "_" = 2 znaki)

      # "A_", "B_", "C_" to robocze nazwy, bo nie pamiętałem, które przyciski wykorzystywaliśmy

      if data == "A_":
         msg = " A ; " + date_time 
         T.insert(END, msg + '\n')
         T.see(END)
      elif data == "B_":
         msg = " B ; " + date_time 
         T.insert(END, msg + '\n')
         T.see(END)
      elif data == "C_":
         msg = " C ; " + date_time 
         T.insert(END, msg + '\n')
         T.see(END)

      # Jeżeli nie jest przesyłane powiadominie o przycisku, to oznacza to, że odebrano aktualną wartość PWM
      # Aktualna wartość PWM (która jest również na LCD) jest rysowana na "oscyloskopie"

      elif data.isdigit() == True:
         duty_cycle = int(data)/100.0
         T.insert(END, data + '\n')
         T.see(END)



# -------------------------------------- GUI elements (text field, buttons, slider etc.) ------------------------------------------

# Create text widget and specify size.
T = Text(win, height = 25, width = 35)


slider = Scale(win, from_=0, to=100, orient=VERTICAL, variable=current_value, length = 200)
#slider.bind('<ButtonRelease-1>', updateValue) # można wysyłać PWM po samym przesunięciu na suwaku, ale guzik obok to rozsądniejsza opcja ;-)  



# Add an optional Label widget
Label(win, text= "Panel sterowania serwomechanizmem", font= ('Aerial 17 bold italic'), bg=COLOR).grid(row = 0, column = 2, sticky = "", pady = 2)


Label(win, text= "Dioda LED", font= ('Aerial 17 bold italic'), bg=COLOR).grid(row = 1, column = 0, sticky = "", pady = 2, columnspan = 2)
ttk.Button(win, text= "LED ON", command=turn_led_on).grid(row = 2, column = 0, sticky = "", pady = 2)
ttk.Button(win, text= "LED OFF", command=turn_led_off).grid(row = 2, column = 1, sticky = "", pady = 2)
Label(win, text= "   Serwomechanizm", font= ('Aerial 17 bold italic'), bg=COLOR).grid(row = 3, column =0, sticky = "", pady = 2, columnspan = 2)
ttk.Button(win, text= "PC", command=pc_control).grid(row = 4, column = 0, sticky = "", pady = 2)
ttk.Button(win, text= "KEYPAD", command=keypad_control).grid(row = 4, column = 1, sticky = "", pady = 2)
slider.grid(row = 5, column = 0, sticky = "", pady = 2)
ttk.Button(win, text= "PWM", command=set_new_PWM_val).grid(row = 5, column =1, sticky = "", pady = 2)
Label(win, text= "Archiwum (klawiatura)", font= ('Aerial 17 bold italic'), bg=COLOR).grid(row = 1, column = 3, sticky = "", pady = 2)
T.grid(row = 2, column = 3, sticky = "", pady = 2, rowspan = 5)


def runGUI():
   win.mainloop()


# -------------------------------------------------- Plot section ---------------------------------------------------------------------
fig = plt.Figure()
fig.patch.set_facecolor(COLOR)
fig.suptitle(u"Sygnał sterujący PWM", fontsize=16, fontweight="bold")
x = np.arange(0, 1, 0.001)        # x-array

def animate(i):
    global duty_cycle
    line.set_ydata((signal.square(2 * np.pi * 5 * (x+i/10.0), duty = duty_cycle) + 1)/2)  # update the data
    return line,

canvas = FigureCanvasTkAgg(fig, master=win)
canvas.get_tk_widget().grid(row = 1, column = 2, sticky = "", pady = 2, columnspan=1, rowspan = 5)

ax = fig.add_subplot(111)
line, = ax.plot(x, signal.square(2 * np.pi * 5 * x, duty = duty_cycle))
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=250, blit=False)
ax.set_ylim([-0.1, 1.1])


# ------------------------------------------------ Threads ------------------------------------------------------------------------------

def main():
    try:
      t1 = threading.Thread(target=read_socket)
      t1.daemon = True;
      t1.start()
      runGUI() # tkinter GUI runs as main thread !!!
    finally:
      connection.close()


if __name__=='__main__':
    main()


