# Seattle Sunrise

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
yFields.0: CTEnd
yFields.1: Sunset
yFields.2: Sunrise
yFields.3: CTBegin

xTickCount: 5
yTickCount: 8
~~~


# Seattle Daylight

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
yFields.0: Daylight

xTickCount: 5
yTickCount: 8
~~~


# Seattle Daylight Change

~~~ line-chart
dataURL: sunrise.csv

width: 1024
height: 480

filters.0.datetime.field: Date
filters.0.datetime.gte: 2021-01-01
filters.0.datetime.lt: 2022-01-01

filters.1.string.field: City
filters.1.string.in.0: Seattle WA

filters.2.number.field: DaylightChange
filters.2.number.lt: 50
filters.2.number.gt: -50

xField: Date
yFields.0: DaylightChange

xTickCount: 5
yTickCount: 8
~~~


# Seattle / San Diego / Juneau Comparison

~~~ line-chart
dataURL: sunrise.csv

width: 1024
height: 480

filters.0.datetime.field: Date
filters.0.datetime.gte: 2021-01-01
filters.0.datetime.lt: 2022-01-01

filters.1.string.field: City
filters.1.string.in.0: Seattle WA
filters.1.string.in.1: Juneau AK
filters.1.string.in.2: San Diego CA

xField: Date
yFields.0: Sunrise
#yFields.1: Sunset
colorFields.0: City

xTickCount: 5
yTickCount: 8
~~~
