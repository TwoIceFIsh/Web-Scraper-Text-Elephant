import os

from colorama import Fore

from core.banner import banner
from database.crud import do_sql

command_list = ['exit', 'help', 'show', 'back']


def command():
    while True:
        try:
            command_line = input(f'\n{Fore.RED}Text-Elephant >> {Fore.GREEN}')
            a_command = command_line.split()[0]

            if a_command == 'exit':
                quit()
                continue

            if a_command == 'show':
                show(command_line)
                continue
            if a_command == 'clear' or a_command == 'cls':
                clear_console()
                banner()
                continue

            if a_command == 'help' or a_command == 'h':
                help()
                continue

            else:
                print('again')
                pass

        except IndexError:
            pass


def show_help():
    print(f'{Fore.BLACK}ex. show 1 / show templates')
    print(f'{Fore.RED}%-5s%-20s%-30s' % ('no', 'commands', 'text'))
    print(f'{Fore.GREEN}%-5s{Fore.YELLOW}%-20s{Fore.BLUE}%-30s' % ('1', 'show templates', 'show templates'))
    print(f'{Fore.GREEN}%-5s{Fore.YELLOW}%-20s{Fore.BLUE}%-30s' % ('2', 'show settings', 'show settings'))


def show_template(template: list):
    __format = f'%-5s%-20s%-8s%-5s%-60s%-30s'
    print(f'Selected Template: {template[0][1]}')
    print(__format % ('no', 'Name', 'x_len', 'x', 'Selector', 'Result'))
    if len(template) != 0:
        lists = do_sql(f'select * from "{template[0][1]}"')
        print(__format % (
            lists[0][0], lists[0][1], lists[0][4], lists[0][5], lists[0][2], lists[0][3]))


def show(command_line: str):
    try:
        args = command_line.split()[1]
        if args == 'templates' or args == '1':

            lists = do_sql('select * from template_list')
            for i in lists:
                print(f'[{i[0]}] {i[1]}')

            try:
                command_line = input(f'\n{Fore.RED}Select Template Number >> {Fore.GREEN}')
                selected_name = do_sql(f'select * from template_list where no ={int(command_line)}')
                show_template(selected_name)
                return
            except:
                pass

        if args == 'settings' or args == '2':
            lists = do_sql('select * from settings')
            print(f'%-5s%-20s%-30s' % ('no', 'type', 'text'))
            for i in lists:
                print(f'{Fore.GREEN}%-5s{Fore.YELLOW}%-20s{Fore.BLUE}%-30s' % (i[0], i[1], i[2]))
            return

        show_help()

    except:
        show_help()


def help():
    print('help')


def exit():
    quit()


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
