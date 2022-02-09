[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
Comparison |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

~~~ markdown-script
markdownPrint( \
    '**Location:** ' + if(vCity != null, vCity, 'Seattle'), \
    "([Change](#url=cities.md&var.vURL='compare.md'))" \
)
~~~


# Daylight Comparison

The following table compares the selected location's daylight statistics with extreme latitudes.

~~~ data-table
data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

calc.0.name: Year
calc.0.expr: date(year([Date]), 1, 1)

filter: (City == vCity || City == 'Juneau' || City == 'Honolulu') && Date >= vStart && Date < vEnd

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
agg.measure.4.name: Max DaylightChange
agg.measure.4.field: DaylightChange
agg.measure.4.func: Max

sort.0.field: Total Daylight
sort.0.desc: true

category.0: City
category.1: Year

precision: 1
datetime: Year
~~~

The daylight comparison chart compares the locations' daylight (in hours) over time.

~~~ line-chart
title: 'Daylight Comparison - ' + vCity
width: 1000
height: 350

data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

filter: (City == vCity || City == 'Juneau' || City == 'Honolulu') && Date >= vStart && Date < vEnd

x: Date
y.0: Daylight
color: City

xtick.count: 13
xtick.skip: 2

ytick.count: 15
ytick.start: 8
ytick.end: 22
ytick.skip: 1

xline.0.value: today()

precision: 0
datetime: Day
~~~

The sunrise/sunset comparison chart compares the locations' sunrise time (in hours) and sunset time
over time.

~~~ line-chart
title: 'Sunrise/Sunset Comparison - ' + vCity
width: 1000
height: 500

data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

filter: (City == vCity || City == 'Juneau' || City == 'Honolulu') && Date >= vStart && Date < vEnd

x: Date
y.0: Sunset
y.1: Sunrise
color: City

xtick.count: 13
xtick.skip: 2

ytick.count: 23
ytick.start: 2
ytick.end: 24
ytick.skip: 1

xline.0.value: today()

precision: 0
datetime: Day
~~~
