from arg_parser import parser
from procedure import main_procedure
from utils.colorize import colorize,CYAN 

if __name__ == "__main__":
    args = parser.parse_args()
    dest_file_name = args.args if args.args else "RENAMEME.txt"
    main_procedure(dest_file_name)
    print(colorize(CYAN, f"Your clipboard items have been moved to {dest_file_name}\n"))
    