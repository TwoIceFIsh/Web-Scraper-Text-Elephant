import os

from colorama import Fore

from command.cls import cls

cls()


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
                os.system(f'python ./command/{py_name}.py -h')
                return

    show_commads()


def show_commads():
    after_list = os.listdir('./command')
    for i in enumerate(after_list):
        after_list[i[0]] = i[1].split('.')[0]
    after_list.remove('__init__')
    after_list.remove('core')
    after_list.remove('database')
    after_list.remove('tools')
    after_list.remove('__pycache__')
    print(f'Choose command : {sorted(after_list)}')


while True:
    command_text = input(f'{Fore.RED}Text-Elephant >> {Fore.GREEN}')
    try:
        if command_text.split()[0] == 'quit' or command_text.split()[0] == 'exit':
            quit()
    except IndexError:
        show_commads()
        continue
    call_py(command_text)
