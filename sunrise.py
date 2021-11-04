import csv
import datetime
import sys
import time

import ephem


CITIES = [
    {'name': 'Colorado Springs CO', 'latitude': '38.8339', 'longitude': '-104.8214', 'offset': -7},
    {'name': 'Kansas City KS', 'latitude': '39.1155', 'longitude': '-94.6268', 'offset': -6},
    {'name': 'Seattle WA', 'latitude': '47.6062', 'longitude': '-122.3321', 'offset': -8}
]


def is_dst(dt):
    tt = (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday(), 0, 0)
    stamp = time.mktime(tt)
    lt = time.localtime(stamp)
    return lt.tm_isdst > 0


def time_hours(dt):
    return round(dt.hour + (dt.minute + (dt.second + dt.microsecond / 1000000) / 60) / 60, 3)


observer = ephem.Observer()
observer.pressure = 0.0

start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2023, 1, 1)

data = []
for city in CITIES:
    observer.lat = city['latitude']
    observer.lon = city['longitude']

    date = start_date
    while date < end_date:
        city_tz = datetime.timezone(datetime.timedelta(hours=city['offset'] + (1 if is_dst(date) else 0)))
        observer.date = datetime.datetime(date.year, date.month, date.day, hour=12, tzinfo=city_tz).astimezone(datetime.timezone.utc)

        # Calculate sunrise, sunset (horizon '-0:34')
        observer.horizon = '-0:34'
        sunrise = observer.previous_rising(ephem.Sun()).datetime().replace(tzinfo=datetime.timezone.utc).astimezone(city_tz)
        sunset = observer.next_setting(ephem.Sun()).datetime().replace(tzinfo=datetime.timezone.utc).astimezone(city_tz)

        # Calculate civil twilight (horizon @ -6)
        observer.horizon = '-6'
        ctbegin = observer.previous_rising(ephem.Sun(), use_center=True).datetime().replace(tzinfo=datetime.timezone.utc).astimezone(city_tz)
        ctend = observer.next_setting(ephem.Sun(), use_center=True).datetime().replace(tzinfo=datetime.timezone.utc).astimezone(city_tz)

        data.append({
            'City': city['name'],
            'Date': date.strftime('%Y-%m-%d'),
            'CTBegin': time_hours(ctbegin),
            'Sunrise': time_hours(sunrise),
            'Sunset': time_hours(sunset),
            'CTEnd': time_hours(ctend)
        })

        date = date + datetime.timedelta(days = 1)

writer = csv.DictWriter(sys.stdout, ['City', 'Date', 'CTBegin', 'Sunrise', 'Sunset', 'CTEnd'])
writer.writeheader()
for row in data:
    writer.writerow(row)
