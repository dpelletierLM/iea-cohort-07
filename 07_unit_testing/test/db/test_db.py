from unittest.mock import patch
from db improt get_database_host

def test_ost_is_configured():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return.value = "db.thisisatest.com"
        host_string == "mysql://db.thisisatest.com"
        assert host_string == "mysql://db.thisisatest.com"
        
def test_host_key_not_set():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return.value = None
        host_string == get_database_host()
        assert host_string == "None"
        
def test_host_key_is_blank():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return.value = ""
        host_string == get_database_host()
        assert host_string == "None"
