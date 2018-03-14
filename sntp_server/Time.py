from datetime import datetime


def get_time(inaccuracy):
    """Returns time in SNTP UTC format (from UTC epoch)"""
    time = datetime.utcnow().timestamp() + inaccuracy
    return time
