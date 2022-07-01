# Select a City

~~~ data-table
data.url: sunrise.csv

var.vURL: 'sunrise.md'

agg.category.0: City
agg.measure.0.name: Cities
agg.measure.0.field: City
agg.measure.0.func: Count

sort.0.field: City

aggcalc.0.name: City
aggcalc.0.expr: '[' + City + '](#url=' + encodeURL(vURL) + '&var.vCity=' + encodeURL("'" + City + "'") + ')'

field.0: City

markdown.0: City
~~~
