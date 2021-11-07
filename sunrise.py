import csv
import datetime

import ephem
import pytz


# The years for which to generate sunrise data
START_YEAR = 2021
N_YEARS = 1


# The list of cities for which to generate sunrise data
CITIES = [
    {'name': 'Colorado Springs CO', 'lat': '38.8339', 'lon': '-104.8214', 'tz': pytz.timezone('US/Mountain')},
    {'name': 'Juneau AK',           'lat': '58.3019', 'lon': '-134.4197', 'tz': pytz.timezone('US/Alaska')},
    {'name': 'Kansas City KS',      'lat': '39.1155', 'lon': '-94.6268',  'tz': pytz.timezone('US/Central')},
    {'name': 'San Diego CA',        'lat': '32.7157', 'lon': '-117.1611', 'tz': pytz.timezone('US/Pacific')},
    {'name': 'Seattle WA',          'lat': '47.6062', 'lon': '-122.3321', 'tz': pytz.timezone('US/Pacific')}
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
        observer.lat = city['lat']
        observer.lon = city['lon']

        # For each day add one sunrise date row
        date = datetime.datetime(START_YEAR, 1, 1, 12, tzinfo=city['tz']).astimezone(datetime.timezone.utc).replace(tzinfo=None)
        end_date = datetime.datetime(START_YEAR + N_YEARS, 1, 1, tzinfo=city['tz']).astimezone(datetime.timezone.utc).replace(tzinfo=None)
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
            twilight_rise_dt = observer.previous_rising(ephem.Sun(), use_center=True).datetime()
            twilight_set_dt = observer.next_setting(ephem.Sun(), use_center=True).datetime()
            twilight_rise = local_time_hours(twilight_rise_dt, city['tz'])
            twilight_set = local_time_hours(twilight_set_dt, city['tz'])

            # Compute daylight
            daylight = (twilight_set_dt - twilight_rise_dt).total_seconds() / (60 * 60)
            daylight_change = (daylight - daylight_yesterday) * 60 if daylight_yesterday is not None else None

            # Create the sunrise data row
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
    with open('sunrise.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, [
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


######################################################################

if __name__ == '__main__':
    main()
