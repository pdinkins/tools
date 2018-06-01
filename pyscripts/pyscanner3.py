import socket
import time
from datetime import datetime

hosts = ["192.168.1.1", '70.171.11.105'] #, "192.168.2.1", "192.168.2.2", "192.168.2.10"]

lowPort = 1
highPort = 65535
#ports = [21, 53, 80, 548, 631, 1990, 5000, 8200, 20005, 33344]
ports = range(lowPort, highPort)

open_hosts = []
open_ports = []



for host in hosts:
    start_time = datetime.now()
    print("\n\n  [##]Now Scanning " + host + "\t" + str(start_time.time()))
    print('=' * 50)
    for port in ports:
        try:
            print("  [+]" + host + ":" + str(port), end="\r")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.001001125)
            result = s.connect_ex((host, port))
            #banner = s.recv(1024) # Will cause a timeout w/o a response
            if result == 0:
                print("  [*]OPEN " + host + ':' + str(port) + "\t" +
                str(datetime.now().time()))
                open_ports.append(port)
                open_hosts.append(host)
            #print(f"  [*]{65536/port:.1f} %", end="\r")
            s.close()
        except KeyboardInterrupt:
            quit()

    stop_time = datetime.now()
    total_time = stop_time - start_time
    print('=' * 50)
    print('\n  [*] Scan finished at %s' % (time.strftime('%H:%M:%S')))
    print('  [*] Scan duration: %s' % (total_time))