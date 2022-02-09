[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
Daylight |
[Table](#url=daylight-table.md) |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

~~~ markdown-script
markdownPrint( \
    '**Location:** ' + if(vCity != null, vCity, 'Seattle'), \
    "([Change](#url=city-select.md&var.vURL='daylight.md'))" \
)
~~~


# Daylight

The following table displays the daylight statistics for the selected location.

~~~ data-table
data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Year
calc.0.expr: date(year([Date]), 1, 1)

filter: City == vCity && Date >= vStart && Date < vEnd

agg.category.0: City
agg.category.1: Year
agg.measure.0.name: Avg Daylight
agg.measure.0.field: Daylight
agg.measure.0.func: Average
agg.measure.1.name: Min Daylight
agg.measure.1.field: Daylight
agg.measure.1.func: Min
agg.measure.2.name: Max Daylight
agg.measure.2.field: Daylight
agg.measure.2.func: Max
agg.measure.3.name: Max DaylightChange
agg.measure.3.field: DaylightChange
agg.measure.3.func: Max

precision: 1
datetime: Year

category.0: City
category.1: Year
~~~

The daylight chart shows daily daylight (in hours) over time.

~~~ line-chart
title: 'Daylight - ' + vCity
width: 875
height: 350

data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

filter: City == vCity && Date >= vStart && Date < vEnd

precision: 0
datetime: Day

x: Date
y.0: Daylight

xtick.count: 13
xtick.skip: 2

ytick.count: 15
ytick.start: 8
ytick.end: 22
ytick.skip: 1

xline.0.value: today()
~~~

The daylight-change chart shows the day-to-day change in daylight over time.

~~~ line-chart
title: 'Daylight Change - ' + vCity
width: 875
height: 350

data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

filter: City == vCity && Date >= vStart && Date < vEnd

precision: 0
datetime: Day

x: Date
y.0: DaylightChange

xtick.count: 13
xtick.skip: 2

ytick.count: 13
ytick.start: -6
ytick.end: 6
ytick.skip: 1

xline.0.value: today()

yline.0.value: 0
yline.0.label: ''
~~~
