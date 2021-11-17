[Home](#url=README.md) |
[Sunrise/Sunset](#url=sunrise.md) |
[Daylight](#url=daylight.md) |
Table |
[Comparison](#url=compare.md) |
[Rankings](#url=daylight-rank.md) |
[Questions](#url=questions.md)

**Location:**
[Chicago](#variables.city.string=Chicago) |
[Denver](#variables.city.string=Denver) |
[Honolulu](#variables.city.string=Honolulu) |
[Houston](#variables.city.string=Houston) |
[Juneau](#variables.city.string=Juneau) |
[Kansas City](#variables.city.string=Kansas%20City) |
[Los Angeles](#variables.city.string=Los%20Angeles) |
[Miami](#variables.city.string=Miami) |
[New York](#variables.city.string=New%20York) |
[Philadelphia](#variables.city.string=Philadelphia) |
[Phoenix](#variables.city.string=Phoenix) |
[San Francisco](#variables.city.string=San%20Francisco) |
[Seattle](#variables.city.string=Seattle)


# Daylight Table

The following table lists the selected location's monthly average daylight (in hours),
civil-twilight-begin time (in hours), and civil-twilight-end time (in hours).

~~~ data-table
dataURL: sunrise.csv

variables.city.string: Seattle

filters.0.field: City
filters.0.vin.0: city

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Month
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Average
aggregation.measures.1.field: TwilightRise
aggregation.measures.1.function: Average
aggregation.measures.2.field: TwilightSet
aggregation.measures.2.function: Average

categoryFields.0: City
categoryFields.1: MONTH(Date)
fields.0: AVERAGE(Daylight)
fields.1: AVERAGE(TwilightRise)
fields.2: AVERAGE(TwilightSet)

precision: 1
datetime: Month
~~~