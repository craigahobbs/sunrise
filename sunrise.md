[Home](#url=README.md) |
Sunrise/Sunset |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

**Location:**
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


# Sunrise / Sunset

The following table shows the selected location's sunrise and sunset extremes.

~~~ data-table
data.url: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date]), 1, 1)

filters.0.field: City
filters.0.includes.0.variable: city
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Year
aggregation.measures.0.field: Sunrise
aggregation.measures.0.function: Min
aggregation.measures.1.field: Sunrise
aggregation.measures.1.function: Max
aggregation.measures.2.field: Sunset
aggregation.measures.2.function: Min
aggregation.measures.3.field: Sunset
aggregation.measures.3.function: Max

precision: 1
datetime: Year

categoryFields.0: City
categoryFields.1: Year
~~~

The sunrise/sunset chart shows sunrise time (in hours) and sunset time over time.

~~~ line-chart
title: Sunrise / Sunset - {{city}}
width: 1000
height: 500

data.url: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.includes.0.variable: city
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

precision: 0
datetime: Day

xField: Date
yFields.0: Sunset
yFields.1: Sunrise

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 23
yTicks.start.number: 2
yTicks.end.number: 24
yTicks.skip: 1

xAnnotations.0.value.live.value: Today
~~~
