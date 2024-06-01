from unittest.mock import Mock, patch

import pytest

from mymodule.lib.http_bin_client import HttpBinClient


@pytest.fixture
def mock_http_bin_client() -> Mock:
    return Mock(spec=HttpBinClient)


@patch("mymodule.lib.http_bin_client.HttpBinClient.get")
def test_get_ip_success(mock_http_bin_client: Mock) -> None:
    want = {"origin": "127.0.0.1"}
    mock_http_bin_client.return_value = want

    client = HttpBinClient()
    got = client.get(path="ip")

    assert got == want


@patch("mymodule.lib.http_bin_client.HttpBinClient.get")
def test_get_ip_fail(mock_http_bin_client: Mock) -> None:
    mock_http_bin_client.side_effect = Exception("Request failed")

    client = HttpBinClient()
    with pytest.raises(Exception) as exc_info:
        client.get(path="ip")

    assert str(exc_info.value) == "Request failed"
