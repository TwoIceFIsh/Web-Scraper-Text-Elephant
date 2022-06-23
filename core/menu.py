from core.console import next_page
from database.crud import do_sql

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


def set_template():
    next_page()
    for i in do_sql(query_text='select * from template_list'):
        print(f'{i}\n')
    value = input('Select template : ')
    column_data = 'Template'
    datas = (value, column_data)
    if type(int(value)) == type(1):
        pass
        # do_sql(query_text="update settings SET value=? where key=?")
        # do_sql(query_text=f'update settings set value={str(value)} where key={column_data}')

    else:
        print('Select Num')
