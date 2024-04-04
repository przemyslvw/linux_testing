import subprocess
import time
import random

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

# Komunikaty aktywności
emotions = {
    "LOOK_R": "( ⚆_⚆)",
    "GRATEFUL": "(^‿‿^)",
    "LOOK_L": "(☉_☉ )",
    "EXCITED": "(ᵔ◡◡ᵔ)",
    "LOOK_R_HAPPY": "( ◕‿◕)",
    "MOTIVATED": "(☼‿‿☼)",
    "LOOK_L_HAPPY": "(◕‿◕ )",
    "DEMOTIVATED": "(≖__≖)",
    "SLEEP": "(⇀‿‿↼)",
    "SMART": "(✜‿‿✜)",
    "SLEEP2": "(≖‿‿≖)",
    "LONELY": "(ب__ب)",
    "AWAKE": "(◕‿‿◕)",
    "SAD": "(╥☁╥ )",
    "BORED": "(-__-)",
    "ANGRY": "(-_-')",
    "INTENSE": "(°▃▃°)",
    "FRIEND": "(♥‿‿♥)",
    "COOL": "(⌐■_■)",
    "BROKEN": "(☓‿‿☓)",
    "HAPPY": "(•‿‿•)"
}

# Przykładowe użycie
while True:
        print(emotions["EXCITED"])  # Wyświetl komunikat "EXCITED"
        logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - EXCITED - Started capturing packets')
        airodump_process = run_airodump("wlan0", "capture")
        time.sleep(60)  # Przechwytuj pakiety przez 60 sekund
        airodump_process.kill()  # Zakończ przechwytywanie pakietów
        logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - EXCITED - Stopped capturing packets')

        print(emotions["INTENSE"])  # Wyświetl komunikat "INTENSE"
        logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - INTENSE - Started cracking password')
        result = run_aircrack("capture-01.cap", "/path/to/wordlist.txt")
        print(result)
        logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - INTENSE - Finished cracking password: {result}')