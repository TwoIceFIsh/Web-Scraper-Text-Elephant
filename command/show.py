import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('sss', help='an integer for the accumulator', action='store')
parser.add_argument('a', help='an integer for the accumulator', action='store')
parser.add_argument('ss', help='an integer for the accumulator', action='store')

args = parser.parse_args()
print(args)
