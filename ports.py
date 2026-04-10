# ports.py - Correspondance entre numéro de port et service standard

def nom_service(port):
    """
    Retourne le nom du service standard pour un port donné
    """
    services = {
        20: "FTP (transfert de fichiers)",
        21: "FTP (commandes)",
        22: "SSH (connexion sécurisée)",
        23: "Telnet (connexion non sécurisée)",
        25: "SMTP (envoi d'emails)",
        53: "DNS (résolution de noms)",
        67: "DHCP (attribution d'IP)",
        68: "DHCP (client)",
        80: "HTTP (sites web)",
        110: "POP3 (réception d'emails)",
        111: "RPC (appels distants)",
        135: "RPC (Windows)",
        137: "NetBIOS (partage fichiers)",
        138: "NetBIOS (datagrammes)",
        139: "NetBIOS (session)",
        143: "IMAP (emails)",
        161: "SNMP (supervision réseau)",
        389: "LDAP (annuaire)",
        443: "HTTPS (sites web sécurisés)",
        445: "SMB (partage Windows)",
        993: "IMAPS (emails sécurisés)",
        995: "POP3S (emails sécurisés)",
        1433: "SQL Server (base de données)",
        3306: "MySQL (base de données)",
        3389: "RDP (bureau à distance)",
        5432: "PostgreSQL (base de données)",
        5900: "VNC (bureau à distance)",
        6379: "Redis (cache)",
        27017: "MongoDB (base de données)",
    }
    
    if port in services:
        return services[port]
    else:
        return "Service inconnu (port non standard)"