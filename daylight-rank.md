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

variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date]), 1, 1)

filters.0: (Date >= start) && (Date < end)

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Daylight
aggregation.measures.1.function: Average
aggregation.measures.2.field: Daylight
aggregation.measures.2.function: Min
aggregation.measures.3.field: Daylight
aggregation.measures.3.function: Max

sorts.0.field: Year
sorts.1.field: AVERAGE(Daylight)
sorts.1.desc: true

precision: 1
datetime: Year

categoryFields.0: Year
categoryFields.1: City
~~~


## US Daylight (Monthly)

The table below ranks the top 10 U.S. cities by their total monthly daylight hours.

~~~ data-table
data.url: sunrise.csv

variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date]), month([Date]), 1)

filters.0: (Date >= start) && (Date < end)

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Month
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Average
aggregation.measures.1.field: TwilightRise
aggregation.measures.1.function: Average
aggregation.measures.2.field: TwilightSet
aggregation.measures.2.function: Average

sorts.0.field: Month
sorts.1.field: AVERAGE(Daylight)
sorts.1.desc: true

top.count: 10
top.categoryFields.0: Month

precision: 1
datetime: Month

categoryFields.0: Month
categoryFields.1: City
~~~
