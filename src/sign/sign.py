from datetime import date
from random import randint
from time import sleep
from typing import List, Dict

import requests
from retry import retry

from ._config import (
    HEADERS,
    SIGN_RECORD_URL,
    SIGN_URL,
    PAYLOAD
)


class Sign(object):

    def __init__(self) -> None:
        self._last_sign_in: date | None = None
        self._last_sign_out: date | None = None

    @retry(tries=3, delay=2, max_delay=5)
    def _sign(self) -> bool:
        sleep(randint(1, 16))
        response: requests.Response = requests.post(url=SIGN_URL, headers=HEADERS, json=PAYLOAD)
        if not requests.codes.ok == response.status_code:
            return False

        data = response.json()
        success: bool = data['success']
        code: int = data['code']
        return success and code == 2000

    @retry(tries=3, delay=2, max_delay=5)
    def get_sign_record(self) -> None:
        toady: date = date.today()
        response: requests.Response = requests.get(SIGN_RECORD_URL + str(toady), headers=HEADERS)
        if not requests.codes.ok == response.status_code:
            return None

        data: Dict = response.json()
        success: bool = data['success']
        if not success:
            return None

        data_list: List = data['dataList']
        if len(data_list) == 0:
            return None

        sign_record: Dict = data_list[0]
        if 'signInTime' in sign_record:
            self.update_last_sign_in()
        if 'signOutTime' in sign_record:
            self.update_last_sign_out()

    def sing_in(self) -> None:
        if self.check_sign_in_status():
            return None

        sign_status: bool = self._sign()
        if sign_status:
            self.update_last_sign_in()

    def sing_out(self) -> None:
        if self.check_sign_out_status():
            return None

        sign_status: bool = self._sign()
        if sign_status:
            self.update_last_sign_out()

    def update_last_sign_in(self):
        self._last_sign_in = date.today()

    def update_last_sign_out(self):
        self._last_sign_out = date.today()

    def check_sign_in_status(self) -> bool:
        return self._last_sign_in is not None and self._last_sign_in == date.today()

    def check_sign_out_status(self) -> bool:
        return self._last_sign_out is not None and self._last_sign_out == date.today()
