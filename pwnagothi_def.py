import subprocess
import time
import os
from emotions import emotions

import logging

# Ustawienie logowania
logging.basicConfig(filename='activity.log', level=logging.INFO)

def run_airodump(interface, output_file):
    command = ["airodump-ng", "-w", output_file, "--output-format", "cap", interface]
    return subprocess.Popen(command)

def run_aircrack(capture_file, wordlist):
    command = ["aircrack-ng", "-w", wordlist, capture_file]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def check_handshake(capture_file):
    command = ["aircrack-ng", capture_file]
    result = subprocess.run(command, capture_output=True, text=True)
    if "1 handshake" in result.stdout:
        return True
    else:
        return False

def check_monitor_mode(interface):
    command = ["iwconfig", interface]
    result = subprocess.run(command, capture_output=True, text=True)
    if "Mode:Monitor" in result.stdout:
        return True
    else:
        return False

def set_monitor_mode(interface):
    down_command = ["ifconfig", interface, "down"]
    monitor_command = ["iwconfig", interface, "mode", "monitor"]
    up_command = ["ifconfig", interface, "up"]
    subprocess.run(down_command)
    subprocess.run(monitor_command)
    subprocess.run(up_command)