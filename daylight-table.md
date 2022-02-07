[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
Table |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

**Location:**
[Chicago](#var.city='Chicago') |
[Denver](#var.city='Denver') |
[Honolulu](#var.city='Honolulu') |
[Houston](#var.city='Houston') |
[Juneau](#var.city='Juneau') |
[Kansas City](#var.city='Kansas%20City') |
[Los Angeles](#var.city='Los%20Angeles') |
[Miami](#var.city='Miami') |
[New York](#var.city='New%20York') |
[Philadelphia](#var.city='Philadelphia') |
[Phoenix](#var.city='Phoenix') |
[San Francisco](#var.city='San%20Francisco') |
[Seattle](#var.city='Seattle')


# Daylight Table

The following table lists the selected location's monthly average daylight (in hours),
civil-twilight-begin time (in hours), and civil-twilight-end time (in hours).

~~~ data-table
data.url: sunrise.csv

variables.city: 'Seattle'
variables.start: date(year(now()), 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date]), month([Date]), 1)

filter: City == city && Date >= start && Date < end

aggregation.categoryFields.0: City
aggregation.categoryFields.1: Month
aggregation.measures.0.name: Avg Daylight
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Average
aggregation.measures.1.name: Avg TwilightRise
aggregation.measures.1.field: TwilightRise
aggregation.measures.1.function: Average
aggregation.measures.2.name: Avg TwilightSet
aggregation.measures.2.field: TwilightSet
aggregation.measures.2.function: Average

precision: 1
datetime: Month

categoryFields.0: City
categoryFields.1: Month
~~~
