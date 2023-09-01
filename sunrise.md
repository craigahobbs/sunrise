~~~ markdown-script
# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE


async function sunriseMain()
    # Render the menu
    markdownPrint('[Home](#url=README.md&var=)')
    for page, ixPage in arrayNew( \
        objectNew('fn', sunriseSunrise, 'name', 'Sunrise', 'title', 'Sunrise / Sunset'), \
        objectNew('fn', sunriseDaylight, 'name', 'Daylight', 'title', 'Daylight'), \
        objectNew('fn', sunriseDaylightTable, 'name', 'Daylight Table', 'title', 'Daylight Table'), \
        objectNew('fn', sunriseComparison, 'name', 'Comparison', 'title', 'Daylight Comparison'), \
        objectNew('fn', sunriseRankings, 'name', 'Rankings', 'title', 'Daylight Rankings'), \
        objectNew('fn', sunriseQuestions, 'name', 'Questions', 'title', 'Questions'), \
        objectNew('fn', sunriseCities, 'name', 'Cities', 'title', 'Select a City', 'hidden', true) \
    ):
        pageName = objectGet(page, 'name')
        pageHidden = objectGet(page, 'hidden')
        pageURL = "#var.vPage='" + urlEncodeComponent(pageName) + "'" + \
            if(vCity != null, "&var.vCity='" + urlEncodeComponent(vCity) + "'", '')
        if vPage == pageName || (vPage == null && ixPage == 0):
            curPage = page
            if !pageHidden:
                markdownPrint('| ' + markdownEscape(pageName))
            endif
        else:
            if !pageHidden:
                markdownPrint('| [' + markdownEscape(pageName) + '](' + pageURL + ')')
            endif
        endif
    endfor

    # Set the title
    curPageTitle = objectGet(curPage, 'title')
    markdownPrint('', '# ' + curPageTitle, '')
    documentSetTitle(curPageTitle)

    # Render the page
    curPageFn = objectGet(curPage, 'fn')
    curPageFn(objectGet(curPage, 'name'))
endfunction


# Chart size constants
sunriseChartWidth = 875
sunriseChartWidthWide = 1000
sunriseChartHeight = 350
sunriseChartHeightTall = 500


async function sunriseCities()
    # Load the sunrise data
    data = dataParseCSV(systemFetch('sunrise.csv', null, true))

    # Aggregate by city to get the city list
    dataCities = dataAggregate(data, objectNew( \
        'categories', arrayNew('City'), \
        'measures', arrayNew( \
            objectNew('field', 'Date', 'function', 'count') \
        ) \
    ))

    # Add the city link field
    pagePart = if(vReturnPage == null, '#', '#var.vPage=\'' + urlEncodeComponent(vReturnPage) + '\'&')
    dataCalculatedField( \
        dataCities, \
        'City', "'[' + City + '](' + pagePart + 'var.vCity=\'' + urlEncodeComponent(City) + '\')'", \
        objectNew('pagePart', pagePart) \
    )

    # Render the city link list
    dataTable(dataCities, objectNew( \
        'fields', arrayNew('City'), \
        'markdown', arrayNew('City') \
    ))
endfunction


async function sunriseSunrise(pageName)
    # Load the city's sunrise data
    sunriseData = sunriseLoadData()
    dataCity = objectGet(sunriseData, 'dataCity')
    dataToday = objectGet(sunriseData, 'dataToday')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(pageName, cityName)

    # Render the current sunrise/sunset
    dataCalculatedField(dataToday, 'TwilightRise', 'sunriseTime(TwilightRise)', sunriseTimeFunctions)
    dataCalculatedField(dataToday, 'Sunrise', 'sunriseTime(Sunrise)', sunriseTimeFunctions)
    dataCalculatedField(dataToday, 'Sunset', 'sunriseTime(Sunset)', sunriseTimeFunctions)
    dataCalculatedField(dataToday, 'TwilightSet', 'sunriseTime(TwilightSet)', sunriseTimeFunctions)
    dataTable(dataToday, objectNew(\
        'fields', arrayNew( \
            'Date', \
            'TwilightRise', \
            'Sunrise', \
            'Sunset', \
            'TwilightSet' \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))

    # Render the sunrise/sunset min/max table
    dataMinMax = dataAggregate(dataCity, objectNew( \
        'measures', arrayNew( \
            objectNew('name', 'Min Sunrise', 'field', 'Sunrise', 'function', 'min'), \
            objectNew('name', 'Max Sunrise', 'field', 'Sunrise', 'function', 'max'), \
            objectNew('name', 'Min Sunset', 'field', 'Sunset', 'function', 'min'), \
            objectNew('name', 'Max Sunset', 'field', 'Sunset', 'function', 'max') \
        ) \
    ))
    dataCalculatedField(dataMinMax, 'Min Sunrise', 'sunriseTime([Min Sunrise])', sunriseTimeFunctions)
    dataCalculatedField(dataMinMax, 'Max Sunrise', 'sunriseTime([Max Sunrise])', sunriseTimeFunctions)
    dataCalculatedField(dataMinMax, 'Min Sunset', 'sunriseTime([Min Sunset])', sunriseTimeFunctions)
    dataCalculatedField(dataMinMax, 'Max Sunset', 'sunriseTime([Max Sunset])', sunriseTimeFunctions)
    dataTable(dataMinMax, objectNew(\
        'fields', arrayNew( \
            'Min Sunrise', \
            'Max Sunrise', \
            'Min Sunset', \
            'Max Sunset' \
        ), \
        'precision', 1 \
    ))

    # Draw the sunrise/sunset line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Sunrise / Sunset - ' + cityName, \
        'width', sunriseChartWidthWide, \
        'height', sunriseChartHeightTall, \
        'x', 'Date', \
        'y', arrayNew('Sunset', 'Sunrise'), \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 25, \
            'start', 0, \
            'end', 24, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today, 'label', datetimeISOFormat(today, true)) \
        ), \
        'precision', 1, \
        'datetime', 'month' \
    ))
endfunction


async function sunriseDaylight(pageName)
    # Load the city's sunrise data
    sunriseData = sunriseLoadData()
    dataCity = objectGet(sunriseData, 'dataCity')
    dataToday = objectGet(sunriseData, 'dataToday')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(pageName, cityName)

    # Render the current daylight
    dataTable(dataToday, objectNew(\
        'fields', arrayNew( \
            'Date', \
            'Daylight', \
            'DaylightChange' \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))

    # Render the daylight stats table
    dataStats = dataAggregate(dataCity, objectNew( \
        'measures', arrayNew( \
            objectNew('name', 'Avg Daylight', 'field', 'Daylight', 'function', 'average'), \
            objectNew('name', 'Min Daylight', 'field', 'Daylight', 'function', 'min'), \
            objectNew('name', 'Max Daylight', 'field', 'Daylight', 'function', 'max'), \
            objectNew('name', 'Max Daylight Change', 'field', 'DaylightChange', 'function', 'max') \
        ) \
    ))
    dataTable(dataStats, objectNew( \
        'fields', arrayNew( \
            'Avg Daylight', \
            'Min Daylight', \
            'Max Daylight', \
            'Max Daylight Change' \
        ), \
        'precision', 1 \
    ))

    # Draw the daylight line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Daylight - ' + cityName, \
        'width', sunriseChartWidth, \
        'height', sunriseChartHeight, \
        'x', 'Date', \
        'y', arrayNew('Daylight'), \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 15, \
            'start', 6, \
            'end', 20, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today, 'label', datetimeISOFormat(today, true)) \
        ), \
        'precision', 1, \
        'datetime', 'month' \
    ))

    # Draw the daylight change line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Daylight Change - ' + cityName, \
        'width', sunriseChartWidth, \
        'height', sunriseChartHeight, \
        'x', 'Date', \
        'y', arrayNew('DaylightChange'), \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 13, \
            'start', -6, \
            'end', 6, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today, 'label', datetimeISOFormat(today, true)) \
        ), \
        'yLines', arrayNew( \
            objectNew('value', 0, 'label', '') \
        ), \
        'precision', 1, \
        'datetime', 'month' \
    ))
endfunction


async function sunriseDaylightTable(pageName)
    # Load the city's sunrise data
    sunriseData = sunriseLoadData()
    dataCity = objectGet(sunriseData, 'dataCity')
    cityName = objectGet(sunriseData, 'cityName')

    # Render the city menu
    sunriseCityMenu(pageName, cityName)

    # Render the monthly daylight average table
    dataStats = dataAggregate(dataCity, objectNew( \
        'categories', arrayNew('Month'), \
        'measures', arrayNew( \
            objectNew('name', 'Avg Daylight', 'field', 'Daylight', 'function', 'average'), \
            objectNew('name', 'Avg TwilightRise', 'field', 'TwilightRise', 'function', 'average'), \
            objectNew('name', 'Avg TwilightSet', 'field', 'TwilightSet', 'function', 'average') \
        ) \
    ))
    dataCalculatedField(dataStats, 'Avg TwilightRise', 'sunriseTime([Avg TwilightRise])', sunriseTimeFunctions)
    dataCalculatedField(dataStats, 'Avg TwilightSet', 'sunriseTime([Avg TwilightSet])', sunriseTimeFunctions)
    dataTable(dataStats, objectNew( \
        'categories', arrayNew('Month'), \
        'fields', arrayNew( \
            'Avg Daylight', \
            'Avg TwilightRise', \
            'Avg TwilightSet' \
        ), \
        'precision', 1 \
    ))
endfunction


async function sunriseComparison(pageName)
    # Load the city's sunrise data
    sunriseData = sunriseLoadData('Honolulu', 'Juneau')
    dataCity = objectGet(sunriseData, 'dataCity')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(pageName, cityName)

    # Render the daylight comparison stats table
    dataStats = dataAggregate(dataCity, objectNew( \
        'categories', arrayNew('City'), \
        'measures', arrayNew( \
            objectNew('name', 'Avg Daylight', 'field', 'Daylight', 'function', 'average'), \
            objectNew('name', 'Min Daylight', 'field', 'Daylight', 'function', 'min'), \
            objectNew('name', 'Max Daylight', 'field', 'Daylight', 'function', 'max'), \
            objectNew('name', 'Max Daylight Change', 'field', 'DaylightChange', 'function', 'max') \
        ) \
    ))
    dataSort(dataStats, arrayNew(arrayNew('Avg Daylight', true)))
    dataTable(dataStats, objectNew( \
        'categories', arrayNew('City'), \
        'fields', arrayNew( \
            'Avg Daylight', \
            'Min Daylight', \
            'Max Daylight', \
            'Max Daylight Change' \
        ), \
        'precision', 1 \
    ))

    # Draw the daylight comparison line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Daylight Comparison - ' + cityName, \
        'width', sunriseChartWidthWide, \
        'height', sunriseChartHeight, \
        'x', 'Date', \
        'y', arrayNew('Daylight'), \
        'color', 'City', \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 15, \
            'start', 6, \
            'end', 20, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today, 'label', datetimeISOFormat(today, true)) \
        ), \
        'precision', 1, \
        'datetime', 'month' \
    ))

    # Draw the sunrise/sunset comparison line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Sunrise/Sunset Comparison - ' + cityName, \
        'width', sunriseChartWidthWide, \
        'height', sunriseChartHeightTall, \
        'x', 'Date', \
        'y', arrayNew('Sunrise', 'Sunset'), \
        'color', 'City', \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 23, \
            'start', 2, \
            'end', 24, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today, 'label', datetimeISOFormat(today, true)) \
        ), \
        'precision', 1, \
        'datetime', 'month' \
    ))
endfunction


async function sunriseRankings()
    # Load the sunrise data
    data = dataParseCSV(systemFetch('sunrise.csv', null, true))

    # Render the daylight comparison stats table
    dataStats = dataAggregate(data, objectNew( \
        'categories', arrayNew('City'), \
        'measures', arrayNew( \
            objectNew('name', 'Avg Daylight', 'field', 'Daylight', 'function', 'average'), \
            objectNew('name', 'Min Daylight', 'field', 'Daylight', 'function', 'min'), \
            objectNew('name', 'Max Daylight', 'field', 'Daylight', 'function', 'max'), \
            objectNew('name', 'Max Daylight Change', 'field', 'DaylightChange', 'function', 'max') \
        ) \
    ))
    dataSort(dataStats, arrayNew(arrayNew('Avg Daylight', true)))
    dataTable(dataStats, objectNew( \
        'categories', arrayNew('City'), \
        'fields', arrayNew( \
            'Avg Daylight', \
            'Min Daylight', \
            'Max Daylight', \
            'Max Daylight Change' \
        ), \
        'precision', 1 \
    ))
endfunction


async function sunriseQuestions(pageName)
    # Load the city's sunrise data
    otherName = 'Juneau'
    sunriseData = sunriseLoadData(otherName)
    dataCity = objectGet(sunriseData, 'dataCity')
    cityName = objectGet(sunriseData, 'cityName')

    # Render the city menu
    sunriseCityMenu(pageName, cityName)

    # Compute this city's longest and shortest days
    dataMinMax = dataAggregate( \
        dataFilter(dataCity, 'City == cityName', objectNew('cityName', cityName)), \
        objectNew( \
            'categories', arrayNew('Year'), \
            'measures', arrayNew( \
                objectNew('name', 'DaylightMax', 'field', 'Daylight', 'function', 'max'), \
                objectNew('name', 'DaylightMin', 'field', 'Daylight', 'function', 'min') \
            ) \
        ) \
    )
    dataSort(dataMinMax, arrayNew(arrayNew('Year', true)))
    daylightYear = objectGet(arrayGet(dataMinMax, 0), 'Year')
    daylightMax = objectGet(arrayGet(dataMinMax, 0), 'DaylightMax')
    daylightMin = objectGet(arrayGet(dataMinMax, 0), 'DaylightMin')

    # How many days longer than this city's longest day?
    daysLonger = arrayLength(dataFilter(dataCity, 'City == otherName && Year == daylightYear && Daylight > daylightMax', \
        objectNew('otherName', otherName, 'daylightYear', daylightYear, 'daylightMax', daylightMax)))
    markdownPrint( \
        '', '**Question:** The longest day in ' + cityName + ' is ' + numberToFixed(daylightMax, 1, true) + ' hours.', \
        'How many days in ' + otherName + ' are at least that long?  ', \
        '**Answer**: ' + daysLonger + ' days' \
    )

    # How many days shorter than this city's shortest day?
    daysShorter = arrayLength(dataFilter(dataCity, 'City == otherName && Year == daylightYear && Daylight < daylightMin', \
        objectNew('otherName', otherName, 'daylightYear', daylightYear, 'daylightMin', daylightMin)))
    markdownPrint( \
        '', '**Question:** The shortest day in ' + cityName + ' is ' + numberToFixed(daylightMin, 1, true) + ' hours.', \
        'How many days in ' + otherName + ' are at least that short?  ', \
        '**Answer**: ' + daysShorter + ' days' \
    )
endfunction


function sunriseCityMenu(pageName, cityName)
    markdownPrint( \
        '', '**Location:** ' + cityName, \
        "([Change](#var.vPage='Cities'&var.vReturnPage='" + urlEncodeComponent(pageName) + "'))" \
    )
endfunction


async function sunriseLoadData(cityName2, cityName3)
    # Load the sunrise data
    data = dataParseCSV(systemFetch('sunrise.csv', null, true))

    # Filter to the selected city
    cityName = if(vCity != null, vCity, 'Seattle')
    dataCity = dataFilter(data, 'City == CITY || City == CITY2 || City == CITY3', \
        objectNew('CITY', cityName, 'CITY2', cityName2, 'CITY3', cityName3))

    # Add calculated fields
    dataCalculatedField(dataCity, 'Year', 'year(Date)')
    dataCalculatedField(dataCity, 'Month', 'month(Date)')

    # Filter to today
    today = datetimeToday()
    dataToday = dataFilter(dataCity, 'Month == MONTH && day(Date) == DAY', \
        objectNew('MONTH', datetimeMonth(today), 'DAY', datetimeDay(today)))
    dataSort(dataToday, arrayNew(arrayNew('Year', true)))
    dataToday = arrayNew(objectCopy(arrayGet(dataToday, 0)))

    # Compute a today within the data bounds
    dataYearMinMax = dataAggregate(dataCity, objectNew( \
        'measures', arrayNew( \
            objectNew('name', 'YearMax', 'field', 'Year', 'function', 'max'), \
            objectNew('name', 'YearMin', 'field', 'Year', 'function', 'min') \
        ) \
    ))
    yearMax = objectGet(arrayGet(dataYearMinMax, 0), 'YearMax')
    yearMin = objectGet(arrayGet(dataYearMinMax, 0), 'YearMin')
    year = datetimeYear(today)
    today = if(year >= yearMin && year <= yearMax, today, datetimeNew(yearMax, datetimeMonth(today), datetimeDay(today)))

    return objectNew( \
        'dataCity', dataCity, \
        'dataToday', dataToday, \
        'cityName', cityName, \
        'today', today \
    )
endfunction


function sunriseTime(time)
    hour = mathFloor(time, 0)
    minuteRatio = time - hour
    minute = mathFloor(minuteRatio * 60, 0)
    return if(hour < 12, hour, hour - 12) + ':' + if(minute < 10, '0', '') + minute + if(hour < 12, ' am', ' pm')
endfunction


sunriseTimeFunctions = objectNew('sunriseTime', sunriseTime, 'mathFloor', mathFloor)


sunriseMain()
~~~
