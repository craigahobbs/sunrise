[Home](#url=README.md) |
Sunrise/Sunset |
[Daylight](#url=daylight.md) |
[Table](#url=daylight-table.md) |
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


# Sunrise / Sunset

The following table shows the selected location's sunrise and sunset extremes.

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
agg.measure.0.name: Min Sunrise
agg.measure.0.field: Sunrise
agg.measure.0.func: Min
agg.measure.1.name: Max Sunrise
agg.measure.1.field: Sunrise
agg.measure.1.func: Max
agg.measure.2.name: Min Sunset
agg.measure.2.field: Sunset
agg.measure.2.func: Min
agg.measure.3.name: Max Sunset
agg.measure.3.field: Sunset
agg.measure.3.func: Max

precision: 1
datetime: Year

category.0: City
category.1: Year
~~~

The sunrise/sunset chart shows sunrise time (in hours) and sunset time over time.

~~~ line-chart
title: 'Sunrise / Sunset - ' + vCity
width: 1000
height: 500

data.url: sunrise.csv

var.vCity: 'Seattle'
var.vStart: date(year(now()), 1, 1)
var.vEnd: date(year(now()) + 1, 1, 1)

filter: City == vCity && Date >= vStart && Date < vEnd

x: Date
y.0: Sunset
y.1: Sunrise

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
