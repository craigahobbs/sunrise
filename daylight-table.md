[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
Table |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

**Location:**
[Chicago](#var.vCity='Chicago') |
[Denver](#var.vCity='Denver') |
[Honolulu](#var.vCity='Honolulu') |
[Houston](#var.vCity='Houston') |
[Juneau](#var.vCity='Juneau') |
[Kansas City](#var.vCity='Kansas%20City') |
[Los Angeles](#var.vCity='Los%20Angeles') |
[Miami](#var.vCity='Miami') |
[New York](#var.vCity='New%20York') |
[Philadelphia](#var.vCity='Philadelphia') |
[Phoenix](#var.vCity='Phoenix') |
[San Francisco](#var.vCity='San%20Francisco') |
[Seattle](#var.vCity='Seattle')


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
