from pyperclip import copy, paste
from typing import List
from utils.colorize import colorize, BOLD, MAGENTA, RED

def copy_to_clipboard(*args:List[str]) -> None:
    formatting = f"{BOLD}{MAGENTA}"
    copy('\n'.join(args))
    
def retrieve_from_clipboard() -> str:
    return paste()