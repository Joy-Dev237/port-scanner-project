# scanner.py - Logique de connexion optimisée
import socket
import threading

def scanner_port(ip, port, delai=0.5):
    """
    Teste la connexion sur un port spécifique
    Timeout réduit pour plus de rapidité
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(delai)
            resultat = s.connect_ex((ip, port))
            return resultat == 0
    except:
        return False
