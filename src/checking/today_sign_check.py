import time

from .checker import Checker
from ..sign.sign import Sign


class TodaySignChecker(Checker):

    def __init__(self, sign: Sign) -> None:
        self.sign: Sign = sign

    def check(self) -> bool:
        hour: int = time.localtime().tm_hour
        if 6 < hour < 12:
            signed = self.sign.check_sign_in_status()
        else:
            signed = self.sign.check_sign_out_status()
        if not signed:
            return super().check()

        return False
