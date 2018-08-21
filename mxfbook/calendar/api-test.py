import urllib3
from bs4 import BeautifulSoup
import xml.etree.ElementTree
import numpy as np
import collections
import pandas as pd

urllib3.disable_warnings()
http = urllib3.PoolManager()

# country : 70(korea), 41(china)

# year : 2018
def get_eventday(year, filter=None, isHolyday=True):

    URL = "https://www.timeanddate.com/calendar/?year=" + str(year) + "&country=41&lang=en"
    #https://www.timeanddate.com/calendar/custom.html?year=2019&country=70&lang=en&lang2=0&display=3&df=1
    r = http.request('GET', URL)
    # print(r.status)
    #
    # print(r.data)

    soup = BeautifulSoup(r.data, "html.parser")

    #mr = soup.find(id="ch1")
    mr = soup.find_all("table", {"class": "cht lpad"})

    results = []

    for tb in mr:
        table = xml.etree.ElementTree.XML(tb.__str__())
        rows = tb.find_all('tr')
        # rows = iter(table)
        # headers = [col.text for col in next(rows)]
        for row in rows:
            cols = row.find_all('td')
            d = cols[0].text
            nm = cols[1].text

            if isHolyday:
                span = cols[0].find('span')
                if span is None:
                    continue

            # get all event day
            if filter is not None:
                if filter in nm:
                    results.append([str(year) + ' ' + d, nm ])
            else:
                results.append([str(year) + ' ' + d, nm])

    return results

            #print(row)
            #print(result)
    #
    #
    # for row in rows:
    #     values = [col.text for col in row]
    #     for key, value in collections.OrderedDict(zip(headers, values)).iteritems():
    #         print key, value

    # rows = mr.find_all('tr')
    #
    # for row in rows:
    #     print(row)

def conv_to_cpp_snippet(holydays):
    # ss -> || ((d == 27 || d == 28 || d == 29) && m == September && y == 2004)
    #template_ss_date = '( d == 27 || d == 28 || d == 29)'
    template_ss = '|| ( ( d == {} || d == {} || d == {}) && m == {} && y == {})'

    pre_y = 1900

    ss = []
    d_list = []
    for h in holydays:
        s = h[0].split()

        #y = s[0]
        d = s[1]
        d_list.append(d)
        #m = s[2]

    return template_ss.format(d_list[0], d_list[1], d_list[2], s[2], s[0])


def conv_to_cpp_snippet2(year, holydays):
    _if = '''case 2018:
			if (
              (d == 21 || d == 22 || d == 23) && m == January && y == 2004 // Lunar New Year
				|| (d == 15 && m == April && y == 2004)    // National Assembly
				|| (d == 6 && m == May && y == 2014) // Harvest Moon Day
				|| ((d == 11 || d == 12 || d == 13) && m == Sep && y == 2000))
				return true;
			break;'''

    sss = []
    sss.append('case {}:'.format(year))
    sss.append('if (')
    i = 0
    for idx, h in enumerate(holydays):
        s = h[0].split()
        nm = h[1]

        y = s[0]
        d = s[1]
        m = s[2]

        if 'Seollal' in nm or 'Buddha' in nm or 'Chuseok' in nm:
            if i == 0:
                ss = '( d == {} && m == {} ) // {}'
            else:
                ss = '|| ( d == {} && m == {} ) // {}'

            sss.append(ss.format(d, m, nm))
            i += 1

    sss.append(')')
    sss.append('return true;')
    sss.append('break;')

    return '\n'.join(sss)

# for year in range(2017,2018):
#     print(conv_to_cpp_snippet(get_holyday(year, 'Chuseok')))

for year in range(2000, 2001):
    print(year, get_eventday(year))
    #print(conv_to_cpp_snippet2(year, get_eventday(year)))






