#!/usr/bin/python

# -----------------------------------------------------------------------------
# cucaracha-playground.py
# -----------------------------------------------------------------------------
# Written by Tyler Lubbers and Julian Bracero
# Illinois State University, Introduction to Artificial Intelligence, IT340,
# Spring 2016
#
# -----------------------------------------------------------------------------
# This executable is used for general experimentation and familiarization with
# a Lego Mindstorms ev3 brick and the ev3dev Python bindings.
#
# -----------------------------------------------------------------------------
import subprocess
import os
from time         import sleep
from random       import choice, randint
from ev3dev.auto  import *

# Bind two large motors plugged into PortB and PortC to motors
# and assert connection
motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]
assert all([m.connected for m in motors]), \
    "Two large motors should be connected to ports B and C"

# Instantiate infrared and touch sensors and assert connection
us = UltrasonicSensor();  assert us.connected
ts = TouchSensor();       assert ts.connected
ls = ColorSensor();       assert ls.connected

# Set IR Sensor to proximity mode
us.mode = 'US-DIST-IN'
ls.mode = 'COL-AMBIENT'

# Instantiate button controller
btn = Button()
retreating = False
light = -1

def start():
    """
    Starting Motors. Vroom Vroom!
    """
    for m in motors:
        m.run_direct()
    light = ls.value()

def backup():
    """
    Avoiding obstacle.
    """

    # Sound backup alarm.
    Sound.speak("Ouuuuuuuuuuuch")
    sleep(1.0)

    # Turn backup lights on:
    for light in (Leds.LEFT, Leds.RIGHT):
        Leds.set_color(light, Leds.RED)

    # Stop both motors and reverse for 1.5 seconds.
    # `run-timed` command will return immediately, so we will have to wait
    # until both motors are stopped before continuing.
    for m in motors:
        m.stop(stop_command='brake')
        m.run_timed(duty_cycle_sp=-20, time_sp=1000)

    # When motor is stopped, its `state` attribute returns empty list.
    # Wait until both motors are stopped:
    while any(m.state for m in motors):
        sleep(0.1)

    # Turn backup lights off:
    for light in (Leds.LEFT, Leds.RIGHT):
        Leds.set_color(light, Leds.GREEN)

def turn():
    """
    Turning
    """

    # We want to turn the robot wheels in opposite directions from 1/4 to 3/4
    # of a second. Use `random.choice()` to decide which wheel will turn which
    # way.
    power = (1, -1)
    t = 200

    for m, p in zip(motors, power):
        m.run_timed(duty_cycle_sp=p*75, time_sp=t)

    # Wait until both motors are stopped:
    while any(m.state for m in motors):
        sleep(0.1)

def playMusic():
  os.system("aplay assets/song.wav")

def retreat():
  retreating = True
  power = (1, -1)
  t = 1000
  for m in motors:
        m.stop(stop_command='brake')
  Sound.speak("Oh No! Run!")

  sleep(2.0)
  for m, p in zip(motors, power):
      m.run_timed(duty_cycle_sp=p*75, time_sp=t)

  # Wait until both motors are stopped:
  while any(m.state for m in motors):
      sleep(0.1)


start()
while not btn.any():
  print ls.value()
  # Checking for obstacle with touch sensor\
  if light > 0:
    if ls.value() - light > 5:
      retreat()
      start()

  light = ls.value()
  if light <  2:
    break

  if ts.value():
      # Ran into something,
      #   backup -> turn -> restart
      retreating = False
      backup()
      turn()
      start()

  # Perceive and store proximity from ir sensor
  # and determine safe motor speed
  prox = us.value()

  if prox > 60:
      # Good to go
      speed = 50
  else:
      # Something up ahead, be weary
      speed = 30

  # If retreating, full speed ahead
  if retreating:
    speed = 90
  # Update motors with determined speed
  for m in motors:
      m.duty_cycle_sp = speed

  sleep(0.1)


# At exit stop motors
for m in motors:
  m.stop()

sleep(0.1)
playMusic()