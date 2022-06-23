import os

from colorama import Fore

from core.start import banner
from database.crud import db_select

menu_options = {
    1: 'Settings',
    2: 'Run',
    3: 'Exit'
}

settings_options = {
    1: 'Url list',
    2: 'Collecting Datas',
    3: 'Processing Datas',
    4: 'Back',
}

run_options = {
    1: 'Full Auto',
    2: 'Just Collecting Datas',
    3: 'Just Processing Datas',
    4: 'Back',
}


def print_menu(menu: dict):
    for key in menu.keys():
        print(key, '--', menu[key])


def option1():
    db_select(query='select * from template_list', concat=0)
    value = input('Select template : ')


def option2():
    print('Handle option \'Option 2\'')


def option3():
    print('Handle option \'Option 3\'')


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def status_bar():
    print(f"Settings {db_select(query='select * from settings', concat=1)} {Fore.YELLOW}")


def next_page():
    clear_console()
    banner()
    status_bar()
