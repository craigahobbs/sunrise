[Home](#url=README.md) |
Sunrise/Sunset |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

**Location:**
[Chicago](#var.city='Chicago') |
[Denver](#var.city='Denver') |
[Honolulu](#var.city='Honolulu') |
[Houston](#var.city='Houston') |
[Juneau](#var.city='Juneau') |
[Kansas City](#var.city='Kansas%20City') |
[Los Angeles](#var.city='Los%20Angeles') |
[Miami](#var.city='Miami') |
[New York](#var.city='New%20York') |
[Philadelphia](#var.city='Philadelphia') |
[Phoenix](#var.city='Phoenix') |
[San Francisco](#var.city='San%20Francisco') |
[Seattle](#var.city='Seattle')


# Sunrise / Sunset

The following table shows the selected location's sunrise and sunset extremes.

~~~ data-table
data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date]), 1, 1)

filters.0: City == city
filters.1: (Date >= start) && (Date < end)

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
title: 'Sunrise / Sunset - ' + city
width: 1000
height: 500

data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

filters.0: City == city
filters.1: (Date >= start) && (Date < end)

precision: 0
datetime: Day

xField: Date
yFields.0: Sunset
yFields.1: Sunrise

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 23
yTicks.start: 2
yTicks.end: 24
yTicks.skip: 1

xAnnotations.0.value: today()
~~~
