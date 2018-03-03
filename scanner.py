import socket
import sys
CHECKED_PORTS = []
COUNT = 0
while COUNT <= 1024:
    CHECKED_PORTS.append(COUNT)
    COUNT += 1

OPEN_PORTS = []
HOST_FQDN = socket.getfqdn()
print("Active Ports:")

for PORT in CHECKED_PORTS:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((HOST_FQDN, PORT))
    except socket.error:
        pass
    else:
        s.close
        OPEN_PORTS.append(PORT)

for PORT in OPEN_PORTS:
    print(PORT, end = ' ')

print("\n--------------------------------")
print("Port scan completed")

