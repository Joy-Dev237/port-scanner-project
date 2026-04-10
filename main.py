# main.py - Programme principal

import sys
from utils import valider_ip, parser_plage_ports
from scanner import scanner_port

print("=== SCANNER DE PORTS ===\n")

# Demande l'adresse IP
ip = input("Adresse IP (ex: 192.168.1.1) : ")
if not valider_ip(ip):
    print("IP invalide")
    sys.exit()

# Demande la plage de ports
plage = input("Plage de ports (ex: 20-100) : ")
try:
    debut, fin = parser_plage_ports(plage)
except:
    print("Plage invalide")
    sys.exit()

print(f"\nScan de {ip} du port {debut} à {fin}...\n")

# Scan
for port in range(debut, fin + 1):
    if scanner_port(ip, port):
        print(f"Port {port} : OUVERT")
    else:
        print(f"Port {port} : fermé")

print("\nScan terminé")