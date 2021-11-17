# Sunrise Dashboard

The **Sunrise Dashboard** contains several live-rendered visualizations of the daily sunrise,
sunset, and daylight data for select U.S. cities.

[Open the Dashboard](#url=sunrise.md)


### About

The dashboard source code is
[here](https://github.com/craigahobbs/sunrise#readme).
The dashboard is composed entirely of Markdown text documents and hosted using
[markdown-up](https://github.com/craigahobbs/markdown-up#readme).
It makes extensive use of markdown-up's markdown-charts, live-rendered charts specified using
special fenced code blocks.

A small Python script,
[sunrise.py](https://github.com/craigahobbs/sunrise/blob/main/sunrise.py),
generates the
[sunrise, sunset, and daylight data](https://github.com/craigahobbs/sunrise/blob/main/sunrise.csv)
using the
[PyEphem](https://pypi.org/project/ephem/) package.


### Development

To update the sunrise data for the current year:

~~~
make data
~~~

Before committing changes to the Python data generation script, sunrise.py:

~~~
make commit
~~~
