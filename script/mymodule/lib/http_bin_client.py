from __future__ import annotations

from typing import Any, Callable, NoReturn

import requests
from requests import Response


def handle_request_exceptions(func: Callable[..., Response]) -> Callable[..., Response]:
    def wrapper(*args: Any, **kwargs: Any) -> Response | NoReturn:
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise
        else:
            return response

    return wrapper


class HttpBinClient(object):
    _BASE_URL = "https://httpbin.org"

    def __init__(self) -> None:
        self.session = requests.Session()

    def _send_request(self, path: str, method: str) -> Response:
        return self.session.request(method=method, url=f"{self._BASE_URL}/{path}")

    @handle_request_exceptions
    def get(self, path: str) -> Response:
        return self._send_request(method="GET", path=path)
