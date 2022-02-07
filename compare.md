[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
Comparison |
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


# Daylight Comparison

The following table compares the selected location's daylight statistics with extreme latitudes.

~~~ data-table
data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date]), 1, 1)

filter: (City == city || City == 'Juneau' || City == 'Honolulu') && Date >= start && Date < end

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Year
aggregation.measures.0.name: Total Daylight
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Sum
aggregation.measures.1.name: Avg Daylight
aggregation.measures.1.field: Daylight
aggregation.measures.1.function: Average
aggregation.measures.2.name: Min Daylight
aggregation.measures.2.field: Daylight
aggregation.measures.2.function: Min
aggregation.measures.3.name: Max Daylight
aggregation.measures.3.field: Daylight
aggregation.measures.3.function: Max
aggregation.measures.4.name: Max DaylightChange
aggregation.measures.4.field: DaylightChange
aggregation.measures.4.function: Max

sorts.0.field: Total Daylight
sorts.0.desc: true

precision: 1
datetime: Year

categoryFields.0: City
categoryFields.1: Year
~~~

The daylight comparison chart compares the locations' daylight (in hours) over time.

~~~ line-chart
title: 'Daylight Comparison - ' + city
width: 1000
height: 350

data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

filter: (City == city || City == 'Juneau' || City == 'Honolulu') && Date >= start && Date < end

precision: 0
datetime: Day

xField: Date
yFields.0: Daylight
colorField: City

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 15
yTicks.start: 8
yTicks.end: 22
yTicks.skip: 1

xAnnotations.0.value: today()
~~~

The sunrise/sunset comparison chart compares the locations' sunrise time (in hours) and sunset time
over time.

~~~ line-chart
title: 'Sunrise/Sunset Comparison - ' + city
width: 1000
height: 500

data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

filter: (City == city || City == 'Juneau' || City == 'Honolulu') && Date >= start && Date < end

precision: 0
datetime: Day

xField: Date
yFields.0: Sunset
yFields.1: Sunrise
colorField: City

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 23
yTicks.start: 2
yTicks.end: 24
yTicks.skip: 1

xAnnotations.0.value: today()
~~~
