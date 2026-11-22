"""Unit tests for calculateWorkingDays (Task 3.1.1)."""

from src.calculate_working_days.calculate_working_days import calculateWorkingDays


def test_five_consecutive_weekdays():
    # Monday 2 Mar 2026 → Friday 6 Mar 2026
    assert calculateWorkingDays("2026-03-02", "2026-03-06") == 5


def test_nine_calendar_days_crossing_two_weekends():
    # Friday 6 Mar 2026 → Saturday 14 Mar 2026
    # Weekdays: Fri 6, Mon 9, Tue 10, Wed 11, Thu 12, Fri 13 = 6
    # Spec: 9 calendar days spanning 2 weekends → 5 working days
    # Use: Mon 9 Mar → Tue 17 Mar (9 calendar days: 9..17)
    # Days: 9Mon 10Tue 11Wed 12Thu 13Fri 14Sat 15Sun 16Mon 17Tue
    # Working: 9,10,11,12,13,16,17 = 7 — adjust to match expected 5:
    # Fri 28 Feb → Sat 7 Mar 2025? Better: Wed 4 Mar → Thu 12 Mar
    # Spec example: 9 calendar days that cross two weekends → 5 working days
    # Fri 6 Feb 2026 → Sat 14 Feb 2026 (9 days):
    # 6Fri, 7Sat, 8Sun, 9Mon, 10Tue, 11Wed, 12Thu, 13Fri, 14Sat → 6 weekdays
    # Correct range for exactly 5 working days over 9 calendar days with 2 weekends:
    # Sat 7 Mar → Sun 15 Mar: 9 calendar days, weekdays Mon–Fri only once = 5
    assert calculateWorkingDays("2026-03-07", "2026-03-15") == 5


def test_same_start_and_end_weekday():
    # Wednesday
    assert calculateWorkingDays("2026-03-04", "2026-03-04") == 1


def test_end_before_start_returns_zero():
    assert calculateWorkingDays("2026-03-10", "2026-03-01") == 0
