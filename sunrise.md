~~~ markdown-script
# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE

include <args.bare>
include <pager.bare>


async function sunriseMain():
    pagerModel = { \
        'pages': [ \
            {'name': 'Home', 'type': {'markdown': { \
                'url': 'README.md'}}}, \
            {'name': 'Sunrise', 'type': {'function': { \
                'function': sunriseSunrise, \
                'title': 'Sunrise / Sunset' \
            }}}, \
            {'name': 'Daylight', 'type': {'function': { \
                'function': sunriseDaylight, \
                'title': 'Daylight' \
            }}}, \
            {'name': 'Daylight Table', 'type': {'function': { \
                'function': sunriseDaylightTable, \
                'title': 'Daylight Table' \
            }}}, \
            {'name': 'Comparison', 'type': {'function': { \
                'function': sunriseComparison, \
                'title': 'Daylight Comparison' \
            }}}, \
            {'name': 'Rankings', 'type': {'function': { \
                'function': sunriseRankings, \
                'title': 'Daylight Rankings' \
            }}}, \
            {'name': 'Questions', 'type': {'function': { \
                'function': sunriseQuestions, \
                'title': 'Questions' \
            }}}, \
            {'name': 'Cities', 'hidden': true, 'type': {'function': { \
                'function': sunriseCities, \
                'title': 'Select a City' \
            }}} \
        ] \
    }
    pagerMain(pagerModel, {'arguments': sunriseArguments, 'start': 'Sunrise', 'hideNav': true, 'keyboard': true})
endfunction


# The Sunrise application arguments
sunriseArguments = argsValidate([ \
    {'name': 'page', 'default': 'Sunrise'}, \
    {'name': 'returnPage', 'explicit': true}, \
    {'name': 'city', 'default': 'Seattle'} \
])


# Chart size constants
sunriseChartWidth = 875
sunriseChartWidthWide = 1000
sunriseChartHeight = 350
sunriseChartHeightTall = 500


async function sunriseCities(args):
    # Load the sunrise data
    data = dataParseCSV(systemFetch('sunrise.csv'))

    # Aggregate by city to get the city list
    dataCities = dataAggregate(data, { \
        'categories': ['City'], \
        'measures': [ \
            {'field': 'Date', 'function': 'count'} \
        ] \
    })


    # Add the city link field
    dataCalculatedField( \
        dataCities, \
        'City', "argsLink(sunriseArguments, [City], {'page': returnPage, 'city': [City]})", \
        {'returnPage': objectGet(args, 'returnPage')} \
    )

    # Render the city link list
    dataTable(dataCities, { \
        'fields': ['City'], \
        'formats': { \
            'City': {'markdown': true} \
        } \
    })
endfunction


async function sunriseSunrise(args):
    # Load the city's sunrise data
    sunriseData = sunriseLoadData(args)
    dataCity = objectGet(sunriseData, 'dataCity')
    dataToday = objectGet(sunriseData, 'dataToday')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(args)

    # Render the current sunrise/sunset
    dataCalculatedField(dataToday, 'TwilightRise', 'sunriseTime(TwilightRise)')
    dataCalculatedField(dataToday, 'Sunrise', 'sunriseTime(Sunrise)')
    dataCalculatedField(dataToday, 'Sunset', 'sunriseTime(Sunset)')
    dataCalculatedField(dataToday, 'TwilightSet', 'sunriseTime(TwilightSet)')
    dataTable(dataToday, {\
        'fields': [ \
            'Date', \
            'TwilightRise', \
            'Sunrise', \
            'Sunset', \
            'TwilightSet' \
        ], \
        'precision': 1, \
        'datetime': 'day' \
    })

    # Render the sunrise/sunset min/max table
    dataMinMax = dataAggregate(dataCity, { \
        'measures': [ \
            {'name': 'Min Sunrise', 'field': 'Sunrise', 'function': 'min'}, \
            {'name': 'Max Sunrise', 'field': 'Sunrise', 'function': 'max'}, \
            {'name': 'Min Sunset', 'field': 'Sunset', 'function': 'min'}, \
            {'name': 'Max Sunset', 'field': 'Sunset', 'function': 'max'} \
        ] \
    })
    dataCalculatedField(dataMinMax, 'Min Sunrise', 'sunriseTime([Min Sunrise])')
    dataCalculatedField(dataMinMax, 'Max Sunrise', 'sunriseTime([Max Sunrise])')
    dataCalculatedField(dataMinMax, 'Min Sunset', 'sunriseTime([Min Sunset])')
    dataCalculatedField(dataMinMax, 'Max Sunset', 'sunriseTime([Max Sunset])')
    dataTable(dataMinMax, {\
        'fields': [ \
            'Min Sunrise', \
            'Max Sunrise', \
            'Min Sunset', \
            'Max Sunset' \
        ], \
        'precision': 1 \
    })

    # Draw the sunrise/sunset line chart
    dataLineChart(dataCity, { \
        'title': 'Sunrise / Sunset - ' + cityName, \
        'width': sunriseChartWidthWide, \
        'height': sunriseChartHeightTall, \
        'x': 'Date', \
        'y': ['Sunset', 'Sunrise'], \
        'xTicks': { \
            'count': 13, \
            'skip': 2 \
        }, \
        'yTicks': { \
            'count': 25, \
            'start': 0, \
            'end': 24, \
            'skip': 1 \
        }, \
        'xLines': [ \
            {'value': today, 'label': datetimeISOFormat(today, true)} \
        ], \
        'precision': 1, \
        'datetime': 'month' \
    })
endfunction


async function sunriseDaylight(args):
    # Load the city's sunrise data
    sunriseData = sunriseLoadData(args)
    dataCity = objectGet(sunriseData, 'dataCity')
    dataToday = objectGet(sunriseData, 'dataToday')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(args)

    # Render the current daylight
    dataTable(dataToday, {\
        'fields': [ \
            'Date', \
            'Daylight', \
            'DaylightChange' \
        ], \
        'precision': 1, \
        'datetime': 'day' \
    })

    # Render the daylight stats table
    dataStats = dataAggregate(dataCity, { \
        'measures': [ \
            {'name': 'Avg Daylight', 'field': 'Daylight', 'function': 'average'}, \
            {'name': 'Min Daylight', 'field': 'Daylight', 'function': 'min'}, \
            {'name': 'Max Daylight', 'field': 'Daylight', 'function': 'max'}, \
            {'name': 'Max Daylight Change', 'field': 'DaylightChange', 'function': 'max'} \
        ] \
    })
    dataTable(dataStats, { \
        'fields': [ \
            'Avg Daylight', \
            'Min Daylight', \
            'Max Daylight', \
            'Max Daylight Change' \
        ], \
        'precision': 1 \
    })

    # Draw the daylight line chart
    dataLineChart(dataCity, { \
        'title': 'Daylight - ' + cityName, \
        'width': sunriseChartWidth, \
        'height': sunriseChartHeight, \
        'x': 'Date', \
        'y': ['Daylight'], \
        'xTicks': { \
            'count': 13, \
            'skip': 2 \
        }, \
        'yTicks': { \
            'count': 15, \
            'start': 6, \
            'end': 20, \
            'skip': 1 \
        }, \
        'xLines': [ \
            {'value': today, 'label': datetimeISOFormat(today, true)} \
        ], \
        'precision': 1, \
        'datetime': 'month' \
    })

    # Draw the daylight change line chart
    dataLineChart(dataCity, { \
        'title': 'Daylight Change - ' + cityName, \
        'width': sunriseChartWidth, \
        'height': sunriseChartHeight, \
        'x': 'Date', \
        'y': ['DaylightChange'], \
        'xTicks': { \
            'count': 13, \
            'skip': 2 \
        }, \
        'yTicks': { \
            'count': 13, \
            'start': -6, \
            'end': 6, \
            'skip': 1 \
        }, \
        'xLines': [ \
            {'value': today, 'label': datetimeISOFormat(today, true)} \
        ], \
        'yLines': [ \
            {'value': 0, 'label': ''} \
        ], \
        'precision': 1, \
        'datetime': 'month' \
    })
endfunction


async function sunriseDaylightTable(args):
    # Load the city's sunrise data
    sunriseData = sunriseLoadData(args)
    dataCity = objectGet(sunriseData, 'dataCity')

    # Render the city menu
    sunriseCityMenu(args)

    # Render the monthly daylight average table
    dataStats = dataAggregate(dataCity, { \
        'categories': ['Month'], \
        'measures': [ \
            {'name': 'Avg Daylight', 'field': 'Daylight', 'function': 'average'}, \
            {'name': 'Avg TwilightRise', 'field': 'TwilightRise', 'function': 'average'}, \
            {'name': 'Avg TwilightSet', 'field': 'TwilightSet', 'function': 'average'} \
        ] \
    })
    dataCalculatedField(dataStats, 'Avg TwilightRise', 'sunriseTime([Avg TwilightRise])')
    dataCalculatedField(dataStats, 'Avg TwilightSet', 'sunriseTime([Avg TwilightSet])')
    dataTable(dataStats, { \
        'categories': ['Month'], \
        'fields': [ \
            'Avg Daylight', \
            'Avg TwilightRise', \
            'Avg TwilightSet' \
        ], \
        'precision': 1 \
    })
endfunction


async function sunriseComparison(args):
    # Load the city's sunrise data
    sunriseData = sunriseLoadData(args, 'Honolulu', 'Juneau')
    dataCity = objectGet(sunriseData, 'dataCity')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(args)

    # Render the daylight comparison stats table
    dataStats = dataAggregate(dataCity, { \
        'categories': ['City'], \
        'measures': [ \
            {'name': 'Avg Daylight', 'field': 'Daylight', 'function': 'average'}, \
            {'name': 'Min Daylight', 'field': 'Daylight', 'function': 'min'}, \
            {'name': 'Max Daylight', 'field': 'Daylight', 'function': 'max'}, \
            {'name': 'Max Daylight Change', 'field': 'DaylightChange', 'function': 'max'} \
        ] \
    })
    dataSort(dataStats, [['Avg Daylight', true]])
    dataTable(dataStats, { \
        'categories': ['City'], \
        'fields': [ \
            'Avg Daylight', \
            'Min Daylight', \
            'Max Daylight', \
            'Max Daylight Change' \
        ], \
        'precision': 1 \
    })

    # Draw the daylight comparison line chart
    dataLineChart(dataCity, { \
        'title': 'Daylight Comparison - ' + cityName, \
        'width': sunriseChartWidthWide, \
        'height': sunriseChartHeight, \
        'x': 'Date', \
        'y': ['Daylight'], \
        'color': 'City', \
        'xTicks': { \
            'count': 13, \
            'skip': 2 \
        }, \
        'yTicks': { \
            'count': 15, \
            'start': 6, \
            'end': 20, \
            'skip': 1 \
        }, \
        'xLines': [ \
            {'value': today, 'label': datetimeISOFormat(today, true)} \
        ], \
        'precision': 1, \
        'datetime': 'month' \
    })

    # Draw the sunrise/sunset comparison line chart
    dataLineChart(dataCity, { \
        'title': 'Sunrise/Sunset Comparison - ' + cityName, \
        'width': sunriseChartWidthWide, \
        'height': sunriseChartHeightTall, \
        'x': 'Date', \
        'y': ['Sunrise', 'Sunset'], \
        'color': 'City', \
        'xTicks': { \
            'count': 13, \
            'skip': 2 \
        }, \
        'yTicks': { \
            'count': 23, \
            'start': 2, \
            'end': 24, \
            'skip': 1 \
        }, \
        'xLines': [ \
            {'value': today, 'label': datetimeISOFormat(today, true)} \
        ], \
        'precision': 1, \
        'datetime': 'month' \
    })
endfunction


async function sunriseRankings():
    # Load the sunrise data
    data = dataParseCSV(systemFetch('sunrise.csv'))

    # Render the daylight comparison stats table
    dataStats = dataAggregate(data, { \
        'categories': ['City'], \
        'measures': [ \
            {'name': 'Avg Daylight', 'field': 'Daylight', 'function': 'average'}, \
            {'name': 'Min Daylight', 'field': 'Daylight', 'function': 'min'}, \
            {'name': 'Max Daylight', 'field': 'Daylight', 'function': 'max'}, \
            {'name': 'Max Daylight Change', 'field': 'DaylightChange', 'function': 'max'} \
        ] \
    })
    dataSort(dataStats, [['Avg Daylight', true]])
    dataTable(dataStats, { \
        'categories': ['City'], \
        'fields': [ \
            'Avg Daylight', \
            'Min Daylight', \
            'Max Daylight', \
            'Max Daylight Change' \
        ], \
        'precision': 1 \
    })
endfunction


async function sunriseQuestions(args):
    # Load the city's sunrise data
    otherName = 'Juneau'
    sunriseData = sunriseLoadData(args, otherName)
    dataCity = objectGet(sunriseData, 'dataCity')
    cityName = objectGet(sunriseData, 'cityName')

    # Render the city menu
    sunriseCityMenu(args)

    # Compute this city's longest and shortest days
    dataMinMax = dataAggregate( \
        dataFilter(dataCity, 'City == cityName', {'cityName': cityName}), \
        { \
            'categories': ['Year'], \
            'measures': [ \
                {'name': 'DaylightMax', 'field': 'Daylight', 'function': 'max'}, \
                {'name': 'DaylightMin', 'field': 'Daylight', 'function': 'min'} \
            ] \
        } \
    )
    dataSort(dataMinMax, [['Year', true]])
    daylightYear = objectGet(arrayGet(dataMinMax, 0), 'Year')
    daylightMax = objectGet(arrayGet(dataMinMax, 0), 'DaylightMax')
    daylightMin = objectGet(arrayGet(dataMinMax, 0), 'DaylightMin')

    # How many days longer than this city's longest day?
    daysLonger = arrayLength(dataFilter(dataCity, 'City == otherName && Year == daylightYear && Daylight > daylightMax', \
        {'otherName': otherName, 'daylightYear': daylightYear, 'daylightMax': daylightMax}))
    markdownPrint( \
        '', '**Question:** The longest day in ' + cityName + ' is ' + numberToFixed(daylightMax, 1, true) + ' hours.', \
        'How many days in ' + otherName + ' are at least that long?  ', \
        '**Answer**: ' + daysLonger + ' days' \
    )

    # How many days shorter than this city's shortest day?
    daysShorter = arrayLength(dataFilter(dataCity, 'City == otherName && Year == daylightYear && Daylight < daylightMin', \
        {'otherName': otherName, 'daylightYear': daylightYear, 'daylightMin': daylightMin}))
    markdownPrint( \
        '', '**Question:** The shortest day in ' + cityName + ' is ' + numberToFixed(daylightMin, 1, true) + ' hours.', \
        'How many days in ' + otherName + ' are at least that short?  ', \
        '**Answer**: ' + daysShorter + ' days' \
    )
endfunction


function sunriseCityMenu(args):
    markdownPrint( \
        '', '**Location:** ' + markdownEscape(objectGet(args, 'city')), \
        '(' + argsLink(sunriseArguments, 'Change', {'page': 'Cities', 'returnPage': objectGet(args, 'page')}) + ')' \
    )
endfunction


async function sunriseLoadData(args, cityName2, cityName3):
    # Load the sunrise data
    data = dataParseCSV(systemFetch('sunrise.csv'))

    # Filter to the selected city
    cityName = objectGet(args, 'city')
    dataCity = dataFilter(data, 'City == CITY || City == CITY2 || City == CITY3', \
        {'CITY': cityName, 'CITY2': cityName2, 'CITY3': cityName3})

    # Add calculated fields
    dataCalculatedField(dataCity, 'Year', 'year(Date)')
    dataCalculatedField(dataCity, 'Month', 'month(Date)')

    # Filter to today
    today = datetimeToday()
    dataToday = dataFilter(dataCity, 'Month == MONTH && day(Date) == DAY', \
        {'MONTH': datetimeMonth(today), 'DAY': datetimeDay(today)})
    dataSort(dataToday, [['Year', true]])
    dataToday = [objectCopy(arrayGet(dataToday, 0))]

    # Compute a today within the data bounds
    dataYearMinMax = dataAggregate(dataCity, { \
        'measures': [ \
            {'name': 'YearMax', 'field': 'Year', 'function': 'max'}, \
            {'name': 'YearMin', 'field': 'Year', 'function': 'min'} \
        ] \
    })
    yearMax = objectGet(arrayGet(dataYearMinMax, 0), 'YearMax')
    yearMin = objectGet(arrayGet(dataYearMinMax, 0), 'YearMin')
    year = datetimeYear(today)
    today = if(year >= yearMin && year <= yearMax, today, datetimeNew(yearMax, datetimeMonth(today), datetimeDay(today)))

    return { \
        'dataCity': dataCity, \
        'dataToday': dataToday, \
        'cityName': cityName, \
        'today': today \
    }
endfunction


function sunriseTime(time):
    hour = mathFloor(time)
    minuteRatio = time - hour
    minute = mathFloor(minuteRatio * 60)
    return if(hour < 12, hour, hour - 12) + ':' + if(minute < 10, '0', '') + minute + if(hour < 12, ' am', ' pm')
endfunction


sunriseMain()
~~~
