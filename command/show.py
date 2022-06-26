import argparse
import os

from colorama import Fore

from database.crud import do_sql


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


parser = argparse.ArgumentParser(prog='show', usage='%(prog)s [options]')
parser.add_argument('options', choices=['templates', 'options'])

args = parser.parse_args()

if args.options == 'templates':
    # show templates list
    selected_template = ''
    template_list = do_sql('select * from template_list')
    for i in template_list:
        print(i)
        selected_template = i

    # show template info
    template = input('Choose template number > ')
    template_info = do_sql(f'select * from "{selected_template[1]}" where no = {template}')
    if len(template_info) > 0:
        cls()
        print(f'{Fore.RED}{i[1]}{Fore.CYAN}')
        print(f'{"No":-<4}{"Column":-<10}{"Selector":-<60}{"x_len":-<10}{"x":-<4}{"Test":-<10}')
        for ii in template_info:
            print(f'{ii[0]: <4}{ii[1]: <10}{ii[2]: <60}{ii[3]: <10}{ii[4]: <4}{ii[5]: <10}')

    else:
        cls()
        print(f'{Fore.RED}{i[1]}{Fore.CYAN}')
        print('No data')

if args.options == 'options':
    option_list = do_sql('select * from settings')
    print(f'{Fore.RED}Show Run options{Fore.CYAN}')
    print(f'{"No":-<4}{"Key":-<20}{"Value":-<20}')
    for i in option_list:
        print(f'{i[0]: <4}{i[1]: <20}{i[2]: <20}')
