[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
Daylight |
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


# Daylight

The following table displays the daylight statistics for the selected location.

~~~ data-table
dataURL: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.variable: city
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Year
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
categoryFields.1: YEAR(Date)
fields.0: AVERAGE(Daylight)
fields.1: MIN(Daylight)
fields.2: MAX(Daylight)
fields.3: MAX(DaylightChange)
~~~

The daylight chart shows daily daylight (in hours) over time.

~~~ line-chart
title: Daylight - {{city}}
width: 875
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.variable: city
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

precision: 0
datetime: Day

xField: Date
yFields.0: Daylight

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 15
yTicks.start.number: 8
yTicks.end.number: 22
yTicks.skip: 1

xAnnotations.0.value.live.value: Today
~~~

The daylight-change chart shows the day-to-day change in daylight over time.

~~~ line-chart
title: Daylight Change - {{city}}
width: 875
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle
variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.variable: city
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end

precision: 0
datetime: Day

xField: Date
yFields.0: DaylightChange

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 13
yTicks.start.number: -6
yTicks.end.number: 6
yTicks.skip: 1

xAnnotations.0.value.live.value: Today
~~~
