import shutil

from colorama import Fore, Style

def create_archive(chosen_format: str, formats: dict[str, str], save_path: str, home_dir: str) -> None:
    """Crée une archive compressée selon l'OS, le format de celle-ci et du chemin où elle sera sauvegardée."""
    try:
        shutil.make_archive(save_path.replace(f".{chosen_format}", ""), formats[chosen_format], home_dir)
        print(f"{Fore.GREEN}✅ Sauvegarde créée avec succès :{Style.RESET_ALL}", save_path)
    except Exception as e:
        print(f"{Fore.RED}❌ Erreur lors de la création de la sauvegarde :{Style.RESET_ALL}", e)
