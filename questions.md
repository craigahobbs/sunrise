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
dataURL: sunrise.csv

variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.string: Juneau
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end
filters.2.field: Daylight
filters.2.gte.number: 17.3

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Count

precision: 0
datetime: Year

categoryFields.0: City
categoryFields.1: YEAR(Date)
~~~

**Question:** Seattle's shortest day is 9.6 hours. How many days in Juneau are at least that short?

~~~ data-table
dataURL: sunrise.csv

variables.start.live.value: Year
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: City
filters.0.include.0.string: Juneau
filters.1.field: Date
filters.1.gte.variable: start
filters.1.lt.variable: end
filters.2.field: Daylight
filters.2.lte.number: 9.6

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Count

precision: 0
datetime: Year

categoryFields.0: City
categoryFields.1: YEAR(Date)
~~~
