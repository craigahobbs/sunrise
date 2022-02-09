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

var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Year
calc.0.expr: date(year([Date]), 1, 1)

filter: Date >= vStart && Date < vEnd

agg.category.0: City
agg.category.1: Year
agg.measure.0.name: Total Daylight
agg.measure.0.field: Daylight
agg.measure.0.func: Sum
agg.measure.1.name: Avg Daylight
agg.measure.1.field: Daylight
agg.measure.1.func: Average
agg.measure.2.name: Min Daylight
agg.measure.2.field: Daylight
agg.measure.2.func: Min
agg.measure.3.name: Max Daylight
agg.measure.3.field: Daylight
agg.measure.3.func: Max

sort.0.field: Year
sort.1.field: Avg Daylight
sort.1.desc: true

category.0: Year
category.1: City

precision: 1
datetime: Year
~~~


## US Daylight (Monthly)

The table below ranks the top 10 U.S. cities by their total monthly daylight hours.

~~~ data-table
data.url: sunrise.csv

var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Month
calc.0.expr: date(year([Date]), month([Date]), 1)

filter: Date >= vStart && Date < vEnd

agg.category.0: City
agg.category.1: Month
agg.measure.0.name: Avg Daylight
agg.measure.0.field: Daylight
agg.measure.0.func: Average
agg.measure.1.name: Avg TwilightRise
agg.measure.1.field: TwilightRise
agg.measure.1.func: Average
agg.measure.2.name: Avg TwilightSet
agg.measure.2.field: TwilightSet
agg.measure.2.func: Average

sort.0.field: Month
sort.1.field: Avg Daylight
sort.1.desc: true

top.count: 10
top.category.0: Month

category.0: Month
category.1: City

precision: 1
datetime: Month
~~~
