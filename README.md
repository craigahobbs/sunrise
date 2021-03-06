# Sunrise Dashboard

The **Sunrise Dashboard** contains several live-rendered visualizations of the daily sunrise,
sunset, and daylight data for select U.S. cities.

[Open the Dashboard](https://craigahobbs.github.io/sunrise/#url=sunrise.md)


### About

The dashboard is composed entirely of Markdown text documents and hosted using
[markdown-up](https://github.com/craigahobbs/markdown-up#readme).
It makes extensive use of markdown-up's markdown-charts, live-rendered charts from special fenced
code blocks.

A small Python script,
[sunrise.py](https://github.com/craigahobbs/sunrise/blob/main/sunrise.py),
generates the
[sunrise, sunset, and daylight data](https://github.com/craigahobbs/sunrise/blob/main/sunrise.csv)
using the
[PyEphem](https://pypi.org/project/ephem/) package.

The dashboard source code is
[here](https://github.com/craigahobbs/sunrise).
Click here for
[development instructions](https://craigahobbs.github.io/sunrise/#url=development.md).
