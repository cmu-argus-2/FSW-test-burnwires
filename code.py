"""
Burn wire test script for Argus

WARNING: This code will ONLY work with v1.1 mainboards
v2 mainboards do not have these pin definitions in firmware
"""

import time
import digitalio
import board

# Set up relay
burn_relay = digitalio.DigitalInOut(board.RELAY_A)
burn_relay.direction = digitalio.Direction.OUTPUT

# Set up burnwire 1 (pin, duty cycle, frequency)
burn1 = pwmio.PWMOut(board.BURN1, 2 ** 1, 1000)

# EN relay for burnwires
burn_relay.value = True

while True:
    print("BURNNING")
    time.sleep(1)