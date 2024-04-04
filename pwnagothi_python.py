import subprocess
import time
import random

def run_airodump(interface, output_file):
    command = ["airodump-ng", "-w", output_file, "--output-format", "cap", interface]
    return subprocess.Popen(command)

def run_aircrack(capture_file, wordlist):
    command = ["aircrack-ng", "-w", wordlist, capture_file]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def should_capture():
    # Prosta logika decyzyjna: przechwytuj pakiety z 50% szansą
    return random.random() < 0.5

def should_crack():
    # Prosta logika decyzyjna: próbuj złamać hasło z 50% szansą
    return random.random() < 0.5

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
    if should_capture():
        print(emotions["EXCITED"])  # Wyświetl komunikat "EXCITED"
        airodump_process = run_airodump("wlan0", "capture")
        time.sleep(60)  # Przechwytuj pakiety przez 60 sekund
        airodump_process.terminate()  # Zakończ przechwytywanie pakietów

    if should_crack():
        print(emotions["INTENSE"])  # Wyświetl komunikat "INTENSE"
        print(run_aircrack("capture-01.cap", "/path/to/wordlist.txt"))