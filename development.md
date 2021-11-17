[Home](#url=README.md)


# Development

To update the sunrise data for the current year:

~~~
make data
~~~

To generate data for multiple years:

~~~
make data YEAR=2021 NYEARS=3
~~~

To host locally:

~~~
python3 -m http.server
~~~

Before committing changes to the Python data generation script, sunrise.py:

~~~
make commit
~~~
