from datetime import date

from chinese_calendar import is_workday

from .checker import Checker


class WorkDayChecker(Checker):

    def check(self) -> bool:
        if not is_workday(date.today()):
            return False
        return super().check()
