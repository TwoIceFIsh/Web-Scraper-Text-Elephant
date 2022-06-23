import os

from colorama import Fore

from core import node
from core.banner import __banner
from core.menu import *
from database.crud import do_sql


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def __print_menu(menu: dict):
    for key in menu.keys():
        print(key, '--', menu[key])


def __status_bar():
    print(f"{do_sql(query_text='select * from settings')}")
    print(
        f'{Fore.YELLOW} ========================================================================================================')


def next_page(menu: dict):
    clear_console()
    __banner()
    __status_bar()
    __print_menu(menu)

    try:
        return int(input('Select Number : '))
    except:
        print('Please valid number')


# TODO: Stack으로 페이지 이동 구현해보기
def show_menu():
    list = node.LinkedList(menu_main)
    option = next_page(menu=menu_main)
    if option == 1:
        list.append(menu_run)
        # next_page(menu=menu_run)
        if option == 1:
            list.append(menu_collecting_html)
            next_page(menu=menu_collecting_html)
        if option == 2:
            list.append(menu_processing_data)
        next_page(menu=menu_processing_data)
        if option == 3:
            list.delete_node(-1)
            next_page(menu=menu_run)
    if option == 3:
        clear_console()
        exit()
