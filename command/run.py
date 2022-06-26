import argparse
import os

from colorama import Fore


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


parser = argparse.ArgumentParser(prog='run', usage='%(prog)s [options]')
parser.add_argument('options', choices=['collecting', 'processing'])

args = parser.parse_args()

if args.options == 'collecting':
    print('collecting')

if args.options == 'processing':
    print('processing')
