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
height: 550

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

xTicks.auto.count: 13
xTicks.auto.skip: 2

yTicks.values.0.value.number: 2
yTicks.values.1.value.number: 3
yTicks.values.2.value.number: 4
yTicks.values.3.value.number: 5
yTicks.values.4.value.number: 6
yTicks.values.5.value.number: 7
yTicks.values.6.value.number: 8
yTicks.values.7.value.number: 9
yTicks.values.8.value.number: 10
yTicks.values.9.value.number: 11
yTicks.values.10.value.number: 12
yTicks.values.11.value.number: 13
yTicks.values.12.value.number: 14
yTicks.values.13.value.number: 15
yTicks.values.14.value.number: 16
yTicks.values.15.value.number: 17
yTicks.values.16.value.number: 18
yTicks.values.17.value.number: 19
yTicks.values.18.value.number: 20
yTicks.values.19.value.number: 21
yTicks.values.20.value.number: 22
yTicks.values.21.value.number: 23
yTicks.values.22.value.number: 24

yTicks.values.1.label:
yTicks.values.3.label:
yTicks.values.5.label:
yTicks.values.7.label:
yTicks.values.9.label:
yTicks.values.11.label:
yTicks.values.13.label:
yTicks.values.15.label:
yTicks.values.17.label:
yTicks.values.19.label:
yTicks.values.21.label:
~~~


### Daylight

~~~ line-chart
title: Daylight - {{city}}
width: 875
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.vin.0: city

xField: Date
yFields.0: Daylight

precision: 0

xTicks.auto.count: 13
xTicks.auto.skip: 2

yTicks.values.0.value.number: 8
yTicks.values.1.value.number: 9
yTicks.values.2.value.number: 10
yTicks.values.3.value.number: 11
yTicks.values.4.value.number: 12
yTicks.values.5.value.number: 13
yTicks.values.6.value.number: 14
yTicks.values.7.value.number: 15
yTicks.values.8.value.number: 16
yTicks.values.9.value.number: 17
yTicks.values.10.value.number: 18
yTicks.values.11.value.number: 19
yTicks.values.12.value.number: 20
yTicks.values.13.value.number: 21
yTicks.values.14.value.number: 22

yTicks.values.1.label:
yTicks.values.3.label:
yTicks.values.5.label:
yTicks.values.7.label:
yTicks.values.9.label:
yTicks.values.11.label:
yTicks.values.13.label:
~~~


### Daylight Change

~~~ line-chart
title: Daylight Change - {{city}}
width: 875
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.string.field: City
filters.0.string.vin.0: city

xField: Date
yFields.0: DaylightChange

precision: 0

xTicks.auto.count: 13
xTicks.auto.skip: 2

yTickCount: 0
yTicks.values.0.value.number: -6
yTicks.values.1.value.number: -5
yTicks.values.2.value.number: -4
yTicks.values.3.value.number: -3
yTicks.values.4.value.number: -2
yTicks.values.5.value.number: -1
yTicks.values.6.value.number: 0
yTicks.values.7.value.number: 1
yTicks.values.8.value.number: 2
yTicks.values.9.value.number: 3
yTicks.values.10.value.number: 4
yTicks.values.11.value.number: 5
yTicks.values.12.value.number: 6

yTicks.values.1.label:
yTicks.values.3.label:
yTicks.values.5.label:
yTicks.values.7.label:
yTicks.values.9.label:
yTicks.values.11.label:
~~~


### Daylight Comparison

~~~ line-chart
title: Daylight Comparison - {{city}}
width: 1000
height: 350

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

xTicks.auto.count: 13
xTicks.auto.skip: 2

yTicks.values.0.value.number: 8
yTicks.values.1.value.number: 9
yTicks.values.2.value.number: 10
yTicks.values.3.value.number: 11
yTicks.values.4.value.number: 12
yTicks.values.5.value.number: 13
yTicks.values.6.value.number: 14
yTicks.values.7.value.number: 15
yTicks.values.8.value.number: 16
yTicks.values.9.value.number: 17
yTicks.values.10.value.number: 18
yTicks.values.11.value.number: 19
yTicks.values.12.value.number: 20
yTicks.values.13.value.number: 21
yTicks.values.14.value.number: 22

yTicks.values.1.label:
yTicks.values.3.label:
yTicks.values.5.label:
yTicks.values.7.label:
yTicks.values.9.label:
yTicks.values.11.label:
yTicks.values.13.label:
~~~


### Sunrise/Sunset Comparison

~~~ line-chart
title: Sunrise/Sunset Comparison - {{city}}
width: 1000
height: 550

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

xTicks.auto.count: 13
xTicks.auto.skip: 2

yTicks.values.0.value.number: 2
yTicks.values.1.value.number: 3
yTicks.values.2.value.number: 4
yTicks.values.3.value.number: 5
yTicks.values.4.value.number: 6
yTicks.values.5.value.number: 7
yTicks.values.6.value.number: 8
yTicks.values.7.value.number: 9
yTicks.values.8.value.number: 10
yTicks.values.9.value.number: 11
yTicks.values.10.value.number: 12
yTicks.values.11.value.number: 13
yTicks.values.12.value.number: 14
yTicks.values.13.value.number: 15
yTicks.values.14.value.number: 16
yTicks.values.15.value.number: 17
yTicks.values.16.value.number: 18
yTicks.values.17.value.number: 19
yTicks.values.18.value.number: 20
yTicks.values.19.value.number: 21
yTicks.values.20.value.number: 22
yTicks.values.21.value.number: 23
yTicks.values.22.value.number: 24

yTicks.values.1.label:
yTicks.values.3.label:
yTicks.values.5.label:
yTicks.values.7.label:
yTicks.values.9.label:
yTicks.values.11.label:
yTicks.values.13.label:
yTicks.values.15.label:
yTicks.values.17.label:
yTicks.values.19.label:
yTicks.values.21.label:
~~~
