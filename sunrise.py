# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE

# pylint: disable=no-member

import argparse
import csv
from datetime import datetime, timedelta, timezone
import sys

import ephem
import pytz


# The list of cities for which to generate sunrise data
CITIES = [
    {'name': 'Chicago',       'lat': '41.8781', 'lon': '-87.6298',  'tz': 'US/Central'},
    {'name': 'Denver',        'lat': '39.7392', 'lon': '-104.9903', 'tz': 'US/Mountain'},
    {'name': 'Honolulu',      'lat': '21.3069', 'lon': '-157.8583', 'tz': 'US/Hawaii'},
    {'name': 'Houston',       'lat': '29.7604', 'lon': '-95.3698',  'tz': 'US/Central'},
    {'name': 'Juneau',        'lat': '58.3019', 'lon': '-134.4197', 'tz': 'US/Alaska'},
    {'name': 'Kansas City',   'lat': '39.1155', 'lon': '-94.6268',  'tz': 'US/Central'},
    {'name': 'Los Angeles',   'lat': '34.0522', 'lon': '-118.2437', 'tz': 'US/Pacific'},
    {'name': 'Miami',         'lat': '25.7617', 'lon': '-80.1918',  'tz': 'US/Eastern'},
    {'name': 'New York',      'lat': '40.7128', 'lon': '-74.0060',  'tz': 'US/Eastern'},
    {'name': 'Philadelphia',  'lat': '39.9526', 'lon': '-75.1652',  'tz': 'US/Eastern'},
    {'name': 'Phoenix',       'lat': '33.4484', 'lon': '-112.0740', 'tz': 'US/Mountain'},
    {'name': 'San Francisco', 'lat': '37.7749', 'lon': '-122.4194', 'tz': 'US/Pacific'},
    {'name': 'Seattle',       'lat': '47.6062', 'lon': '-122.3321', 'tz': 'US/Pacific'}
]


def main():
    # Command line arguments
    parser = argparse.ArgumentParser(description='Generate sunrise data')
    parser.add_argument('-y', '--year', type=int, nargs='?', default=datetime.now().year, help='The year to start generating sunrise data')
    parser.add_argument('-n', '--years', type=int, nargs='?', default=1, help='The number of years of sunrise data to generate')
    args = parser.parse_args()

    # Initialize the ephem observer
    observer = ephem.Observer()
    observer.pressure = 0.0

    # Generate the sunrise data city by city
    data = []
    timedelta_day = timedelta(days=1)
    for city in CITIES:
        city_tz = pytz.timezone(city['tz'])

        # Update the observer's location
        observer.lat = city['lat']
        observer.lon = city['lon']

        # For each day add one sunrise date row
        noon_utc = datetime(args.year, 1, 1, 12, tzinfo=city_tz).astimezone(timezone.utc)
        date = noon_utc.replace(year=args.year, month=1, day=1, tzinfo=None) - timedelta_day
        end_utc = datetime(args.year + args.years, 1, 1, tzinfo=city_tz).astimezone(timezone.utc)
        end_date = end_utc.replace(year=args.year + args.years, month=1, day=1, tzinfo=None)
        daylight_yesterday = None
        while date < end_date:
            # Update the observer's date
            observer.date = date

            # Calculate sunrise, sunset (horizon '-0:34')
            observer.horizon = '-0:34'
            sunrise = local_time_hours(observer.previous_rising(ephem.Sun()).datetime(), city_tz)
            sunset = local_time_hours(observer.next_setting(ephem.Sun()).datetime(), city_tz)

            # Calculate civil twilight (horizon @ -6)
            observer.horizon = '-6'
            twilight_rise = local_time_hours(observer.previous_rising(ephem.Sun(), use_center=True).datetime(), city_tz)
            twilight_set = local_time_hours(observer.next_setting(ephem.Sun(), use_center=True).datetime(), city_tz)

            # Compute daylight
            daylight = sunset - sunrise
            daylight_change = (daylight - daylight_yesterday) * 60 if daylight_yesterday is not None else None

            # Create the sunrise data row
            if daylight_change is not None:
                data.append({
                    'City': city['name'],
                    'Date': date.strftime('%Y-%m-%d'),
                    'Sunrise': round(sunrise, 3),
                    'Sunset': round(sunset, 3),
                    'TwilightRise': round(twilight_rise, 3),
                    'TwilightSet': round(twilight_set, 3),
                    'Daylight': round(daylight, 3),
                    'DaylightChange': round(daylight_change, 3) if daylight_change is not None else 'null'
                })

            # Next day
            date = date + timedelta_day
            daylight_yesterday = daylight

    # Write the CSV
    writer = csv.DictWriter(sys.stdout, [
        'City',
        'Date',
        'Sunrise',
        'Sunset',
        'TwilightRise',
        'TwilightSet',
        'Daylight',
        'DaylightChange'
    ])
    writer.writeheader()
    for row in data:
        writer.writerow(row)


# Helper function to compute the local time in hours (0-24)
def local_time_hours(naive_gmt_dt, local_tz):
    local_dt = naive_gmt_dt.replace(tzinfo=timezone.utc).astimezone(local_tz)
    return local_dt.hour + (local_dt.minute + (local_dt.second + local_dt.microsecond / 1000000) / 60) / 60


######################################################################

if __name__ == '__main__':
    main()
