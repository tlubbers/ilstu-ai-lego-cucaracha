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

# Binding two large motors plugged into PortB and PortC
# motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]

def start():
  Sound.speak("La cucaracha!");
  for m in motors
    m.rundirect()