import multiprocessing
import os
import random
import re
import time

import requests

from mail_func import sendMail


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
        pool = multiprocessing.Pool(processes=60)
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
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
            'Cookie': 'AEC=AakniGOnpF2nBzjctcvYDJ-atN3mu8F_201VqXBX65d1Ku5zaHpWqn62Lg; 1P_JAR=2022-06-20-09; NID=511=JS2_O17zyNEIaQLUUdSC0oqb0w3EUnvGd0beN_Y0HQjqJboMOPMZKhOcKws8abwPcyM8SHurqCtI0ndId114XPh8B4VQV2JSgR1bKoq3CGvz0Ctcl9LcOq05SS2WB9DfePq7TqkyAhmTu3U6oPc29vrCrZXsfPLvGbq0CzAzpfU; GSP=A=kkBOvw:CPTS=1655716886:LM=1655716886:S=UeBsNUsGvBVR1eZN; GOOGLE_ABUSE_EXEMPTION=ID=262779af78884ff9:TM=1655720214:C=r:IP=183.96.162.58-:S=NJ712P7k_5VSAvFtjRyoOyY',
            'Referer': 'https://scholar.google.com/',
            'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"'
        }

        time.sleep(random.uniform(1, 120))
        response = requests.get(a_url, headers=headers)

        if response.status_code == 200 and "a robot" not in response.text:
            f2 = open('./datas/' + str(a_no) + '.html', 'w', encoding='UTF-8')
            f2.write(response.text.strip())
            f2.close()
            print(
                f'[{str(now)} > {str(round(time.time() - start_time2, 1))}s] Collected [{str(len(os.listdir("./datas")))}/{str(a_total_num)}] -{str(round(float(float(a_total_num) - len(os.listdir("./datas"))) / 0.5 / 60, 2))}m({str(round(float(float(a_total_num) - len(os.listdir("./datas"))) / 0.5 / 60 / 60, 1))}h)  Url : {str(a_no)} {a_url}')
        elif "not a robot" in response.text:
            print('!!(R)ROBOT!! [' + str(now) + ' > ' + str(round(time.time() - start_time2, 1)) + 's] Url : ' + a_url)
            sendMail(
                article=f'[{str(now)} > {str(round(time.time() - start_time2, 1))}s] Robot [{str(len(os.listdir("./datas")))}/{str(a_total_num)}] -{str(round(float(float(a_total_num) - len(os.listdir("./datas"))) / 0.5 / 60, 2))}m({str(round(float(float(a_total_num) - len(os.listdir("./datas"))) / 0.5 / 60 / 60, 1))}h)  Url : {str(a_no)} {a_url}',
                new_num=80, to_ad='team.k0konutz@gmail.com')
            time.sleep(100)
            os.system('shutdown -s -f')

        else:
            print(
                f'!![{str(response.status_code)}]!! [{str(now)} > {str(round(time.time() - start_time2, 1))}s] Url : {a_url}')
    else:
        print(f'File has found : {str(a_no)} {a_url}')
