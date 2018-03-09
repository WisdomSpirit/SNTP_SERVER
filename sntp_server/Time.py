from datetime import datetime


NTP_UTC_OFFSET = 2208988800

def get_time(accuracy):
    """Returns time in SNTP UTC format (from UTC epoch)"""
    time = datetime.now().timestamp() + NTP_UTC_OFFSET + accuracy
    return time
