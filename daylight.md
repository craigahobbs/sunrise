[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
Daylight |
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


# Daylight

The following table displays the daylight statistics for the selected location.

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
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Average
aggregation.measures.1.field: Daylight
aggregation.measures.1.function: Min
aggregation.measures.2.field: Daylight
aggregation.measures.2.function: Max
aggregation.measures.3.field: DaylightChange
aggregation.measures.3.function: Max

precision: 1
datetime: Year

categoryFields.0: City
categoryFields.1: Year
~~~

The daylight chart shows daily daylight (in hours) over time.

~~~ line-chart
title: 'Daylight - ' + city
width: 875
height: 350

data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

filters.0: City == city
filters.1: (Date >= start) && (Date < end)

precision: 0
datetime: Day

xField: Date
yFields.0: Daylight

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 15
yTicks.start: 8
yTicks.end: 22
yTicks.skip: 1

xAnnotations.0.value: today()
~~~

The daylight-change chart shows the day-to-day change in daylight over time.

~~~ line-chart
title: 'Daylight Change - ' + city
width: 875
height: 350

data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

filters.0: City == city
filters.1: (Date >= start) && (Date < end)

precision: 0
datetime: Day

xField: Date
yFields.0: DaylightChange

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 13
yTicks.start: -6
yTicks.end: 6
yTicks.skip: 1

xAnnotations.0.value: today()

yAnnotations.0.value: 0
yAnnotations.0.label: ''
~~~
