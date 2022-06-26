import re

from bs4 import BeautifulSoup

from tools.text_mining import select_rows, get_year_list


def get_columns(value: int):
    if value == 1:
        return ['No', 'Name', 'scholar URL', 'Reference(Oldest)', 'Reference(Newest)', 'Cited Total Num',
                'Search Count Num']
    if value == 2:
        return ['No', 'Name', 'Url', 'Domain', 'Kingdom', 'Phylum', 'Subphylum', 'Class',
                'Distribution Table - Continent/Country/Region', 'Habitat List - Category',
                'Habitat List - Sub-Category',
                'Habitat List - Habitat', 'Habitat List - Presence',
                'Host Plants and Other Plants Affected - Plant name',
                'Host Plants and Other Plants Affected - Family', 'Host Plants and Other Plants Affected - Context',
                'Growth Stages', 'List of Symptoms/Signs - Sign', 'References(Total num)', 'References(USDA num)',
                'References(Oldest)', 'References(Newest)', 'Distribution References', 'Pathway Causes - Cause',
                'Pathway Vectors - Vector', 'Impact Summary - Category']

    return []


def www_cabi_org(no: int, html: str):
    result = []
    soup = BeautifulSoup(html, 'html.parser')

    # No
    # TODO: ID 만들기
    result.append('TODO MAKE NO')

    # Name
    name = soup.select_one('body > div > div > div > div > div > h3')
    result.append(name.text.strip())

    # Url
    # TODO: URL 만들기
    result.append('TODO MAKE URL')

    # Taxonomic Tree
    taxonomic_tree = soup.select('body > div > div > div > div > div > div > div > div > ul > li')
    data_set = ['', '', '', '', '']
    if 'Taxonomic Tree' in html:
        for i in taxonomic_tree:
            keyword = i.text.strip()
            if ':' in keyword:
                key = keyword.split(':')[0].strip()
                value = keyword.split(':')[1].strip()

                if 'Domain' in key:
                    data_set[0] = value

                if 'Kingdom' in key:
                    data_set[1] = value

                if 'Phylum' in key:
                    data_set[2] = value

                if 'Subphylum' in key:
                    data_set[3] = value

                if 'Class' in key:
                    data_set[4] = value

        for x in enumerate(data_set):
            if '' == x[1]:
                data_set[x[0]] = 'N/A'
        result += data_set

    else:
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')

    # Distribute Table
    if 'Distribution Table' in html:
        dt = soup.select('#todistributionDatabaseTable > div > div > div > table > tbody > tr > td > a')
        result.append(select_rows(input_list=dt, no_x=8, no_y=1))
    else:
        result.append('N/A')

    # Habitat List
    if 'Habitat List' in html:
        qs = soup.select('#toenvironments > div > table > tbody > tr > td')
        result.append(select_rows(input_list=qs, no_x=5, no_y=1))
        result.append(select_rows(input_list=qs, no_x=5, no_y=2))
        result.append(select_rows(input_list=qs, no_x=5, no_y=3))
        result.append(select_rows(input_list=qs, no_x=5, no_y=4))

    else:
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')

    # Host Plants and Other Plants Affected
    if 'Host Plants and Other Plants Affected' in html:
        hpopa_list = soup.select('#tohostPlants > div > div > table > tbody > tr > td')
        result.append(select_rows(input_list=hpopa_list, no_y=1, no_x=4))
        result.append(select_rows(input_list=hpopa_list, no_y=2, no_x=4))
        result.append(select_rows(input_list=hpopa_list, no_y=3, no_x=4))

    else:
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')

    # Growth Stages
    if 'Growth Stages' in html:
        result.append(soup.select_one('#togrowthStages > div').text.strip())
    else:
        result.append('N/A')

    # List of Symptoms/Signs
    if 'List of Symptoms/Signs' in html:
        lss = soup.select('#tosymptomsOrSigns > div > div > table > tbody > tr > td')
        result.append(select_rows(input_list=lss, no_x=3, no_y=1))
    else:
        result.append('N/A')

    # References(Total num)
    if 'References' in html:
        qs = soup.select('#toreferences > div > p')
        result.append(len(qs))
    else:
        result.append('N/A')

    # References(USDA num Kyeaword Search)
    if 'References' in html:
        qs = soup.select('#toreferences > div > p > a')
        search_text = 'Department of Agriculture'
        count_num = 0
        for i in qs:
            if search_text in i.text.strip():
                count_num += 1
        result.append(count_num)
    else:
        result.append('N/A')

    # References(Old New)
    if 'References' in html:
        input_list = []
        texts = soup.select('#toreferences > div > p')
        for i in texts:
            input_list.append(i.text.strip())
        year = get_year_list(input_list)

        result.append(min(year))
        result.append(max(year))

    else:
        result.append('N/A')
        result.append('N/A')

    # Distribution References(num)
    if 'Distribution References' in html:
        qs = soup.select('#toreferences > div > div > p')
        result.append(len(qs))

    else:
        result.append('N/A')

    # Pathway Causes - Cause
    if 'Pathway Causes' in html:
        qs = soup.select('#topathwayCauses > div > div > table > tbody > tr > td > a')
        result.append(select_rows(input_list=qs, no_x=5, no_y=1))

    else:
        result.append('N/A')

    # Pathway Vectors - Vector
    if 'Pathway Vectors' in html:
        qs = soup.select('#topathwayVectors > div > div > table > tbody > tr > td')
        result.append(select_rows(input_list=qs, no_y=1, no_x=5))
    else:
        result.append('N/A')

    # Impact Summary - Category
    if 'Impact Summary' in html:
        impact_summary = soup.select('#toimpactSummary > div > div > table > tbody > tr > td')
        result.append(select_rows(input_list=impact_summary, no_x=2, no_y=1))

    else:
        result.append('N/A')

    return result


def scholar_google_com(no: int, html: str):
    """
    template_scholar_google_com
    :param no:
    :param html:
    :return:
    """
    result = []
    soup = BeautifulSoup(html, 'html.parser')

    # data [no]
    result.append(no)

    # data [search name]
    name = soup.select_one(selector='html > body > div > div > div > div > form > div > input')['value']
    result.append(name)

    # data [scholar url]
    scholar_url = 'https://scholar.google.com/scholar?hl=en&as_vis=0&as_sdt=0%2C5&q=' \
                  + re.sub(pattern=r"\(.*\)", repl='', string=name).replace(' ', '+').replace("'", '%27')
    result.append(scholar_url)

    # No results founded
    if 'did not match any article' in html:
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')
        result.append('N/A')
        print(result)
        # data ['No', 'Name', 'scholar URL', 'N/A', 'N/A', 'N/A', 'N/A']
        return result

    # results founded
    else:
        # data [Reference(Oldest)]
        # data [Reference(Newest)]
        column_cited_date = soup.select(selector='body > div > div > div > div > div > div > div > div:nth-child(2)')
        year_list = []

        for i in enumerate(column_cited_date, start=1):
            if re.search(r'[\d]{4}', i[1].text) is not None:
                m = re.search(r'[\d]{4}', i[1].text)
                year_list.append(m.group())
        if len(year_list) > 0:
            result.append(int(min(year_list)))
            result.append(int(max(year_list)))
        else:
            result.append('N/A')
            result.append('N/A')

        # data [cited total count]
        column_cited_total_num = soup.select(
            selector='body > div > div > div > div > div > div > div > div > a:nth-child(3)')
        cited_num_list = []

        for i in enumerate(column_cited_total_num):
            if 'Cited' in i[1].text:
                cited_num_list.append(int(i[1].text.split(' ')[2]))
        if len(cited_num_list) > 0:
            result.append(int(sum(cited_num_list)))
        else:
            result.append('N/A')

        # data [search total count]
        column_search_list_num = soup.select(selector='html > body > div > div > div:nth-child(3) > div')
        for i in column_search_list_num:
            if 'result' in i.text:
                result.append(
                    int(i.text.replace('About', '').replace('results', '').replace('result', '').strip().split('(')[
                            0].replace(",", '')))
            continue

        # data ['No', 'Name', 'scholar URL', 'Reference(Oldest)', 'Reference(Newest)', 'Cited Total Num',
        # 'Search Count Num']
        return result
