# scanner.py - Teste si un port est ouvert

import socket

def scanner_port(ip, port):
    try:
        # Crée une connexion
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Attend 0.5 seconde max
        resultat = s.connect_ex((ip, port))
        s.close()
        # 0 = connexion réussie = port ouvert
        return resultat == 0
    except:
        return False