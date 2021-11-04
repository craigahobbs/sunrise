# 2021 Seattle Sunrise / Sunset Chart

~~~ line-chart
dataURL: sunrise.csv

width: 1024
height: 480

filters.0.datetime.field: Date
filters.0.datetime.gte: 2021-01-01
filters.0.datetime.lt: 2022-01-01

filters.1.string.field: City
filters.1.string.in.0: Seattle WA

xField: Date
yFields.0: Sunrise
yFields.1: Sunset
yFields.2: CTBegin
yFields.3: CTEnd

xTickCount: 5
yTickCount: 8
~~~


# 2021 Seattle and KC Sunrise / Sunset Chart

~~~ line-chart
dataURL: sunrise.csv

width: 1024
height: 480

filters.0.datetime.field: Date
filters.0.datetime.gte: 2021-01-01
filters.0.datetime.lt: 2022-01-01

filters.1.string.field: City
filters.1.string.in.0: Seattle WA
filters.1.string.in.1: Kansas City KS

xField: Date
yFields.0: Sunrise
#yFields.1: Sunset
#yFields.2: CTBegin
#yFields.3: CTEnd
colorFields.0: City

xTickCount: 5
yTickCount: 8
~~~
