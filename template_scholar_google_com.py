import re
from bs4 import BeautifulSoup


def template_scholar_google_com(html: str):
    """
    template_scholar_google_com
    :param html:
    :return:
    """
    result = []
    soup = BeautifulSoup(html, 'html.parser')

    # search total count
    column_search_list_num = soup.select(selector='body > div > div > div:nth-child(3) > div')
    for i in enumerate(column_search_list_num):
        if re.search('About \d', i[1].text):
            result.append(int(i[1].text.split(' ')[1].replace(',','')))
    # cited total count
    column_cited_total_num = soup.select(selector='body > div > div > div > div > div > div > div > div > a')
    cited_num_list = []
    for i in enumerate(column_cited_total_num):
        if 'Cited' in i[1].text:
            cited_num_list.append(int(i[1].text.split(' ')[2]))
    result.append(int(sum(cited_num_list)))

    # max_year, min_year
    column_cited_date = soup.select(selector='body > div > div > div > div > div > div > div > div:nth-child(2)')
    year_list = []
    for i in enumerate(column_cited_date,start=1):
        if re.search(r'[\d]{4}',i[1].text) is not None:
            m = re.search(r'[\d]{4}',i[1].text)
            year_list.append(m.group())

    result.append(int(min(year_list)))
    result.append(int(max(year_list)))

    return result


