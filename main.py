import socket # tcp/udp calls
from termcolor import colored # terminal printing


def scan(target_ip, target_port):
    print(f"Scanning {target_ip}")
    for ports in range(1, target_port):
        port_scan(target_ip, ports)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[O] Connected to port {str(port)}")
        sock.close()
    except:
        pass


target_ip = input("Target/s to scan? (Split by ',' if needed): ")
target_port = int(input("How many ports do you want to scan? "))

if "," in target_ip:
    print(colored("[/] Scanning specified targets", "green"))
    for ips in target_ip.split(","):
        scan(ips, target_port)
else:
    print("[/] Scanning target")
    scan(target_ip, target_port)