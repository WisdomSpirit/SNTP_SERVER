import time

def get_time(accuracy):
    """Returns time in SNTP UTC format (from UTC epoch)"""
    return time.time() + accuracy + 2208988800
