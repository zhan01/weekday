import datetime

year = int(input('Year: '))
month = int(input('Month: '))
date = int(input('Day: '))

def get_weekday(year, month, date):
    result = datetime.datetime(year, month, date)
    return result.strftime('%A')

print(get_weekday(year, month, date))



assert get_weekday(1996, 12, 2) == 'Monday'
assert get_weekday(2012, 12, 12) == 'Wednesday'
assert get_weekday(2016, 1, 10) == 'Sunday'
assert get_weekday(2018, 8, 13) == 'Monday'