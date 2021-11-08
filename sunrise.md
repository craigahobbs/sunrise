# US Cities Sunrise Charts

[Chicago](#variables.city.string=Chicago) |
[Denver](#variables.city.string=Denver) |
[Honolulu](#variables.city.string=Honolulu) |
[Houston](#variables.city.string=Houston) |
[Juneau](#variables.city.string=Juneau) |
[Kansas City](#variables.city.string=Kansas%20City) |
[Los Angeles](#variables.city.string=Los%20Angeles) |
[Miami](#variables.city.string=Miami) |
[New York](#variables.city.string=New%20York) |
[Philadelphia](#variables.city.string=Philadelphia) |
[Phoenix](#variables.city.string=Phoenix) |
[San Francisco](#variables.city.string=San%20Francisco) |
[Seattle](#variables.city.string=Seattle)


### Sunrise / Sunset

~~~ line-chart
title: Sunrise - {{city}}
width: 1000
height: 450

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.vin.0: city

xField: Date
yFields.0: TwilightSet
yFields.1: Sunset
yFields.2: Sunrise
yFields.3: TwilightRise

precision: 0

xTickCount: 0
xTicks.0.value.datetime: 2021-01-01
xTicks.1.value.datetime: 2021-02-01
xTicks.2.value.datetime: 2021-03-01
xTicks.3.value.datetime: 2021-04-01
xTicks.4.value.datetime: 2021-05-01
xTicks.5.value.datetime: 2021-06-01
xTicks.6.value.datetime: 2021-07-01
xTicks.7.value.datetime: 2021-08-01
xTicks.8.value.datetime: 2021-09-01
xTicks.9.value.datetime: 2021-10-01
xTicks.10.value.datetime: 2021-11-01
xTicks.11.value.datetime: 2021-12-01
xTicks.12.value.datetime: 2022-01-01

# Hide even-month X-axis tick labels
xTicks.1.label:
xTicks.3.label:
xTicks.5.label:
xTicks.7.label:
xTicks.9.label:
xTicks.11.label:

yTickCount: 0
yTicks.0.value.number: 1
yTicks.1.value.number: 2
yTicks.2.value.number: 3
yTicks.3.value.number: 4
yTicks.4.value.number: 5
yTicks.5.value.number: 6
yTicks.6.value.number: 7
yTicks.7.value.number: 8
yTicks.8.value.number: 9
yTicks.9.value.number: 10
yTicks.10.value.number: 11
yTicks.11.value.number: 12
yTicks.12.value.number: 13
yTicks.13.value.number: 14
yTicks.14.value.number: 15
yTicks.15.value.number: 16
yTicks.16.value.number: 17
yTicks.17.value.number: 18
yTicks.18.value.number: 19
yTicks.19.value.number: 20
yTicks.20.value.number: 21
yTicks.21.value.number: 22
yTicks.22.value.number: 23
yTicks.23.value.number: 24

# Hide odd-hour Y-axis labels
yTicks.0.label:
yTicks.2.label:
yTicks.4.label:
yTicks.6.label:
yTicks.8.label:
yTicks.10.label:
yTicks.12.label:
yTicks.14.label:
yTicks.16.label:
yTicks.18.label:
yTicks.20.label:
yTicks.22.label:
~~~


### Daylight

~~~ line-chart
title: Daylight - {{city}}
width: 875
height: 450

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.vin.0: city

xField: Date
yFields.0: Daylight

precision: 0

xTickCount: 0
xTicks.0.value.datetime: 2021-01-01
xTicks.1.value.datetime: 2021-03-01
xTicks.2.value.datetime: 2021-05-01
xTicks.3.value.datetime: 2021-07-01
xTicks.4.value.datetime: 2021-09-01
xTicks.5.value.datetime: 2021-11-01
xTicks.6.value.datetime: 2022-01-01

yTickCount: 0
yTicks.0.value.number: 8
yTicks.1.value.number: 10
yTicks.2.value.number: 12
yTicks.3.value.number: 14
yTicks.4.value.number: 16
yTicks.5.value.number: 18
yTicks.6.value.number: 20
yTicks.7.value.number: 22
~~~


### Daylight Change

~~~ line-chart
title: Daylight Change - {{city}}
width: 875
height: 450

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.vin.0: city

xField: Date
yFields.0: DaylightChange

precision: 0

xTickCount: 0
xTicks.0.value.datetime: 2021-01-01
xTicks.1.value.datetime: 2021-03-01
xTicks.2.value.datetime: 2021-05-01
xTicks.3.value.datetime: 2021-07-01
xTicks.4.value.datetime: 2021-09-01
xTicks.5.value.datetime: 2021-11-01
xTicks.6.value.datetime: 2022-01-01

yTickCount: 0
yTicks.0.value.number: -6
yTicks.1.value.number: -4
yTicks.2.value.number: -2
yTicks.3.value.number: 0
yTicks.4.value.number: 2
yTicks.5.value.number: 4
yTicks.6.value.number: 6
~~~


### Daylight Comparison

~~~ line-chart
title: Daylight Comparison - {{city}}
width: 1000
height: 450

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.in.0: Juneau
filters.0.string.in.1: Honolulu
filters.0.string.vin.0: city

xField: Date
yFields.0: Daylight
colorFields.0: City

precision: 0

xTickCount: 0
xTicks.0.value.datetime: 2021-01-01
xTicks.1.value.datetime: 2021-03-01
xTicks.2.value.datetime: 2021-05-01
xTicks.3.value.datetime: 2021-07-01
xTicks.4.value.datetime: 2021-09-01
xTicks.5.value.datetime: 2021-11-01
xTicks.6.value.datetime: 2022-01-01

yTickCount: 0
yTicks.0.value.number: 8
yTicks.1.value.number: 10
yTicks.2.value.number: 12
yTicks.3.value.number: 14
yTicks.4.value.number: 16
yTicks.5.value.number: 18
yTicks.6.value.number: 20
yTicks.7.value.number: 22
~~~


### Sunrise/Sunset Comparison

~~~ line-chart
title: Sunrise/Sunset Comparison - {{city}}
width: 1000
height: 450

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.in.0: Juneau
filters.0.string.in.1: Honolulu
filters.0.string.vin.0: city

xField: Date
yFields.0: Sunset
yFields.1: Sunrise
colorFields.0: City

precision: 0

xTickCount: 0
xTicks.0.value.datetime: 2021-01-01
xTicks.1.value.datetime: 2021-03-01
xTicks.2.value.datetime: 2021-05-01
xTicks.3.value.datetime: 2021-07-01
xTicks.4.value.datetime: 2021-09-01
xTicks.5.value.datetime: 2021-11-01
xTicks.6.value.datetime: 2022-01-01

yTickCount: 0
yTicks.0.value.number: 2
yTicks.1.value.number: 4
yTicks.2.value.number: 6
yTicks.3.value.number: 8
yTicks.4.value.number: 10
yTicks.5.value.number: 12
yTicks.6.value.number: 14
yTicks.7.value.number: 16
yTicks.8.value.number: 18
yTicks.9.value.number: 20
yTicks.10.value.number: 22
yTicks.11.value.number: 24
~~~
