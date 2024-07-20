import datetime
import datetime_nepali


year = int(input("input English year: "))
month = int(input("input English month: "))
day = int(input("input English day: "))

date = datetime_nepali.date.from_datetime_date(datetime.date(year, month, day))



print(f"english date is {date}")