import os

from colorama import Fore

from core.banner import banner
from database.crud import do_sql


def edit(command_line: str):
    command_line_list = command_line.split()

    if len(command_line_list) == 2:
        pass
    if len(command_line_list) == 3:
        pass

    pass


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
                main_help()
                continue

            if a_command == 'edit':
                edit(command_line)
                continue

            else:
                print('again')
                pass

        except IndexError:
            pass


def show_help():
    __format = f'{Fore.GREEN}%-5s{Fore.YELLOW}%-10s{Fore.BLUE}%-30s{Fore.BLUE}%-30s'
    print(f'[{Fore.BLACK}ex. show -t 1, show --settings]')
    print(f'{Fore.RED}%-5s%-10s%-30s%-30s' % ('no', 'commands', 'args', 'text'))
    print(__format % ('1', 'show', '-t, --templates, [n]', 'show templates'))
    print(__format % ('2', 'show ', '-s, --settings', 'show settings'))


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

        command_line_list = command_line.split()
        args = command_line_list[1]
        if len(command_line_list) == 2:

            if args == '--templates' or args == '-t':

                lists = do_sql('select * from template_list')
                for i in lists:
                    print(f'[{i[0]}] {i[1]}')

                try:

                    command_line = input(f'\n{Fore.RED}Select Template Number >> {Fore.GREEN}')
                    selected_name = do_sql(f'select * from template_list where no ={int(command_line)}')
                    clear_console()
                    banner()
                    show_template(selected_name)
                    return

                except:
                    pass

            if args == '--settings' or args == '-s':
                lists = do_sql('select * from settings')
                print(f'%-5s%-20s%-30s' % ('no', 'type', 'text'))
                for i in lists:
                    print(f'{Fore.GREEN}%-5s{Fore.YELLOW}%-20s{Fore.BLUE}%-30s' % (i[0], i[1], i[2]))
                return
        if len(command_line_list) == 3:
            if args == '--templates' or args == '-t':
                selected_name = do_sql(f'select * from template_list where no ={int(command_line_list[2])}')
                clear_console()
                banner()
                show_template(selected_name)
                return

        show_help()

    except:
        show_help()


def main_help():
    print('help')


def exit():
    quit()


def clear_console():
    __command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        __command = 'cls'
    os.system(__command)
