#!/usr/bin/python

# cucaracha-playground.py
# -----------------------------------------------------------------------------
# Written by Tyler Lubbers and Julian Bracero
# Illinois State University, Introduction to Artificial Intelligence, IT340,
# Spring 2016
# -----------------------------------------------------------------------------
# This executable is used for general experimentation and familiarization with
# a Lego Mindstorms ev3 brick and the ev3dev Python bindings.
#
from time         import sleep
from random       import choice, randint
from ev3dev.auto  import *

# Bind two large motors plugged into PortB and PortC to motors
#motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]

# Bind infrared and touch to ir and ts, respectively
#ir = InfraredSensor(); assert ir.connected
#ts = TouchSensor();    assert ts.connected

# Infared in proximity mode lets you use things like d = ir.value(), if d > 50
# than move forward.
#ir.mode = 'IR-PROX'

# Bind buttons on the brick to btn, a Button() object is more like a
# button controller than a button.
btn = Button()

def start():
  Sound.speak("La cucaracha!");
  # Putting motors in rundirect lets you change speeds later
  #for m in motors
  #  m.rundirect()

def playMusic():
    # Eventually will incorporate song using Sound objects
    Sound.tone([(1000, 500, 500)] * 3)

start()
while not btn.any():
  start()
  playMusic()

# At exit stop motors
#for m in motors:
  #  m.stop()