from bs4 import BeautifulSoup

from tools.text_mining import select_rows


def set_columns():
    return ['No', 'Name', 'Url', 'Domain', 'Kingdom', 'Phylum', 'Subphylum', 'Class',
            'Distribution Table - Continent/Country/Region', 'Habitat List - Category', 'Habitat List - Sub-Category',
            'Habitat List - Habitat', 'Habitat List - Presence', 'Host Plants and Other Plants Affected - Plant name',
            'Host Plants and Other Plants Affected - Family', 'Host Plants and Other Plants Affected - Context',
            'Growth Stages', 'List of Symptoms/Signs - Sign', 'References(Total num)', 'References(USDA num)',
            'References(Oldest)', 'References(Newest)', 'Distribution References', 'Pathway Causes - Cause',
            'Pathway Vectors - Vector', 'Impact Summary - Category']


def input_html(no: int, html: str):
    result = []
    soup = BeautifulSoup(html, 'html.parser')

    # No
    result.append(no)

    # Url
    result.append(no)

    # Name
    name = soup.select_one('body > div > div > div > div > div > h3')
    result.append(name.text.strip())

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

    # # Distribute Table
    # if 'Distribution Table' in html:
    #     qs = '#todistributionDatabaseTable > div > div > div > table > tbody > tr > td > a'
    #     ws_new.cell(row=row, column=20, value=';'.join(tm.get_text_all_search(soup, qs, '-', 'n')))
    # else:
    #     result.append('N/A')
    #
    # # Habitat List
    # if 'Habitat List' in html:
    #     qs = '#toenvironments > div > table > tbody > tr > td'
    #     ws_new.cell(row=row, column=21, value=';'.join(tm.get_table_all(soup, qs, 5, 1)))
    #     ws_new.cell(row=row, column=22, value=';'.join(tm.get_table_all(soup, qs, 5, 2)))
    #     ws_new.cell(row=row, column=23, value=';'.join(tm.get_table_all(soup, qs, 5, 3)))
    #     ws_new.cell(row=row, column=24, value=';'.join(tm.get_table_all(soup, qs, 5, 4)))
    #
    # else:
    #     result.append('N/A')
    #     result.append('N/A')
    #     result.append('N/A')
    #     result.append('N/A')

    # Host Plants and Other Plants Affected
    if 'Host Plants and Other Plants Affected' in html:
        hpopa_list = soup.select('#tohostPlants > div > div > table > tbody > tr > td')
        result += ';'.join(select_rows(input_list=hpopa_list, no_y=1, no_x=4))
        result += ';'.join(select_rows(input_list=hpopa_list, no_y=2, no_x=4))
        result += ';'.join(select_rows(input_list=hpopa_list, no_y=3, no_x=4))

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
        list = soup.select('#tosymptomsOrSigns > div > div > table > tbody > tr > td')
        result += ';'.join(select_rows(input_list=list, no_x=3, no_y=1))
    else:
        result.append('N/A')

    # # References(Total num)
    # if 'References' in html:
    #     qs = '#toreferences > div > p'
    #     ws_new.cell(row=row, column=30, value=len(tm.get_text_all(soup, qs)))
    # else:
    #     result.append('N/A')
    #
    # # References(USDA num Kyeaword Search)
    # if 'References' in html:
    #     qs = '#toreferences > div > p > a'
    #     search_text = 'Department of Agriculture'
    #     ws_new.cell(row=row, column=31, value=len(tm.get_text_all_search(soup, qs, search_text, 'y')))
    # else:
    #     result.append('N/A')
    #
    # # References(Old New)
    # if 'References' in html:
    #
    #     qs = '#toreferences > div > p'
    #     year = tm.get_year_cabi(soup, qs)
    #
    #     ws_new.cell(row=row, column=32, value=int(min(year)))
    #     ws_new.cell(row=row, column=33, value=int(max(year)))
    #
    # else:
    #     ws_new.cell(row=row, column=32, value='N/A')
    #     ws_new.cell(row=row, column=33, value='N/A')
    #
    # # Distribution References(num)
    # if 'Distribution References' in html:
    #     qs = '#toreferences > div > div > p'
    #     ws_new.cell(row=row, column=34, value=len(tm.get_text_all(soup, qs)))
    #
    # else:
    #     ws_new.cell(row=row, column=34, value=0)
    #
    # # Pathway Causes - Cause
    # if 'Pathway Causes' in html:
    #     qs = '#topathwayCauses > div > div > table > tbody > tr > td > a'
    #     ws_new.cell(row=row, column=35, value=';'.join(tm.get_text_all(soup, qs)))
    #
    # else:
    #     ws_new.cell(row=row, column=35, value='N/A')
    #
    # # Pathway Vectors - Vector
    # if 'Pathway Vectors' in html:
    #     qs = '#topathwayVectors > div > div > table > tbody > tr > td > a'
    #     ws_new.cell(row=row, column=36, value=';'.join(tm.get_text_all(soup, qs)))
    #
    # else:
    #     ws_new.cell(row=row, column=36, value='N/A')
    #
    # # Impact Summary - Category
    # if 'Impact Summary' in html:
    #     impact_summary = soup.select_one('#toimpactSummary > div > div > table > tbody > tr > td')
    #     result.append(impact_summary.text)
    #     ws_new.cell(row=row, column=37, value=';'.join(tm.get_table_all(soup, qs, 2, 1)))
    #
    # else:
    #     ws_new.cell(row=row, column=37, value='N/A')
    print(result)
    return result

#
# def get_year_cabi(soup: soup_object, qs):
#     year_list = []
#     result_list = soup.select(qs)
#
#     append = year_list.append
#     for result in result_list:
#         # 숫자4개 및 문자 1개를 파싱
#         out_text = re.findall(r'([ ]?\d{4}[a-z]{0,1}[-,\. \d]?)', result.text)
#
#         # 정규식에 맞는 문자열이 1개이상 있으면 정제 작업 수행
#         if len(out_text) > 0:
#             out_text[0] = re.sub(r'[a-z]?\.?,? ?-?', '', out_text[0])
#
#             # 데이터가 2022를 초과하거나 숫자로 5자리 이상이면 스킵
#             if (len(out_text[0]) > 4) or (int(out_text[0]) > 2022):
#                 # print('[Not year] ' + out_text[0] + ' : ' + str(result.text))
#                 continue
#             append(int(out_text[0]))
#
#     return year_list
