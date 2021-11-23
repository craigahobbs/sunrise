[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
[Comparison](#url=compare.md) |
Rankings |
[Questions](#url=questions.md)


# Daylight Rankings

The following table ranks U.S. cities by their total annual daylight hours.

~~~ data-table
data.url: sunrise.csv

variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date
filters.0.gte.variable: start
filters.0.lt.variable: end

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

sorts.0.field: YEAR(Date)
sorts.1.field: AVERAGE(Daylight)
sorts.1.desc: true

precision: 1
datetime: Year

categoryFields.0: YEAR(Date)
categoryFields.1: City
~~~


## US Daylight (Monthly)

The table below ranks the top 10 U.S. cities by their total monthly daylight hours.

~~~ data-table
data.url: sunrise.csv

variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Month
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Average
aggregation.measures.1.field: TwilightRise
aggregation.measures.1.function: Average
aggregation.measures.2.field: TwilightSet
aggregation.measures.2.function: Average

sorts.0.field: MONTH(Date)
sorts.1.field: AVERAGE(Daylight)
sorts.1.desc: true

top.count: 10
top.categoryFields.0: MONTH(Date)

precision: 1
datetime: Month

categoryFields.0: MONTH(Date)
categoryFields.1: City
~~~
