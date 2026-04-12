# ports.py - Correspondance entre ports et services standards
# Pour rendre le scan plus intelligent et informatif

def nom_service(port):
    """
    Retourne le nom du service associé à un port
    """
    services = {
        20: "📁 FTP (transfert fichiers)",
        21: "📁 FTP (commandes)",
        22: "🔒 SSH (connexion sécurisée)",
        23: "⚠️ Telnet (non sécurisé)",
        25: "📧 SMTP (envoi emails)",
        53: "🌐 DNS (résolution noms)",
        67: "📡 DHCP (serveur)",
        68: "📡 DHCP (client)",
        80: "🌍 HTTP (sites web classiques)",
        110: "📧 POP3 (réception emails)",
        111: "🔧 RPC (appels distants)",
        135: "🪟 RPC (Windows)",
        137: "🖥️ NetBIOS (noms)",
        138: "🖥️ NetBIOS (datagrammes)",
        139: "🖥️ NetBIOS (session)",
        143: "📧 IMAP (emails)",
        161: "📊 SNMP (supervision)",
        389: "📋 LDAP (annuaire)",
        443: "🔒 HTTPS (sites sécurisés)",
        445: "🖥️ SMB (partage Windows)",
        993: "🔒 IMAPS (emails sécurisés)",
        995: "🔒 POP3S (emails sécurisés)",
        1433: "🗄️ SQL Server",
        3306: "🐬 MySQL",
        3389: "🖥️ RDP (bureau distant)",
        5432: "🐘 PostgreSQL",
        5900: "🖥️ VNC (bureau distant)",
        6379: "⚡ Redis",
        27017: "🍃 MongoDB",
    }
    
    if port in services:
        return services[port]
    else:
        return "❓ Service inconnu"