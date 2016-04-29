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
from time         import sleep
from random       import choice, randint
from ev3dev.auto  import *

# Bind two large motors plugged into PortB and PortC to motors
# and assert connection
motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]
assert all([m.connected for m in motors]), \
    "Two large motors should be connected to ports B and C"

# Instantiate infrared and touch sensors and assert connection
ir = InfraredSensor(); assert ir.connected
ts = TouchSensor();    assert ts.connected

# Set IR Sensor to proximity mode
ir.mode = 'IR-PROX'

# Instantiate button controller
btn = Button()

def start():
    """
    Starting Motors. Vroom Vroom!
    """
    for m in motors:
        m.run_direct()

def backup():
    """
    Avoiding obstacle.
    """

    # Sound backup alarm.
    Sound.tone([(1000, 500, 500)] * 3)

    # Turn backup lights on:
    for light in (Leds.LEFT, Leds.RIGHT):
        Leds.set_color(light, Leds.RED)

    # Stop both motors and reverse for 1.5 seconds.
    # `run-timed` command will return immediately, so we will have to wait
    # until both motors are stopped before continuing.
    for m in motors:
        m.stop(stop_command='brake')
        m.run_timed(duty_cycle_sp=-50, time_sp=1500)

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
    power = choice([(1, -1), (-1, 1)])
    t = randint(250, 750)

    for m, p in zip(motors, power):
        m.run_timed(duty_cycle_sp=p*75, time_sp=t)

    # Wait until both motors are stopped:
    while any(m.state for m in motors):
        sleep(0.1)

def playMusic():
    subprocess.call(['/usr/bin/aplay', '~/GitHub/ilstu-ai-lego-cucaracha/assets/song.wav'], shell=True)

start()
while not btn.any():
  # Checking for obstacle with touch sensor
  if ts.value():
      # Ran into something,
      #   backup -> turn -> restart
      backup()
      turn()
      start()

  # Perceive and store proximity from ir sensor
  # and determine safe motor speed
  prox = ir.value()
  if prox > 60:
      # Good to go
      speed = 90
  else:
      # Something up ahead, be weary
      speed = 40

  # Update motors with determined speed
  for m in motors:
      m.duty_cycle_sp = speed

  sleep(0.1)


# At exit stop motors
for m in motors:
  m.stop()