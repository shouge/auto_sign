from random import randint

from ..checking.checker import Checker


class RandomChecker(Checker):

    def check(self) -> bool:
        if randint(1, 10) % 2 == 0:
            return super().check()
        return False
