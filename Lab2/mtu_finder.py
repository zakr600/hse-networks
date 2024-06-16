import subprocess
import sys
import re
import socket

def is_valid_host(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False

def ping(host, packet_size, timeout=10):
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', '-W', str(timeout), '-M', 'do', '-s', str(packet_size), host]
        process = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return process.returncode == 0
    except Exception as e:
        print(f"Error during ping: {e}")
        sys.exit(1)

import platform

def find_min_mtu(host):
    low, high = 28, 65508

    while high - low > 1:
        mid = (low + high) // 2
        packet_size = mid - 28
        if ping(host, packet_size):
            low = mid
        else:
            high = mid
    return low

if __name__ == '__main__':
    host = input('Enter host:')
    if not host:
        print("You need to specify destination host")
        sys.exit(1)
    if not is_valid_host(host):
        print("The entered host is not valid")
        sys.exit(1)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        resolved = subprocess.run(['ping', param, '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if resolved.returncode != 0:
            print("The destination host is unreachable.")
            sys.exit(1)
    except Exception as e:
        print(f"Failed to resolve host: {e}.")
        sys.exit(1)

    min_mtu = find_min_mtu(host)
    print(f"Minimum MTU to {host} is {min_mtu}")
