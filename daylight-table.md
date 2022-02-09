[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
Table |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

~~~ markdown-script
markdownPrint( \
    '**Location:** ' + if(vCity != null, vCity, 'Seattle'), \
    "([Change](#url=city-select.md&var.vURL='daylight-table.md'))" \
)
~~~


# Daylight Table

The following table lists the selected location's monthly average daylight (in hours),
civil-twilight-begin time (in hours), and civil-twilight-end time (in hours).

~~~ data-table
data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Month
calc.0.expr: date(year([Date]), month([Date]), 1)

filter: City == vCity && Date >= vStart && Date < vEnd

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

precision: 1
datetime: Month

category.0: City
category.1: Month
~~~
