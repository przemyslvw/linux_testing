import subprocess
import time
import os
from emotions import emotions
from pwnagothi_def import run_airodump, run_aircrack, check_handshake, check_monitor_mode, set_monitor_mode

import logging

# Ustawienie logowania
logging.basicConfig(filename='activity.log', level=logging.INFO)

# Przykładowe użycie
capture_count = 1
while True:
    if not check_monitor_mode("wlan0"):
        print("Karta sieciowa nie jest w trybie monitorowania. Przełączam kartę do trybu monitorowania.")
        set_monitor_mode("wlan0")
        if not check_monitor_mode("wlan0"):
            print("Nie udało się przełączyć karty do trybu monitorowania. Spróbuj ponownie.")
            break

    print(emotions["EXCITED"])  # Wyświetl komunikat "EXCITED"
    print("Rozpoczynam przechwytywanie pakietów...")
    capture_file = f"capture-{capture_count:02d}"
    airodump_process = run_airodump("wlan0", capture_file)
    time.sleep(60)  # Przechwytuj pakiety przez 60 sekund
    airodump_process.kill()  # Zakończ przechwytywanie pakietów
    print("Zakończono przechwytywanie pakietów.")

    print("Sprawdzam, czy przechwycono handshake...")
    if not check_handshake(f"{capture_file}-01.cap"):
        print("Nie przechwycono handshake'a WPA. Spróbuj ponownie.")
        capture_count += 1
        continue

    print("Przechwycono handshake!")
    logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - EXCITED - Handshake captured')
    logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - EXCITED - Started capturing packets')
    logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - EXCITED - Stopped capturing packets')

    print(emotions["INTENSE"])  # Wyświetl komunikat "INTENSE"
    print("Rozpoczynam łamanie hasła...")
    result = run_aircrack(f"{capture_file}-01.cap", "/pass/pass.txt")
    print("Zakończono łamanie hasła. Wynik: ", result)
    logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - INTENSE - Started cracking password')
    logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())} - INTENSE - Finished cracking password: {result}')

    capture_count += 1