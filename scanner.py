# scanner.py - Teste si un port est ouvert

import socket

def scanner_port(ip, port, delai=0.5):
    """
    Teste si un port est ouvert sur une IP donnée
    Retourne True si ouvert, False sinon
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(delai)
        resultat = s.connect_ex((ip, port))
        s.close()
        return resultat == 0
    except:
        return False