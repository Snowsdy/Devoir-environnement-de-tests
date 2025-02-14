import os

from datetime import datetime
from colorama import Fore, Style
from utils import detect_os, create_archive

if __name__ == "__main__":
    """Crée une archive compressée du répertoire personnel 
    de l'utilisateur avec l'extension choisie et 
    permet de définir l'emplacement de sauvegarde."""
    os_name = detect_os()

    if os_name == "":
        print(f"{Fore.RED}❌ Une erreur est survenue lors de la détection du système d'exploitation")
        exit
    else:
        print(f"{Fore.GREEN}🌍 OS détecté : {Fore.BLUE}{os_name}{Style.RESET_ALL}")

    timestamp = datetime.now().strftime("%Y%m%d")
    home_dir = os.path.expanduser("~")

    formats = {
        "zip": "zip", 
        "tar.gz": "gztar", 
        "tar.bz2": "bztar", 
        "tar.xz": "xztar"
    }
    print(f"{Fore.CYAN}📂 Formats disponibles :{Fore.LIGHTGREEN_EX}", ", ".join(formats.keys()), Style.RESET_ALL)
    chosen_format = input("Choisissez un format de compression : ").strip().lower()
    if chosen_format not in formats:
        print(f"{Fore.YELLOW}⚠️  Format non reconnu, utilisation de tar.gz par défaut.{Style.RESET_ALL}")
        chosen_format = "tar.gz"

    backup_file = f"backup_{os_name}_{timestamp}.{chosen_format}"
    backup_filename = input(f"Donnez un nom à l'archive (par défaut: {backup_file})").strip()

    if backup_filename:
        backup_file = f"{backup_filename}.{chosen_format}"

    default_save_path = os.path.join(home_dir, backup_file)

    save_dir = input(f"Entrez le chemin du dossier de sauvegarde (par défaut : {home_dir}): ").strip()

    if not save_dir:
        save_dir = home_dir
    
    save_path = os.path.join(save_dir, backup_file)

    print(f"{Fore.LIGHTBLUE_EX}🖥️ Création de l'archive...{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}⚠️  L'opération peut prendre plusieurs minutes !{Style.RESET_ALL}")

    create_archive(
        chosen_format=chosen_format,
        formats=formats,
        save_path=save_path,
        home_dir=home_dir
    )