from core.ini import *
from core.menu import *
from core.start import banner
# Show banner
from database.crud import create_db

create_db()

# Check config file
if os.path.isfile('./Settings.ini') is False:
    config_generator()
else:
    # TODO: check config file
    print('#TODO: check config file')

while True:
    clear_console()
    banner()
    print_menu(menu_options)
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:

        option1()
    elif option == 2:
        print_menu(run_options)
    elif option == 3:
        print('Thanks message before exiting')
        exit()
        clear_console()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
