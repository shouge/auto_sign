from datetime import date
from random import randint
from time import sleep

import requests
from retry import retry

from ._config import (
    HEADERS,
    PAYLOAD,
    SIGN_URL
)


class Sign(object):

    def __init__(self) -> None:
        self._last_sign_in: date | None = None
        self._last_sign_out: date | None = None

    @retry(tries=3, delay=2, max_delay=5)
    def _sign(self) -> bool:
        sleep(randint(1, 16))
        print("Start Sign Mock!!!!")
        return True
        # response: requests.Response = requests.post(url=SIGN_URL, headers=HEADERS, json=PAYLOAD)
        # if requests.codes.ok != response.status_code:
        #     return False
        #
        # data = response.json()
        # success: bool = data['success']
        # code: int = data['code']
        # return success and code == 2000

    def sing_in(self) -> None:
        if self.check_sign_in_status():
            return None

        sign_status: bool = self._sign()
        if sign_status:
            self._last_sign_in = date.today()

    def sing_out(self) -> None:
        if self.check_sign_out_status():
            return None

        sign_status: bool = self._sign()
        if sign_status:
            self._last_sign_out = date.today()

    def check_sign_in_status(self) -> bool:
        return self._last_sign_in is not None and self._last_sign_in == date.today()

    def check_sign_out_status(self) -> bool:
        return self._last_sign_out is not None and self._last_sign_out == date.today()
