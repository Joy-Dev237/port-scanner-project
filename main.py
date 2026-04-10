# main.py - Programme principal complet

import sys
from utils import valider_ip, parser_plage_ports, est_dans_mon_reseau
from scanner import scanner_port
from ports import nom_service

def main():
    print("=" * 60)
    print("🔍 SCANNER DE PORTS - Version Réseau Local")
    print("=" * 60)
    print("Ce scanner vérifie d'abord que l'IP est dans votre réseau local.\n")
    
    # === BOUCLE POUR L'IP ===
    while True:
        ip = input("📡 Adresse IP cible (ex: 192.168.1.1) : ")
        
        # Vérification du format
        if not valider_ip(ip):
            print(f"❌ '{ip}' n'est pas une IP valide. Réessaie !\n")
            continue
        
        # Vérification du réseau local
        if not est_dans_mon_reseau(ip):
            print(f"⚠️ Attention : {ip} n'est pas dans votre réseau local.")
            confirmation = input("Voulez-vous quand même scanner cette IP ? (o/n) : ")
            if confirmation.lower() != 'o':
                print("Scan annulé. Veuillez entrer une IP de votre réseau.\n")
                continue  # Re-demande une IP
        
        print(f"✅ IP valide et autorisée : {ip}\n")
        break  # Sort de la boucle
    
    # === BOUCLE POUR LA PLAGE DE PORTS ===
    while True:
        plage = input("🔌 Plage de ports (ex: 20-100) : ")
        try:
            debut, fin = parser_plage_ports(plage)
            print(f"✅ Plage valide : {debut} à {fin}\n")
            break
        except ValueError:
            print(f"❌ '{plage}' n'est pas une plage valide. Format: début-fin (ex: 20-100)\n")
    
    # === LANCEMENT DU SCAN ===
    print(f"🚀 Lancement du scan de {ip} du port {debut} à {fin}...\n")
    
    ports_ouverts = []
    
    for port in range(debut, fin + 1):
        print(f"   Test du port {port}...", end=" ")
        
        if scanner_port(ip, port):
            service = nom_service(port)
            print(f"✅ OUVERT → {service}")
            ports_ouverts.append(port)
        else:
            print("❌ Fermé")
    
    # === RÉSULTATS ===
    print("\n" + "=" * 60)
    print("📊 RÉSULTATS DU SCAN")
    print("=" * 60)
    
    if ports_ouverts:
        print(f"✅ {len(ports_ouverts)} port(s) ouvert(s) trouvé(s) :\n")
        for port in ports_ouverts:
            service = nom_service(port)
            print(f"   • Port {port} : {service}")
    else:
        print("❌ Aucun port ouvert trouvé dans la plage spécifiée.")
    
    print("\n" + "=" * 60)
    print("🏁 Scan terminé.")

if __name__ == "__main__":
    main()