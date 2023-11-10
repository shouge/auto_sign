from __future__ import annotations

import time

from ..checking.checker import Checker
from ..checking.random_check import RandomChecker
from ..checking.today_sign_check import TodaySignChecker
from ..checking.workday_check import WorkDayChecker
from ..sign.sign import Sign


class SignTask:

    def __init__(self):
        self._sign: Sign = Sign()
        self._checker: Checker = WorkDayChecker()
        self._checker.set_next(TodaySignChecker(self._sign)).set_next(RandomChecker())

    def __call__(self, *args, **kwargs):
        print("Starting Task Job!")
        check: bool = self._checker.check()
        print("Checker check status is {}", check)
        if not check:
            return None

        hour: int = time.localtime().tm_hour
        if 6 < hour < 12:
            self._sign.sing_in()
        else:
            self._sign.sing_out()
