"""Count weekdays between two dates (inclusive)."""

from datetime import date, datetime, timedelta
from typing import Union

DateLike = Union[date, datetime, str]


def _to_date(value: DateLike) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return datetime.strptime(value, "%Y-%m-%d").date()


def calculateWorkingDays(startDate: DateLike, endDate: DateLike) -> int:
    """
    Return the number of Monday–Friday days from startDate to endDate inclusive.
    Returns 0 when endDate is before startDate.
    """
    start = _to_date(startDate)
    end = _to_date(endDate)

    if end < start:
        return 0

    working_days = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # Mon=0 ... Fri=4
            working_days += 1
        current += timedelta(days=1)
    return working_days


if __name__ == "__main__":
    # Three demo cases for Task 2 screenshots
    print("Mon–Fri one week:", calculateWorkingDays("2026-03-02", "2026-03-06"))  # 5
    print("Same weekday:", calculateWorkingDays("2026-03-04", "2026-03-04"))  # 1
    print("End before start:", calculateWorkingDays("2026-03-10", "2026-03-01"))  # 0
