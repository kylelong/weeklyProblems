from datetime import date
def newYearsDay(year):
    return date(year, 1, 1).strftime('%A')

assert newYearsDay(2025) == "Wednesday"
assert newYearsDay(2024) == "Monday"