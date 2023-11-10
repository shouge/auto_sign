import logging
import time
from datetime import date

import requests
from chinese_calendar import is_workday
from pytz import timezone
from retry import retry
from schedule import Scheduler

logging.basicConfig()
schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.INFO)

HEADERS = {
    'User-Agent': 'BosumErp/2.1.29 (iPhone; iOS 15.7.1; Scale/3.00)',
    'userphonetoken': '54ea8b0c6bea4c0689d4d49ef585836e@@eb3e4b3dc7a342d98ba95b3eccdced4f'
}

PAYLOAD = {
    "signPhone": "4DE2A58A-B225-4170-AEA1-1316BAD45262",
    "signType": "手动打卡",
    "longitude": "113.0300721571181",
    "groupSetId": "c279b9ea31c04d3395674e5fad303c19",
    "signWIFIName": "HOK-office",
    "latitude": "28.23089898003472",
    "type": "",
    "signWIFI": "DA:F1:53:26:3A:33"
}


@retry(tries=3, delay=2, max_delay=5)
def auto_sign() -> None:
    if not is_workday(date.today()):
        return None
    r = requests.post(url="https://erp.bosum.com/erp/phone/attendanceSign/sign", headers=HEADERS, json=PAYLOAD)
    schedule_logger.debug(r.text)


class Sign(object):

    def __init__(self):
        self.scheduler = Scheduler()
        self.scheduler.every().day.at("09:31", timezone("Asia/Shanghai")).do(job_func=auto_sign).tag("SignIn", "Sign")
        self.scheduler.every().day.at("21:26", timezone("Asia/Shanghai")).do(job_func=auto_sign).tag("SignOut", "Sign")

    def watch(self) -> None:
        while True:
            self.scheduler.run_pending()
            time.sleep(1)
