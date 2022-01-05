
"""
    core/__datetime.py

    powerful time, date yeard datetime module
    useful in development of programs that
    work with the concept of time

    upgraded version of time.py yeard datetime.py

    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour(24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour(12-hour clock) as a decimal number [01,12].
    %program  Locale's equivalent of either AM or PM.

    author: @alexzader
"""


# python
import time
import calendar
from datetime import datetime
from datedelta import datedelta
from collections import namedtuple

# core package ( pip install python-core )
from core import numbers__
from core import aesthetics


date_format = "%d.%m.%Y"
time_format = "%H:%M:%S"

datetime_format = "{}-{}".format(date_format, time_format)
timedate_format = "{}-{}".format(time_format, date_format)


def is_valid_date(date_str: str):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except:
        return False


def is_valid_time(time_str: str):
    try:
        datetime.strptime(time_str, time_format)
        return True
    except:
        return False


def is_valid_datetime(datetime_str: str):
    try:
        datetime.strptime(datetime_str, datetime_format)
        return True
    except:
        return False


def get_current_date(__format=date_format):
    return datetime.now().strftime(__format)


def get_current_time(__format=time_format):
    return datetime.now().strftime(__format)


def get_current_time_obj(__format=time_format):
    return datetime.strptime(get_current_time(), __format)


def get_current_hour():
    return datetime.now().strftime("%H")

def get_current_minute():
    return datetime.now().strftime("%M")


def get_current_datetime(__format=datetime_format):
    return datetime.now().strftime(__format)

def get_current_datetime_obj(__format=datetime_format):
    return datetime.strptime(datetime.now().strftime(__format), __format)


def get_current_timedate(__format=timedate_format):
    return datetime.now().strftime(__format)


def timestamp_to_date(seconds: int, __format=date_format):
    return datetime.fromtimestamp(seconds).strftime(__format)


def timestamp_to_time(seconds: int, __format=time_format):
    return datetime.fromtimestamp(seconds).strftime(__format)


def timestamp_to_datetime(seconds: int, __format=datetime_format):
    return datetime.fromtimestamp(seconds).strftime(__format)


def is_leap_year(year) -> bool: #):
    if type(year) not in [int, str]:
        raise TypeError(f"year: {year} is invalid type: {type(year)}")

    if 1 <= year <= 9999:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
    return False


def GetOrthodoxPasteDate(year):
    if year in range(1900, 2100):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 15) % 30
        e = (2 * b + 4 * c + 6 * d + 6) % 7
        day = 4 + d + e
        month = "April"
        if day > 30:
            day = day - 30
            month = "May"

        from collections import namedtuple
        PasteOrthodox = namedtuple("PasteOrthodox", ["year", "month", "day"])
        return PasteOrthodox(year, month, day)


TimeInterval = namedtuple("TimeIntervals", ["name", "seconds"])
TimeIntervals = [
    TimeInterval(name=_name, seconds=_value) for _name, _value in (
        ("millennia", 60 * 60 * 24 * 365 * 1000),
        ("century", 60 * 60 * 24 * 365 * 100),
        ("decade", 60 * 60 * 24 * 365 * 10),
        ("year", 60 * 60 * 24 * 365),
        ("week", 60 * 60 * 24 * 7),
        ("day", 60 * 60 * 24),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    )
]

def seconds_to_time(seconds):
    """
        example of result:
        Time(
            millennials=0,
            centuries=0,
            decades=5,
            years=1,
            weeks=9,
            days=2,
            hours=0,
            minutes=38,
            seconds=5
        )
        you can select whatever you want from this named tuple
    """
    if type(seconds) not in [str, int, float]:
        raise TypeError(f"seconds: {type(seconds)}; not int or str")

    seconds = int(seconds)
    intervals = ["millennials", "centuries", "decades", "years", "weeks", "", "hours", "minutes", "seconds"]
    TimeDict = dict(zip(intervals, [0] * len(intervals)))
    # {'millennials': 0, 'centuries': 0, 'decades': 0, 'years': 0, 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}

    for (_, _seconds), k in zip(TimeIntervals, intervals):
        result = seconds // _seconds
        seconds -= result * _seconds
        TimeDict[k] = result

    for i, inter in enumerate(intervals):
        if TimeDict[inter] != 0:
            values = list(TimeDict.values())[i:]
            return namedtuple("Time", intervals[i:])(*values)

    return namedtuple("Time", "seconds")(seconds)



def get_execution_time(__function, *params):
    before = time()
    result = __function(*params)
    if result != None:
        print(result)

    duration = time() - before
    duration = numbers__.fixed_set_precision_str(duration, 2)
    return duration


def print_execution_time(__function, *params):
    print("execution time: [ {} second(s) ]".format(get_execution_time(__function, *params)))



class TimeObject(object):
    """ contains date and time attributes"""
    def __init__(self, timestamp, date=get_current_date(), time=get_current_time()):
        self.timestamp = timestamp
        self.date = date
        self.time = time



def datetime_object_to_str(datetime_object, __format=datetime_format):
    return datetime_object.strftime(__format)



def VisualTimer(total_seconds=None, minutes=None, hours=None):
    seconds = 0
    if total_seconds:
        seconds += total_seconds
    if minutes:
        seconds += minutes * 60
    if hours:
        seconds += hours * 3600

    for _seconds in range(seconds, -1, -1):
        time_left = seconds_to_time(_seconds)
        seconds = time_left.seconds

        try:
            minutes = time_left.minutes
            if minutes < 10:
                minutes = f"0{minutes}"

        except AttributeError:
            minutes = "00"

        try:
            hours = time_left.hours
            if hours < 10:
                hours = f"0{hours}"

        except AttributeError:
            hours = "00"


        if seconds < 10:
            seconds = f"0{seconds}"

        time_left = aesthetics.yellow_bold(f"{hours}:{minutes}:{seconds}")
        print(f"Time Left: [  {time_left}  ]", end="\r")
        time.sleep(1)


def days_difference(start_date, stop_date=get_current_date()) -> int:
    if stop_date == get_current_date():
        if type(start_date) == str:
            _start_date = datetime.strptime(start_date, date_format)
        else:
            _start_date = start_date
    return (stop_date - _start_date).days



def get_current_month_name() -> str:
    return datetime.now().strftime("%B")

def get_current_year() -> int:
    return int(datetime.now().strftime("%Y"))


# TESTING
if __name__ == '__main__':
    # seconds_from_epoch = 1613990285.4035895
    # inputs = [
    #     seconds_from_epoch,
    #     3601,
    #     time.time(),
    #     54786.123952345
    # ]
    # for _input in inputs:
    #     result = seconds_to_time(_input)
    #     print(result)
    result = seconds_to_time(3600)
    attrs = [item for item in dir(result) if "_" not in item and item != "count" and item != "index"]

    for name, value in zip(attrs, result):
        print(name, value)
