import subprocess
import time

def run_airodump(interface, output_file):
    command = ["airodump-ng", "-w", output_file, "--output-format", "cap", interface]
    return subprocess.Popen(command)

def run_aircrack(capture_file, wordlist):
    command = ["aircrack-ng", "-w", wordlist, capture_file]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# Przykładowe użycie
airodump_process = run_airodump("wlan0", "capture")
time.sleep(60)  # Przechwytuj pakiety przez 60 sekund
airodump_process.terminate()  # Zakończ przechwytywanie pakietów

print(run_aircrack("capture-01.cap", "/path/to/wordlist.txt"))