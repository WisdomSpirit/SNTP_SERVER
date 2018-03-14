from datetime import datetime


UTC_OFFSET = 2208988800

def get_time(inaccuracy):
    """Returns time in SNTP UTC format (from UTC epoch)"""
    time = datetime.now().timestamp() + UTC_OFFSET + inaccuracy
    return time
