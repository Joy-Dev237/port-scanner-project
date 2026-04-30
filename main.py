# main.py - Version qui force le scan (ignore la restriction)
import sys
import time
import concurrent.futures
from utils import valider_ip, est_dans_reseau_local, afficher_infos_reseau, obtenir_reseau_local
from scanner import scanner_port
from ports import nom_service

def afficher_banniere():
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + " SCANNER DE PORTS - ÉDITION PROFESSIONNELLE".center(58) + "║")
    print("╚" + "═" * 58 + "╝\n")

def main():
    afficher_banniere()
    afficher_infos_reseau()
    
    print(" MODE SCAN ÉTENDU ACTIVÉ ")
    print("   (10.x.x.x, 172.16-31.x.x, 192.168.x.x)\n")
    
    while True:
        ip = input(" Entrez l'IP à scanner (ex: 192.168.137.123) : ")
        if not valider_ip(ip):
            print("❌ Format IP invalide.\n")
            continue
        
        # Vérification assouplie
        if not est_dans_reseau_local(ip):
            print(f" {ip} semble être sur un autre réseau.")
            force = input("   Voulez-vous quand même scanner ? (o/n) : ")
            if force.lower() != 'o':
                continue
        break

    try:
        print("\n OPTIONS DE SCAN :")
        print("  1. Scan rapide (ports 1-1024)")
        print("  2. Scan complet (1-65535)")
        print("  3. Scan personnalisé")
        choix = input("Votre choix (1/2/3) : ")
        
        if choix == "1":
            debut, fin = 1, 1024
        elif choix == "2":
            debut, fin = 1, 65535
            print(" Scan complet peut prendre plusieurs minutes...")
        else:
            plage = input(" Plage de ports (ex: 1-1000) : ")
            debut, fin = map(int, plage.split('-'))
        
        total = fin - debut + 1
    except Exception as e:
        print(f" Erreur : {e}")
        return

    print(f"\n Scan DE {ip} LANCÉ ({total} ports)")
    print("   (Cela peut prendre du temps selon la plage)\n")
    start_time = time.time()
    
    ports_ouverts = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = {executor.submit(scanner_port, ip, port, 0.5): port for port in range(debut, fin + 1)}
        
        compteur = 0
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            compteur += 1
            
            # Progression
            if compteur % 100 == 0 or compteur == total:
                pourcent = (compteur / total) * 100
                print(f"   {compteur}/{total} ports ({pourcent:.1f}%)", end='\r')
            
            if future.result():
                service = nom_service(port)
                print(f"\n   PORT {port} OUVERT - {service}")
                ports_ouverts.append(port)
    
    temps_total = time.time() - start_time
    
    print("\n" + "═" * 60)
    print(f" RÉSULTATS - {ip}")
    print("═" * 60)
    print(f"  Temps : {temps_total:.2f} secondes")
    print(f" Ports analysés : {total}")
    print(f" Ports ouverts : {len(ports_ouverts)}")
    
    if ports_ouverts:
        print("\n Détail :")
        for port in ports_ouverts:
            print(f"   • {port} : {nom_service(port)}")
    else:
        print("\nAucun port ouvert détecté")
        print("   → Vérifiez le pare-feu de l'appareil cible")
        print("   → Assurez-vous que l'appareil accepte les connexions")
        print("   → Testez avec 'ping " + ip + "' dans un terminal")
    
    print("═" * 60)

if __name__ == "__main__":
    main()
