import csv
import datetime

import ephem
import pytz


# The years for which to generate sunrise data
START_YEAR = 2020
END_YEAR = 2023


# The list of cities for which to generate sunrise data
CITIES = [
    {
        'name': 'Colorado Springs CO',
        'latitude': '38.8339',
        'longitude': '-104.8214',
        'tz': pytz.timezone('US/Mountain')
    },
    {
        'name': 'Juneau AK',
        'latitude': '58.3019',
        'longitude': '-134.4197',
        'tz': pytz.timezone('US/Alaska')
    },
    {
        'name': 'Kansas City KS',
        'latitude': '39.1155',
        'longitude': '-94.6268',
        'tz': pytz.timezone('US/Central')
    },
    {
        'name': 'San Diego CA',
        'latitude': '32.7157',
        'longitude': '-117.1611',
        'tz': pytz.timezone('US/Pacific')
    },
    {
        'name': 'Seattle WA',
        'latitude': '47.6062',
        'longitude': '-122.3321',
        'tz': pytz.timezone('US/Pacific')
    }
]


# Compute the local time in hours (0-24)
def local_time_hours(naive_gmt_dt, local_tz):
    local_dt = naive_gmt_dt.replace(tzinfo=datetime.timezone.utc).astimezone(local_tz)
    return local_dt.hour + (local_dt.minute + (local_dt.second + local_dt.microsecond / 1000000) / 60) / 60


def main():

    # Initialize the ephem observer
    observer = ephem.Observer()
    observer.pressure = 0.0

    # Generate the sunrise data city by city
    data = []
    timedelta_day = datetime.timedelta(days=1)
    for city in CITIES:

        # Update the observer's location
        observer.lat = city['latitude']
        observer.lon = city['longitude']

        # For each day add one sunrise date row
        date = datetime.datetime(START_YEAR, 1, 1, 12, tzinfo=city['tz'])
        end_date = datetime.datetime(END_YEAR + 1, 1, 1, tzinfo=city['tz'])
        daylight_yesterday = None
        while date < end_date:

            # Update the observer's date
            observer.date = date

            # Calculate sunrise, sunset (horizon '-0:34')
            observer.horizon = '-0:34'
            sunrise = local_time_hours(observer.previous_rising(ephem.Sun()).datetime(), city['tz'])
            sunset = local_time_hours(observer.next_setting(ephem.Sun()).datetime(), city['tz'])

            # Calculate civil twilight (horizon @ -6)
            observer.horizon = '-6'
            ctbegin = local_time_hours(observer.previous_rising(ephem.Sun(), use_center=True).datetime(), city['tz'])
            ctend = local_time_hours(observer.next_setting(ephem.Sun(), use_center=True).datetime(), city['tz'])

            # Compute daylight
            daylight = ctend - ctbegin
            daylight_change = (daylight - daylight_yesterday) * 60 if daylight_yesterday is not None else None

            # Create the sunrise data row
            data.append({
                'City': city['name'],
                'Date': date.strftime('%Y-%m-%d'),
                'Sunrise': round(sunrise, 3),
                'Sunset': round(sunset, 3),
                'CTBegin': round(ctbegin, 3),
                'CTEnd': round(ctend, 3),
                'Daylight': round(daylight, 3),
                'DaylightChange': round(daylight_change, 3) if daylight_change is not None else 'null'
            })

            # Next day
            date = date + timedelta_day
            daylight_yesterday = daylight


    # Write the CSV
    with open('sunrise.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, [
            'City',
            'Date',
            'CTBegin',
            'Sunrise',
            'Sunset',
            'CTEnd',
            'Daylight',
            'DaylightChange'
        ])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


######################################################################

if __name__ == '__main__':
    main()
