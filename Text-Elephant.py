import os

from core.ini import *

# Check config file

if os.path.isfile('./Settings.ini') is False:
    config_generator()
else:
    # TODO: check config file
    pass

while True:
    show_menu()
