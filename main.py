import os

from core.console import clear_console
from core.ini import *
from core.menu import *
# Show banner
from database.crud import do_sql

# Check config file
if os.path.isfile('./Settings.ini') is False:
    config_generator()
else:
    # TODO: check config file
    pass

while True:
    # header initialisation
    next_page()

    # menu initialization
    print_menu(menu_options)
    option = ''
    try:
        do_sql('select * from settings')
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:
        set_template()
    elif option == 2:
        print_menu(run_options)
    elif option == 3:
        clear_console()
        exit()

    else:
        print('Invalid option. Please enter a number between 1 and 4.')
