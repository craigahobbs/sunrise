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

var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Year
calc.0.expr: date(year([Date]), 1, 1)

filter: City == 'Juneau' && Date >= vStart && Date < vEnd && Daylight >= 17.3

agg.category.0: City
agg.category.1: Year
agg.measure.0.name: Days
agg.measure.0.field: Daylight
agg.measure.0.func: Count

datetime: Year
~~~

**Question:** Seattle's shortest day is 9.6 hours. How many days in Juneau are at least that short?

~~~ data-table
data.url: sunrise.csv

var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Year
calc.0.expr: date(year([Date]), 1, 1)

filter: City == 'Juneau' && Date >= vStart && Date < vEnd && Daylight <= 9.6

agg.category.0: City
agg.category.1: Year
agg.measure.0.name: Days
agg.measure.0.field: Daylight
agg.measure.0.func: Count

datetime: Year
~~~
