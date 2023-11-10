from __future__ import annotations

from abc import ABC, abstractmethod


class Checker(ABC):
    _next_check: Checker | None = None

    def set_next(self, checker: Checker) -> Checker:
        self._next_check = checker
        return checker

    @abstractmethod
    def check(self) -> bool:
        if self._next_check is not None:
            return self._next_check.check()
        return True
