# main.py - Programme principal (interface utilisateur)
# C'est le fichier à exécuter

import sys
import time
from utils import (
    valider_ip, 
    est_dans_reseau_local, 
    afficher_infos_reseau,
    obtenir_reseau_local
)
from scanner import scanner_port
from ports import nom_service

def afficher_banniere():
    """
    Affiche une belle bannière au démarrage
    """
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " SCANNER DE PORTS - Édition Réseau Local".center(58) + "║")
    print("╠" + "═" * 58 + "╣")
    print("║" + " Version Sécurisée - Uniquement réseau local".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()

def afficher_barre_progression(current, total, largeur=30):
    """
    Affiche une barre de progression simple
    """
    pourcentage = int((current / total) * 100)
    rempli = int((current / total) * largeur)
    vide = largeur - rempli
    barre = "█" * rempli + "░" * vide
    return f"[{barre}] {pourcentage}%"

def main():
    """
    Fonction principale du programme
    """
    # Affiche la bannière
    afficher_banniere()
    
    # Affiche les informations réseau (pour que l'utilisateur sache)
    afficher_infos_reseau()
    
    # === BOUCLE POUR L'ADRESSE IP ===
    while True:
        print("┌" + "─" * 58 + "┐")
        ip = input("│  Adresse IP à scanner : ").strip()
        print("└" + "─" * 58 + "┘")
        
        # Vérification du format IP
        if not valider_ip(ip):
            print("\n ERREUR : Format d'IP invalide !")
            print("   Une IP valide ressemble à : 192.168.1.1\n")
            continue
        
        # VÉRIFICATION CRITIQUE : Est-ce que l'IP est dans le réseau local ?
        if not est_dans_reseau_local(ip):
            mon_reseau = obtenir_reseau_local()
            print("\n" + "═" * 60)
            print(" ACCÈS REFUSÉ !")
            print("═" * 60)
            print(f" Cette machine n'est pas dans votre réseau local.")
            print(f" Votre réseau autorisé : {mon_reseau}xxx")
            print(f" IP saisie : {ip}")
            print("\n Ce scanner est conçu pour analyser UNIQUEMENT")
            print("   les appareils présents sur votre réseau local.")
            print("═" * 60 + "\n")
            continue  # Redemande une IP
        
        # IP valide et dans le réseau local
        print(f"\n IP valide et autorisée : {ip}")
        print(f"   (Cette IP est bien dans votre réseau local)\n")
        break
    
    # === BOUCLE POUR LA PLAGE DE PORTS ===
    while True:
        print("┌" + "─" * 58 + "┐")
        plage = input("│ 🔌 Plage de ports (ex: 20-100) : ").strip()
        print("└" + "─" * 58 + "┘")
        
        try:
            parties = plage.split('-')
            if len(parties) != 2:
                raise ValueError()
            debut = int(parties[0])
            fin = int(parties[1])
            
            if debut < 1 or fin > 65535 or debut > fin:
                raise ValueError()
            
            print(f"\n Plage valide : {debut} à {fin}\n")
            break
            
        except ValueError:
            print("\n ERREUR : Plage de ports invalide !")
            print("   Format attendu : début-fin (ex: 20-100)")
            print("   Les ports doivent être entre 1 et 65535\n")
    
    # === CONFIRMATION AVANT SCAN ===
    total_ports = fin - debut + 1
    print("═" * 60)
    print(" RÉCAPITULATIF DU SCAN")
    print("═" * 60)
    print(f"    Cible        : {ip}")
    print(f"   🔌 Plage        : {debut} → {fin}")
    print(f"    Ports à tester : {total_ports}")
    print("═" * 60)
    
    confirmation = input("\n Lancer le scan ? (o/n) : ").strip().lower()
    if confirmation != 'o':
        print("\n Scan annulé. Au revoir !")
        sys.exit(0)
    
    # === LANCEMENT DU SCAN ===
    print("\n" + "═" * 60)
    print(" SCAN EN COURS...")
    print("═" * 60 + "\n")
    
    ports_ouverts = []
    
    for index, port in enumerate(range(debut, fin + 1), 1):
        # Affiche la progression
        progression = afficher_barre_progression(index, total_ports)
        print(f"   {progression} | Test port {port}...", end=" ")
        
        if scanner_port(ip, port):
            service = nom_service(port)
            print(f"OUVERT → {service}")
            ports_ouverts.append(port)
        else:
            print(" Fermé")
        
        # Petit délai pour ne pas surcharger le réseau
        time.sleep(0.05)
    
    # === RÉSULTATS FINAUX ===
    print("\n" + "═" * 60)
    print(" RÉSULTATS DU SCAN")
    print("═" * 60)
    
    if ports_ouverts:
        print(f"\n {len(ports_ouverts)} port(s) ouvert(s) trouvé(s) sur {total_ports} testés :\n")
        for port in ports_ouverts:
            service = nom_service(port)
            print(f"   Port {port} : {service}")
    else:
        print("\n Aucun port ouvert trouvé dans la plage spécifiée.")
        print("    Conseil : Essayez une plage plus large (ex: 1-1000)")
    
    print("\n" + "═" * 60)
    print(" Scan terminé.")
    print("═" * 60 + "\n")

# Point d'entrée du programme
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Scan interrompu par l'utilisateur. Au revoir !\n")
        sys.exit(0)