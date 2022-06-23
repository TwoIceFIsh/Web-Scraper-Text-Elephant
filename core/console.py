import os

from colorama import Fore

from core.banner import banner
from database.crud import do_sql


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def next_page():
    clear_console()
    banner()
    status_bar()


def status_bar():
    print(f"{do_sql(query_text='select * from settings')}")
    print(f'{Fore.YELLOW} ========================================================================')
