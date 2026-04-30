# utils.py - Version modifiée (autorise tous les réseaux privés)
import socket

def valider_ip(ip):
    """Vérifie si une adresse IP est valide (format IPv4)"""
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
    """Récupère l'adresse IP réelle de ta machine sur le réseau local"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            if ip.startswith('127.'):
                return "172.20.46.224"
            return ip
        except:
            return "172.20.46.224"

def obtenir_reseau_local():
    """Détecte le réseau local réel de ta machine"""
    ip_locale = obtenir_ip_locale()
    parties = ip_locale.split('.')
    if len(parties) >= 3:
        return parties[0] + '.' + parties[1] + '.' + parties[2] + '.'
    return "172.20.46."

def est_dans_reseau_local(ip):
    """
    VERSION MODIFIÉE : Autorise tous les réseaux privés courants
    (192.168.x.x, 172.16.x.x à 172.31.x.x, 10.x.x.x)
    """
    # Vérifier si l'IP est dans une plage privée
    parties = ip.split('.')
    if len(parties) != 4:
        return False
    
    premier_octet = int(parties[0])
    
    # Plages d'IP privées :
    # 10.0.0.0 - 10.255.255.255
    # 172.16.0.0 - 172.31.255.255
    # 192.168.0.0 - 192.168.255.255
    
    if premier_octet == 10:
        return True
    if premier_octet == 172 and 16 <= int(parties[1]) <= 31:
        return True
    if premier_octet == 192 and parties[1] == '168':
        return True
    
    # Si l'IP n'est pas privée, refuser
    print(f"⚠️ Seules les IP privées sont autorisées (10.x.x.x, 172.16-31.x.x, 192.168.x.x)")
    return False

def afficher_infos_reseau():
    """Affiche les informations réseau de ta machine"""
    ip_locale = obtenir_ip_locale()
    reseau = obtenir_reseau_local()
    print("┌" + "─" * 58 + "┐")
    print("│ " + " INFORMATIONS RÉSEAU".ljust(56) + "│")
    print("├" + "─" * 58 + "┤")
    print(f"│  Votre IP locale     : {ip_locale.ljust(36)}│")
    print(f"│  Votre réseau        : {reseau + 'xxx'.ljust(36)}│")
    print("├" + "─" * 58 + "┤")
    print("│  PLAGES AUTORISÉES :".ljust(58) + "│")
    print("│  • 10.0.0.0 - 10.255.255.255".ljust(58) + "│")
    print("│  • 172.16.0.0 - 172.31.255.255".ljust(58) + "│")
    print("│  • 192.168.0.0 - 192.168.255.255".ljust(58) + "│")
    print("└" + "─" * 58 + "┘")
    print()
