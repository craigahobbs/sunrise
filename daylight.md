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

filters.0.field: City
filters.0.vin.0: city

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

categoryFields.0: City
categoryFields.1: YEAR(Date)
fields.0: AVERAGE(Daylight)
fields.1: MIN(Daylight)
fields.2: MAX(Daylight)
fields.3: MAX(DaylightChange)

precision: 1
datetime: Year
~~~

The daylight chart shows daily daylight (in hours) over time.

~~~ line-chart
title: Daylight - {{city}}
width: 875
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.field: City
filters.0.vin.0: city

xField: Date
yFields.0: Daylight

precision: 0
datetime: Day

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 15
yTicks.start.number: 8
yTicks.end.number: 22
yTicks.skip: 1
~~~

The daylight-change chart shows the day-to-day change in daylight over time.

~~~ line-chart
title: Daylight Change - {{city}}
width: 875
height: 350

dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.field: City
filters.0.vin.0: city

xField: Date
yFields.0: DaylightChange

precision: 0
datetime: Day

xTicks.count: 13
xTicks.skip: 2

yTicks.count: 13
yTicks.start.number: -6
yTicks.end.number: 6
yTicks.skip: 1
~~~