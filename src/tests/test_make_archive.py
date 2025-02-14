import pytest
from unittest.mock import patch
from utils import create_archive

@pytest.fixture
def mock_shutil():
    with patch("shutil.make_archive") as mock:
        yield mock

@pytest.mark.parametrize("os_name", ["Darwin", "Linux", "Windows"])
def test_create_archive_success(mock_shutil, os_name):
    chosen_format = "zip"
    formats = {"zip": "zip", "tar": "tar"}
    save_path = f"/path/to/archive.{chosen_format}"
    home_dir = "/home/user"

    # Simule le comportement en fonction du système d'exploitation
    with patch("platform.system", return_value=os_name):
        # Simule une exécution réussie de make_archive
        mock_shutil.return_value = None

        with patch("builtins.print") as mock_print:
            create_archive(chosen_format, formats, save_path, home_dir)
            
            # On vérifie si make_archive a été appelé correctement
            mock_shutil.assert_called_once_with(save_path.replace(f".{chosen_format}", ""), "zip", home_dir)
            
            # Vérifie que le message de succès contient bien "✅"
            call_args = mock_print.call_args[0]  # Récupère les arguments passés à print
            assert "✅" in call_args[0]  # Vérifie la présence du symbole ✅ dans le message

@pytest.mark.parametrize("os_name", ["Darwin", "Linux", "Windows"])
def test_create_archive_failure(mock_shutil, os_name):
    chosen_format = "zip"
    formats = {"zip": "zip", "tar": "tar"}
    save_path = f"/path/to/archive.{chosen_format}"
    home_dir = "/home/user"

    # Simule une exception lors de l'appel de make_archive
    with patch("platform.system", return_value=os_name):
        mock_shutil.side_effect = Exception("Erreur lors de la création de l'archive")

        with patch("builtins.print") as mock_print:
            create_archive(chosen_format, formats, save_path, home_dir)
            
            # Vérifie que make_archive a été appelé
            mock_shutil.assert_called_once_with(save_path.replace(f".{chosen_format}", ""), "zip", home_dir)
            
            # Vérifie que le message d'erreur contient bien "❌"
            call_args = mock_print.call_args[0]  # Récupère les arguments passés à print
            assert "❌" in call_args[0]  # Vérifie la présence du symbole ❌ dans le message
