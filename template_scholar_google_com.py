import re

from bs4 import BeautifulSoup


def template_scholar_google_com(no: int, html: str):
    """
    template_scholar_google_com
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
        result.append(int(min(year_list)))
        result.append(int(max(year_list)))

        # data [cited total count]
        column_cited_total_num = soup.select(
            selector='body > div > div > div > div > div > div > div > div > a:nth-child(3)')
        cited_num_list = []
        for i in enumerate(column_cited_total_num):
            if 'Cited' in i[1].text:
                cited_num_list.append(int(i[1].text.split(' ')[2]))
        result.append(int(sum(cited_num_list)))

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
