import subprocess

# zwraca wartość interfejsu sieciowego
def get_network_interface():
    return "wlan0"
    # try:
    #     result = subprocess.run(["ip", "route"], capture_output=True, text=True, check=True)
    #     lines = result.stdout.split('\n')
    #     for line in lines:
    #         if "default" in line:
    #             return line.split()[4]  # The network interface is the 5th element in the line
    # except subprocess.CalledProcessError as e:
    #     print("Failed to get network interface.")
    #     print("Error:")
    #     print(e.stderr)

#  skanowanie na podatności
def run_vulnerability_scan(ip):
    print(f"Running vulnerability scan on host: {ip}")
    command = ["nmap", "-v", "--script=vuln", ip]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Vulnerability scan of {ip} completed successfully.")
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Vulnerability scan of {ip} failed.")
        print("Error:")
        print(e.stderr)

# ta funkcja skanuje hosta na podstawie określonego adresu IP
def run_detailed_nmap_scan(ip):
    print(f"Running detailed nmap scan on host: {ip}")
    command = ["nmap", "-v", "-A", "-T4", "-p-", ip]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Detailed scan of {ip} completed successfully.")
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Detailed scan of {ip} failed.")
        print("Error:")
        print(e.stderr)

# wykonuje skanowanie Nmap na określonym zakresie adresów IP
def run_nmap_scan(ip_range):
    network_interface = get_network_interface()
    print(f"Running nmap scan on network: {ip_range} using network interface: {network_interface}")
    command = ["nmap", "-sn", ip_range]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Scan completed successfully.")
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Scan failed.")
        print("Error:")
        print(e.stderr)

#ta funkcjA sprawdza, czy określony ciąg znaków znajduje się w wynikach skanowania
def check_scan_results_for_string(results, string):
    if results is None:
        print("No results to check.")
        return

    if string in results:
        print(f"Found {string} in scan results.")
    else:
        print(f"Did not find {string} in scan results.")

#ta funkcja skanuje hosta na podstawie określonego adresu IP
def run_nmap_scan(ip_range):
    network_interface = get_network_interface()
    print(f"Running nmap scan on network: {ip_range} using network interface: {network_interface}")
    command = ["nmap", "-O", "-e", network_interface, ip_range]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Scan completed successfully.")
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Scan failed.")
        print("Error:")
        print(e.stderr)

# run_nmap_scan("192.168.0.0/24")

# run_detailed_nmap_scan("192.168.0.164")

# results = run_detailed_nmap_scan("192.168.0.164")
# check_scan_results_for_string(results, "OpenSSH")
run_vulnerability_scan("192.168.0.164")