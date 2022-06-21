import multiprocessing
import os
import random
import re
import time

import requests

from tools.mailing import sendMail


def get_list_from(name_list_file):
    result = []
    file = open(name_list_file, 'r', encoding='utf-8')
    for name in file.readlines():
        result.append(
            re.sub(pattern=r"\(.*\)", repl='', string=name).replace('\n', '').replace(' ', '+').replace("'", '%27'))
    file.close()
    return result


def add_prefix(name_list: list, prefix: str, prefix2: int):
    result = name_list
    for i in enumerate(result):
        result[i[0]] = f'{str(i[0] + 1)}|{prefix}{i[1]}|{str(prefix2)}'
    return result


def time_m(a_total_num: int, elapsed_sec: float):
    return round(float(float(a_total_num) - len(os.listdir("./datas"))) * elapsed_sec / 60, 1)


def time_h(a_total_num: int, elapsed_sec: float):
    return round(float(float(a_total_num) - len(os.listdir("./datas"))) * elapsed_sec / 60 / 60, 1)


def collect_html_from(url_list: list):
    """
    Multiprocessing(Data Collecting Logic)
    :param url_list:
    :return:
    """
    if not os.path.isdir('./datas'):
        os.mkdir('./datas')

    while True:
        file_list2 = os.listdir('./datas')
        if len(file_list2) == len(url_list):
            break
        pool = multiprocessing.Pool(processes=2)
        pool.map(data_collect, url_list)
        pool.close()
        pool.join()


def data_collect(url_text: str):
    """
    Data Collecting Logic
    :param url_text:
    :return:
    """
    start_time2 = time.time()
    a_no = url_text.split('|')[0]
    a_url = url_text.split('|')[1]
    a_total_num = url_text.split('|')[2]

    if not os.path.isfile('./datas/' + str(a_no) + '.html'):

        import string
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
            'Cookie': 'GSP=A=kkBOvw:CPTS=1655786455:LM=1655786455:S=BXjRLCmgZenj_ytR; NID=511=Id4TpY2WOU0MzTIh6kRTX-EoX-kNgkL5MUqVbRY6yzrA8IdyPsi1cmAIIzBHUvPFGZSavg-Ar1bFOXecjRzGKLt1SfY2mCclnh8kR368fa0dcEeQPv7Bg7NMeeZoFdbpk9TOyYx4UgGT6OaT3-vK5njr0pDxEqqLBRSaLQ-at2M',
            'Referer': 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + ''.join(
                random.choice(string.ascii_letters) for i in range(5)),
            'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"'
        }

        time.sleep(random.uniform(1, 10))
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        response = requests.get(a_url, headers=headers)

        if response.status_code == 200 and "a robot" not in response.text:
            f2 = open('./datas/' + str(a_no) + '.html', 'w', encoding='UTF-8')
            f2.write(response.text.strip())
            f2.close()
            print(
                f'[{str(now)} > {str(round(time.time() - start_time2, 1))}s] Collected [{str(len(os.listdir("./datas")))}/{str(a_total_num)}] -{time_m(a_total_num=int(a_total_num), elapsed_sec=4)}m({time_h(a_total_num=int(a_total_num), elapsed_sec=4)}h)  Url : {str(a_no)} {a_url}')
            if len(os.listdir("./datas")) % 100 == 0:
                sendMail(title_text=f'[진행상황] [{str(len(os.listdir("./datas")))}/{str(a_total_num)}] ',
                         body_text='COLLECTED',
                         to_ad='team.k0konutz@gmail.com')
                sendMail(title_text=f'[진행상황] [{str(len(os.listdir("./datas")))}/{str(a_total_num)}] ',
                         body_text='COLLECTED',
                         to_ad='aidenlee@gravity.co.kr')
        elif "not a robot" in response.text:
            print('!!(R)ROBOT!! [' + str(now) + ' > ' + str(round(time.time() - start_time2, 1)) + 's] Url : ' + a_url)
            sendMail(title_text=f'[ROBOT] 쿠키를 갈아주세요 ', body_text='ROBOT', to_ad='team.k0konutz@gmail.com')
            quit()
            return
        else:
            print(
                f'!![{str(response.status_code)}]!! [{str(now)} > {str(round(time.time() - start_time2, 1))}s] Url : {a_url}')
    else:
        # print(f'File has found : {str(a_no)} {a_url}')
        None


#
# def make_output_file(output_file_name: str, col_list: list):
#     wb = Workbook()
#     ws = wb.active
#
#     # excel file initialisation
#     ws.append(col_list)
#     wb.save(filename=output_file_name)
#
#     # excel file writelines
#     for html in enumerate(os.listdir('./datas'), start=1):
#         print(f'{html[1]} [{html[0]}/{len(os.listdir("./datas"))}]')
#
#         try:
#             f = open('./datas/' + html[1], 'r', encoding='utf-8')
#             ws.append(template_scholar_google_com(html[0], f.read()))
#         except:
#             print('error file : ./datas/' + html[1])
#             ws.append(template_scholar_google_com(html[0], f.read()))
#         finally:
#             wb.save(filename=output_file_name)
#
#     wb.close()


def xpath_to_selector(xpath_text: str):
    xpath_list = xpath_text.split('/')
    result = ''
    for i in xpath_list:
        if len(i) > 0:
            x = re.sub(r'\[.*\]', '', i)
            if xpath_list[len(xpath_list) - 1] == i:

                result += x
            else:
                result += x + ' > '
    return result


def select_rows(input_list: list, no_x: int, no_y: int):
    result = []
    for i in enumerate(input_list, start=1):
        if i[0] % no_x == no_y:
            print(i[1].text.strip())
            result.append(i[1].text.strip())
    return result
