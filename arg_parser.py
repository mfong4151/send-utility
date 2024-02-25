import argparse

parser = argparse.ArgumentParser(description="Description here")

# Creates positional arguments for n number of arguments, if not needed then comment out or remove
parser.add_argument('args', nargs="?", help='This should be the name of the file you want to create')