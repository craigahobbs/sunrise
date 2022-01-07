[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
Questions


# Questions

**Question:** Seattle's longest day is 17.3 hours. How many days in Juneau are at least that long?

~~~ data-table
data.url: sunrise.csv

variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date]), 1, 1)

filters.0: City == 'Juneau'
filters.1: (Date >= start) && (Date < end)
filters.2: Daylight >= 17.3

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Count

precision: 0
datetime: Year

categoryFields.0: City
categoryFields.1: Year
~~~

**Question:** Seattle's shortest day is 9.6 hours. How many days in Juneau are at least that short?

~~~ data-table
data.url: sunrise.csv

variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date]), 1, 1)

filters.0: City == 'Juneau'
filters.1: (Date >= start) && (Date < end)
filters.2: Daylight <= 9.6

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Count

precision: 0
datetime: Year

categoryFields.0: City
categoryFields.1: Year
~~~
