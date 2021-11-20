[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
Comparison |
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


# Daylight Comparison

The following table compares the selected location's daylight statistics with extreme latitudes.

~~~ data-table
dataURL: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.variable: city
filters.0.include.1.string: Juneau
filters.0.include.2.string: Honolulu
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Daylight
aggregation.measures.1.function: Average
aggregation.measures.2.field: Daylight
aggregation.measures.2.function: Min
aggregation.measures.3.field: Daylight
aggregation.measures.3.function: Max
aggregation.measures.4.field: DaylightChange
aggregation.measures.4.function: Max

sort.0.field: SUM(Daylight)
sort.0.desc: true

precision: 1
datetime: Year

categoryFields.0: City
categoryFields.1: YEAR(Date)
fields.0: SUM(Daylight)
fields.1: AVERAGE(Daylight)
fields.2: MIN(Daylight)
fields.3: MAX(Daylight)
fields.4: MAX(DaylightChange)
~~~

The daylight comparison chart compares the locations' daylight (in hours) over time.

~~~ line-chart
title: Daylight Comparison - {{city}}
width: 1000
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.variable: city
filters.0.include.1.string: Juneau
filters.0.include.2.string: Honolulu
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

precision: 0
datetime: Day

xField: Date
yFields.0: Daylight
colorFields.0: City

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 15
yTicks.start.number: 8
yTicks.end.number: 22
yTicks.skip: 1

xAnnotations.0.value.live.value: Today
~~~

The sunrise/sunset comparison chart compares the locations' sunrise time (in hours) and sunset time
over time.

~~~ line-chart
title: Sunrise/Sunset Comparison - {{city}}
width: 1000
height: 500

dataURL: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.variable: city
filters.0.include.1.string: Juneau
filters.0.include.2.string: Honolulu
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

precision: 0
datetime: Day

xField: Date
yFields.0: Sunset
yFields.1: Sunrise
colorFields.0: City

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 23
yTicks.start.number: 2
yTicks.end.number: 24
yTicks.skip: 1

xAnnotations.0.value.live.value: Today
~~~
