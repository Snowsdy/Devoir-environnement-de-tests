import platform
from colorama import Fore, Style

def detect_os():
    """Détecte le système d'exploitation et retourne un nom normalisé."""
    os_name = platform.system()

    if os_name == "Linux":
        try:
            with open("/proc/version", "r") as f:
                version_info = f.read().lower()
                if "microsoft" in version_info:
                    return "WSL"
        except FileNotFoundError:
            pass
        return "Linux"

    if os_name == "Darwin":
        return "MacOS"

    return os_name

if __name__ == "__main__":
    """Exécute la fonction en standalone. (à des fins de debug)"""
    detected_os = detect_os()
    if detect_os == "":
        print(f"{Fore.RED}❌ Une erreur est survenue lors de la détection du système d'exploitation")
        exit
    else:
        print(f"{Fore.GREEN}🌍 OS détecté : {Fore.BLUE}{detected_os}{Style.RESET_ALL}")
