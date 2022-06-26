import argparse
import os
import re

from colorama import Fore

from database.crud import do_sql

SELECT_ALL_FROM_TEMPLATE_LIST = f'select * from template_list'
SELECT_ALL_FROM_SETTINGS = 'select * from settings'
SETTINGS_COLUMNS = f'{"No":-<4}{"Key":-<20}{"Value":-<30}{"Comments":-<20}'


def banner():
    print(Fore.GREEN + f'''
████████╗███████╗██╗  ██╗████████╗    ███████╗██╗     ███████╗██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔════╝██║     ██╔════╝██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝
   ██║   █████╗   ╚███╔╝    ██║       █████╗  ██║     █████╗  ██████╔╝███████║███████║██╔██╗ ██║   ██║   
   ██║   ██╔══╝   ██╔██╗    ██║       ██╔══╝  ██║     ██╔══╝  ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   
   ██║   ███████╗██╔╝ ██╗   ██║       ███████╗███████╗███████╗██║     ██║  ██║██║  ██║██║ ╚████║   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
Made {Fore.RED}♥{Fore.GREEN} by Aiden Lee(@Twoicefish) {Fore.CYAN}''')


def cls():
    __command = 'clear'

    if os.name in ('nt', 'dos'):
        __command = 'cls'

    os.system(__command)
    banner()


def show_options():
    option_list = do_sql(SELECT_ALL_FROM_SETTINGS)
    print(f'{Fore.RED}Set Run options{Fore.CYAN}')
    print(SETTINGS_COLUMNS)
    for i in option_list:
        print(f'{Fore.RED}{i[0]: <4}{Fore.GREEN}{i[1]: <20}{Fore.RED}{i[2]: <30}{Fore.GREEN}{i[3]: <30}')


def clear_show():
    cls()
    show_options()


parser = argparse.ArgumentParser(prog='set', usage='%(prog)s [options]')
parser.add_argument('options', choices=['templates', 'options'])

args = parser.parse_args()


def start():
    clear_show()
    if args.options == 'templates':
        selected_option = input(f'{Fore.RED}Change No [q] > {Fore.GREEN}')
    if args.options == 'options':

        selected_option = input(f'{Fore.RED}Change No [q] > {Fore.GREEN}')

        if selected_option == 'q':
            quit()
        try:
            cls()
            # show before data
            before_data = do_sql(f'select * from settings where no = {int(selected_option)}')[0]
            print(SETTINGS_COLUMNS)
            print(
                f'{before_data[0]: <4}{before_data[1]: <20}{Fore.RED}{before_data[2]: <30}{Fore.GREEN}{before_data[3]: <20}')

            if selected_option == '1':
                # show templates
                template_list = do_sql(SELECT_ALL_FROM_TEMPLATE_LIST)
                print('Templates : ' + str(template_list))

                try:
                    new_value = input(f'{Fore.RED}Choose Template No > {Fore.GREEN}')
                    template_name = do_sql(f'select name from template_list where no ={str(new_value)}')[0][0]
                    do_sql(f'update settings set value="{template_name}" where no = {int(selected_option)}')
                    clear_show()
                    return
                except IndexError:
                    return

            if selected_option == '2' or selected_option == '3' or selected_option == '4':
                new_value = input(f'{Fore.RED}New Value > {Fore.GREEN}')

                if selected_option == '2':
                    if len(new_value) == 0:
                        return
                    new_value = new_value.strip()

                    new_value = re.sub(f'[^a-zA-z0-9.]+', '', new_value)
                    new_value = new_value.replace('.xlsx', '')

                if selected_option == '3':
                    try:
                        if int(new_value) > 60:
                            new_value = "60"
                    except ValueError:
                        return

                if selected_option == '4':

                    if '@' not in new_value:
                        return

                do_sql(f'update settings set value="{new_value}" where no = {int(selected_option)}')
                clear_show()

        except ValueError:
            pass


while True:
    start()
