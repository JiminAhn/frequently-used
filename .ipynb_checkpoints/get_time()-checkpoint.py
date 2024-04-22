import datetime
import pytz

def get_time(): ## 현재 시각 반환

    now = datetime.datetime.utcnow()
    UTC = pytz.timezone('UTC')
    KST = pytz.timezone('Asia/Seoul')
    now_utc = now.replace(tzinfo=UTC)
    now_kst = now_utc.astimezone(KST)
    timestr = now_kst.strftime("%y%m%d")

    return timestr
