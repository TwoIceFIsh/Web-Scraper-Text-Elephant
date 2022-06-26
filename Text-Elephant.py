import os

from colorama import Fore

from core.banner import banner
from core.console import clear_console

clear_console()
banner()


def call_py(command_line: str):
    command_list = command_line.split()
    py_name = command_line.split()[0]

    for i in os.listdir('./command'):
        if i == py_name + '.py':

            if len(command_list) > 1:
                args = ''
                for i in command_list[1:]:
                    args += i + ' '
                os.system(f'python ./command/{py_name}.py {args}')
                return
            else:
                os.system(f'python ./command/{py_name}.py')
                return

    after_list = os.listdir('./command')
    for i in enumerate(after_list):
        after_list[i[0]] = i[1].split('.')[0]
    after_list.remove('__init__')
    print(f'choose command : {sorted(after_list)}')


while True:
    command_text = input(f'{Fore.RED}Text-Elephant >> {Fore.GREEN}')
    if command_text.split()[0] == 'quit' or command_text.split()[0] == 'exit':
        quit()
    call_py(command_text)
