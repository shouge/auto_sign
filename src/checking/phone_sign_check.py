from __future__ import annotations

import time

from .checker import Checker
from ..sign.sign import Sign


class PhoneSignChecker(Checker):
    def __init__(self, sign: Sign) -> None:
        self._sign = sign

    def check(self) -> bool:
        self._sign.get_sign_record()

        hour: int = time.localtime().tm_hour
        if 6 < hour < 12:
            signed: bool = self._sign.check_sign_in_status()
        else:
            signed: bool = self._sign.check_sign_out_status()
        if not signed:
            return super().check()

        return False
