~~~ markdown-script
# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE


async function sunriseMain()
    # Render the menu
    markdownPrint('[Home](#url=README.md&var=)')
    pages = arrayNew( \
        objectNew('fn', sunriseSunrise, 'name', 'Sunrise', 'title', 'Sunrise / Sunset'), \
        objectNew('fn', sunriseDaylight, 'name', 'Daylight', 'title', 'Daylight'), \
        objectNew('fn', sunriseTable, 'name', 'Table', 'title', 'Daylight Table'), \
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
        if(!pageHidden, markdownPrint('| ' + if(isCurPage, pageName, '[' + pageName + "](#var.vPage='" + pageName + "')")))
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
    # Load the sunrise data
    data = dataParseCSV(fetch('sunrise.csv', null, true))

    # Filter to the selected city
    city = if(vCity != null, vCity, 'Seattle')
    dataCity = dataFilter(data, 'City == CITY', objectNew('CITY', city))

    # Render the city menu
    sunriseCityMenu(pageName)

    # Render the current sunrise/sunset
    today = datetimeToday()
    dataCurrent = dataFilter(dataCity, 'month(Date) == MONTH && day(Date) == DAY', \
        objectNew('MONTH', datetimeMonth(today), 'DAY', datetimeDay(today)))
    dataTable(dataCurrent, objectNew(\
        'fields', arrayNew( \
            'Date', \
            'TwilightRise', \
            'Sunrise', \
            'Sunset', \
            'TwilightSet', \
            'Daylight' \
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
            objectNew('name', 'Max Sunset', 'field', 'Sunset', 'function', 'max'), \
            objectNew('name', 'Min Daylight', 'field', 'Daylight', 'function', 'min'), \
            objectNew('name', 'Max Daylight', 'field', 'Daylight', 'function', 'max') \
        ) \
    ))
    dataTable(dataMinMax, objectNew('precision', 1))

    # Draw the sunrise/sunset line chart
    dataLineChart(dataCity, objectNew( \
        'title', 'Sunrise / Sunset - ' + city, \
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


async function sunriseDaylight()
endfunction


async function sunriseTable()
endfunction


async function sunriseComparison()
endfunction


async function sunriseRankings()
endfunction


async function sunriseQuestions()
endfunction


sunriseMain()
~~~
