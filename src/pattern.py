import datetime

from configuration import PATTERN, PATTERN_WIDTH


def get_pattern_intensity_for_today() -> int:
    row = get_day_of_week()
    col = get_week_index() % PATTERN_WIDTH
    return PATTERN[row][col]


def get_day_of_week(date_time=None) -> int:
    if not date_time:
        date_time = datetime.datetime.utcnow()
    return date_time.isoweekday() % 7


def get_week_index(date_time=None) -> int:
    if not date_time:
        date_time = datetime.datetime.utcnow()
    ref_date_time = datetime.datetime(2020, 3, 1)
    diff_in_days = (date_time - ref_date_time).days
    return int(diff_in_days // 7)
