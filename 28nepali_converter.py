import datetime
import datetime_nepali


year = int(input("input Nepali year: "))
month = int(input("input nepali month: "))
day = int(input("input nepali day: "))

date = datetime_nepali.date(year, month, day).to_datetime_date()

print(f"english date is {date}")