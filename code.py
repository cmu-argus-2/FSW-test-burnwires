"""
Burn wire test script for Argus

WARNING: This code will ONLY work with v1.1 mainboards
v2 mainboards do not have these pin definitions in firmware
"""

import time

import board
import digitalio
import pwmio

# Set up relay
burn_relay = digitalio.DigitalInOut(board.RELAY_A)
burn_relay.direction = digitalio.Direction.OUTPUT

# EN relay for burnwires
burn_relay.value = True

time.sleep(5)

# Set up burnwire 1 (pin, duty cycle, frequency)
burn1 = pwmio.PWMOut(board.BURN1, duty_cycle = int(0.05 * 65536), frequency = 200)
burn2 = pwmio.PWMOut(board.BURN2, duty_cycle = int(0.05 * 65536), frequency = 200)

for i in range(0, 5):
    print("BRUNIGNINGINGIN")
    time.sleep(1)

