from __future__ import annotations

import time

from ..checking.checker import Checker
from ..checking.phone_sign_check import PhoneSignChecker
from ..checking.random_check import RandomChecker
from ..checking.today_sign_check import TodaySignChecker
from ..checking.workday_check import WorkDayChecker
from ..sign.sign import Sign


class SignTask:

    def __init__(self) -> None:
        self._sign: Sign = Sign()
        self._checker: Checker = WorkDayChecker()
        self._checker.set_next(TodaySignChecker(self._sign)).set_next(RandomChecker()).set_next(
            PhoneSignChecker(self._sign))

    def __call__(self, *args, **kwargs):
        check: bool = self._checker.check()
        print("chck is ", check)
        if not check:
            return None

        hour: int = time.localtime().tm_hour
        is_sign_in: bool = 6 < hour < 12
        if is_sign_in:
            self._sign.sing_in()
        else:
            self._sign.sing_out()
