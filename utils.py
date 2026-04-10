# utils.py - Vérifie que l'IP a le bon format

def valider_ip(ip):
    # Une IP valide = 4 nombres séparés par des points
    # Exemple: 192.168.1.1
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

def parser_plage_ports(plage):
    # Convertit "20-100" en (20, 100)
    debut, fin = plage.split('-')
    debut = int(debut)
    fin = int(fin)
    if debut < 1 or fin > 65535 or debut > fin:
        raise ValueError("Plage invalide")
    return debut, fin