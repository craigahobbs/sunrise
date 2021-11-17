# US Daylight Table

The following table ranks U.S. cities by their total annual daylight hours.

~~~ data-table
dataURL: sunrise.csv

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Year
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Daylight
aggregation.measures.1.function: Average
aggregation.measures.2.field: Daylight
aggregation.measures.2.function: Min
aggregation.measures.3.field: Daylight
aggregation.measures.3.function: Max

categoryFields.0: YEAR(Date)
categoryFields.1: City
fields.0: SUM(Daylight)
fields.1: AVERAGE(Daylight)
fields.2: MIN(Daylight)
fields.3: MAX(Daylight)

sort.0.field: YEAR(Date)
sort.1.field: SUM(Daylight)
sort.1.desc: true

precision: 1
datetime: Year
~~~


## US Cities Daylight (Monthly)

The table below ranks U.S. cities by their total monthly daylight hours.

~~~ data-table
dataURL: sunrise.csv

aggregation.categories.0.field: City
aggregation.categories.1.field: Date
aggregation.categories.1.by: Month
aggregation.measures.0.field: Daylight
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Daylight
aggregation.measures.1.function: Average
aggregation.measures.2.field: Daylight
aggregation.measures.2.function: Min
aggregation.measures.3.field: Daylight
aggregation.measures.3.function: Max

categoryFields.0: MONTH(Date)
categoryFields.1: City
fields.0: SUM(Daylight)
fields.1: AVERAGE(Daylight)
fields.2: MIN(Daylight)
fields.3: MAX(Daylight)

sort.0.field: MONTH(Date)
sort.1.field: SUM(Daylight)
sort.1.desc: true

precision: 1
datetime: Month
~~~
