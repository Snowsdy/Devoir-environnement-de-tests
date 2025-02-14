import pytest
from utils import detect_os

@pytest.mark.parametrize("mocked_system, expected", [
    ("Windows", "Windows"),
    ("Linux", "Linux"),
    ("Darwin", "MacOS"),
    ("WSL", "WSL"),
])
def test_detect_os(mocker, mocked_system, expected):
    """✅ Teste la détection du système d'exploitation."""
    mock_system = mocker.patch("platform.system", return_value=mocked_system)
    
    if mocked_system == "Linux":
        mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=""))
        if expected == "WSL":
            mock_open.return_value.read.return_value = "microsoft"

    assert detect_os() == expected