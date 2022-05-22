from main import sunrise, sunset, time_now, data
from datetime import datetime

print(time_now)
print(f"{time_now.year}-{time_now.month}-{time_now.day}")


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


start = datetime.time(18, 0, 0)
end = datetime.time(5, 0, 0)
time_in_range(start, end, datetime.time(23, 30, 0))
