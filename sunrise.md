~~~ markdown-script
# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE


async function sunriseMain()
    # Render the menu
    markdownPrint('[Home](#url=README.md&var=)')
    pages = arrayNew( \
        objectNew('fn', sunriseSunrise, 'name', 'Sunrise', 'title', 'Sunrise / Sunset'), \
        objectNew('fn', sunriseDaylight, 'name', 'Daylight', 'title', 'Daylight'), \
        objectNew('fn', sunriseDaylightTable, 'name', 'Daylight Table', 'title', 'Daylight Table'), \
        objectNew('fn', sunriseComparison, 'name', 'Comparison', 'title', 'Daylight Comparison'), \
        objectNew('fn', sunriseRankings, 'name', 'Rankings', 'title', 'Daylight Rankings'), \
        objectNew('fn', sunriseQuestions, 'name', 'Questions', 'title', 'Questions'), \
        objectNew('fn', sunriseCities, 'name', 'Cities', 'title', 'Select a City', 'hidden', true) \
    )
    ixPage = 0
    curPage = null
    pageLoop:
        page = arrayGet(pages, ixPage)
        pageName = objectGet(page, 'name')
        pageHidden = objectGet(page, 'hidden')
        isCurPage = (vPage == null && ixPage == 0) || vPage == pageName
        curPage = if(isCurPage, page, curPage)
        pageURL = "#var.vPage='" + encodeURIComponent(pageName) + "'" + \
            if(vCity != null, "&var.vCity='" + encodeURIComponent(vCity) + "'", '')
        if(!pageHidden, markdownPrint('| ' + if(isCurPage, pageName, '[' + pageName + '](' + pageURL + ')')))
        ixPage = ixPage + 1
    jumpif (ixPage < arrayLength(pages)) pageLoop

    # Set the title
    curPageTitle = objectGet(curPage, 'title')
    markdownPrint('', '# ' + curPageTitle, '')
    setDocumentTitle(curPageTitle)

    # Render the page
    curPageFn = objectGet(curPage, 'fn')
    curPageFn(objectGet(curPage, 'name'))
endfunction


function sunriseCityMenu(pageName)
    markdownPrint( \
        '**Location:** ' + if(vCity != null, vCity, 'Seattle'), \
        "([Change](#var.vPage='Cities'&var.vReturnPage='" + encodeURIComponent(pageName) + "'))", \
        '' \
    )
endfunction


async function sunriseCities()
    # Load the sunrise data
    data = dataParseCSV(fetch('sunrise.csv', null, true))

    # Aggregate by city to get the city list
    dataCities = dataAggregate(data, objectNew( \
        'categories', arrayNew('City'), \
        'measures', arrayNew( \
            objectNew('field', 'Date', 'function', 'count') \
        ) \
    ))

    # Add the city link field
    pagePart = if(vReturnPage == null, '#', '#var.vPage=\'' + encodeURIComponent(vReturnPage) + '\'&')
    dataCalculatedField( \
        dataCities, \
        'City', "'[' + City + '](' + pagePart + 'var.vCity=\'' + encodeURIComponent(City) + '\')'", \
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
    sunriseCityMenu(pageName)

    # Render the current sunrise/sunset
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
    dataTable(dataMinMax, objectNew('precision', 1))

    # Draw the sunrise/sunset line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Sunrise / Sunset - ' + cityName, \
        'width', 1000, \
        'height', 500, \
        'x', 'Date', \
        'y', arrayNew('Sunset', 'Sunrise'), \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 23, \
            'start', 0, \
            'end', 24, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today) \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))
endfunction


async function sunriseDaylight(pageName)
    # Load the city's sunrise data
    sunriseData = sunriseLoadData()
    dataCity = objectGet(sunriseData, 'dataCity')
    cityName = objectGet(sunriseData, 'cityName')
    today = objectGet(sunriseData, 'today')

    # Render the city menu
    sunriseCityMenu(pageName)

    # Render the current daylight
    dataTable(dataCurrent, objectNew(\
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
        'width', 875, \
        'height', 350, \
        'x', 'Date', \
        'y', arrayNew('Daylight'), \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 15, \
            'start', 8, \
            'end', 22, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today) \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))

    # Draw the daylight change line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Daylight Change - ' + cityName, \
        'width', 875, \
        'height', 350, \
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
            objectNew('value', today) \
        ), \
        'yLines', arrayNew( \
            objectNew('value', 0, 'label', '') \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))
endfunction


async function sunriseDaylightTable(pageName)
    # Load the city's sunrise data
    sunriseData = sunriseLoadData()
    dataCity = objectGet(sunriseData, 'dataCity')

    # Render the city menu
    sunriseCityMenu(pageName)

    # Render the monthly daylight average table
    dataStats = dataAggregate(dataCity, objectNew( \
        'categories', arrayNew('Month'), \
        'measures', arrayNew( \
            objectNew('name', 'Avg Daylight', 'field', 'Daylight', 'function', 'average'), \
            objectNew('name', 'Avg TwilightRise', 'field', 'TwilightRise', 'function', 'average'), \
            objectNew('name', 'Avg TwilightSet', 'field', 'TwilightSet', 'function', 'average') \
        ) \
    ))
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
    sunriseCityMenu(pageName)

    # Render the comparison stats table
    dataStats = dataAggregate(dataCity, objectNew( \
        'categories', arrayNew('City'), \
        'measures', arrayNew( \
            objectNew('name', 'Total Daylight', 'field', 'Daylight', 'function', 'sum'), \
            objectNew('name', 'Avg Daylight', 'field', 'Daylight', 'function', 'average'), \
            objectNew('name', 'Min Daylight', 'field', 'Daylight', 'function', 'min'), \
            objectNew('name', 'Max Daylight', 'field', 'Daylight', 'function', 'max'), \
            objectNew('name', 'Max Daylight Change', 'field', 'DaylightChange', 'function', 'max') \
        ) \
    ))
    dataSort(dataStats, arrayNew(arrayNew('Total Daylight', true)))
    dataTable(dataStats, objectNew( \
        'categories', arrayNew('City'), \
        'fields', arrayNew( \
            'Total Daylight', \
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
        'width', 1000, \
        'height', 350, \
        'x', 'Date', \
        'y', arrayNew('Daylight'), \
        'color', 'City', \
        'xTicks', objectNew( \
            'count', 13, \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'count', 15, \
            'start', 8, \
            'end', 22, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', today) \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))

    # Draw the sunrise/sunset comparison line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Sunrise/Sunset Comparison - ' + cityName, \
        'width', 1000, \
        'height', 500, \
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
            objectNew('value', today) \
        ), \
        'precision', 1, \
        'datetime', 'day' \
    ))
endfunction


async function sunriseRankings()
endfunction


async function sunriseQuestions()
endfunction


async function sunriseLoadData(cityName2, cityName3)
    # Load the sunrise data
    data = dataParseCSV(fetch('sunrise.csv', null, true))

    # Filter to the selected city
    cityName = if(vCity != null, vCity, 'Seattle')
    dataCity = dataFilter(data, 'City == CITY || City == CITY2 || City == CITY3', \
        objectNew('CITY', cityName, 'CITY2', cityName2, 'CITY3', cityName3))

    # Add calculated fields
    dataCalculatedField(dataCity, 'Month', 'month(Date)')

    # Filter to today
    today = datetimeToday()
    dataToday = dataFilter(dataCity, 'Month == MONTH && day(Date) == DAY', \
        objectNew('MONTH', datetimeMonth(today), 'DAY', datetimeDay(today)))

    return objectNew( \
        'dataCity', dataCity, \
        'dataToday', dataToday, \
        'cityName', cityName, \
        'today', objectGet(arrayGet(dataToday, 0), 'Date') \
    )
endfunction


sunriseMain()
~~~
