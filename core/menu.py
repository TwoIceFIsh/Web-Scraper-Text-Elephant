import os

from database.crud import db_select

menu_options = {
    1: 'Settings',
    2: 'Run',
}
 
run_options = {
    1: 'Settings',
    2: 'Collecting Datas',
    3: 'Processing Datas',
    4: 'Exit',
}


def print_menu(menu: dict):
    for key in menu.keys():
        print(key, '--', menu[key])


def option1():
    db_select('select * from template_list')
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
