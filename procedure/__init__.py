from utils.file_io import read_files, write_files
from utils.colorize import colorize, RED, BOLD, DEFAULT
from utils.copy_to_clipboard import retrieve_from_clipboard

def main_procedure(dest_file_name: str):
    
    #Read Clipboard
    new_text = retrieve_from_clipboard() 
    #Write to file
    write_files(dest_file_name, new_text)
      
    return    
