# utils.py - Validation des entrées et détection du réseau local
# Ce fichier contient toutes les fonctions de vérification

import socket
import os

def valider_ip(ip):
    """
    Vérifie si une adresse IP est valide (format IPv4)
    Exemple: 192.168.1.1 -> True
             999.999.999.999 -> False
    """
    parties = ip.split('.')
    if len(parties) != 4:
        return False
    for partie in parties:
        if not partie.isdigit():
            return False
        nombre = int(partie)
        if nombre < 0 or nombre > 255:
            return False
    return True

def obtenir_ip_locale():
    """
    Récupère l'adresse IP réelle de ta machine sur le réseau local
    Exemple: 192.168.1.45
    """
    try:
        # Crée une connexion temporaire pour connaître notre IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        # Si ça échoue, on essaie une autre méthode
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        except:
            return "127.0.0.1"

def obtenir_reseau_local():
    """
    Détecte le réseau local réel de ta machine
    Exemple: si ton IP est 192.168.1.45 -> retourne "192.168.1."
    """
    ip_locale = obtenir_ip_locale()
    parties = ip_locale.split('.')
    if len(parties) >= 3:
        return parties[0] + '.' + parties[1] + '.' + parties[2] + '.'
    return "192.168.1."

def est_dans_reseau_local(ip):
    """
    Vérifie si une IP appartient au MÊME réseau local que ta machine
    C'est la fonction clé qui filtre les adresses hors réseau
    """
    mon_reseau = obtenir_reseau_local()
    return ip.startswith(mon_reseau)

def afficher_infos_reseau():
    """
    Affiche les informations réseau de ta machine (interface utilisateur)
    """
    ip_locale = obtenir_ip_locale()
    reseau = obtenir_reseau_local()
    print("┌" + "─" * 58 + "┐")
    print("│ " + " INFORMATIONS RÉSEAU".ljust(56) + "│")
    print("├" + "─" * 58 + "┤")
    print(f"│  Votre IP locale     : {ip_locale.ljust(36)}│")
    print(f"│ Votre réseau        : {reseau + 'xxx'.ljust(36)}│")
    print(f"│  Plage autorisée     : {reseau + '1 à ' + reseau + '254'.ljust(31)}│")
    print("└" + "─" * 58 + "┘")
    print()