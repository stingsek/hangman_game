import os


def is_file_valid(file_path):
    lines = []
    if not file_path:
        return False
    if is_text_file(file_path):
        try:
            with open(file_path,'r', encoding='utf-8') as file:
                if not is_file_empty(file):
                     lines = [line.rstrip('\n') for line in file]
                     return all(is_line_valid(line) for line in lines)
        except (UnicodeDecodeError, FileNotFoundError, PermissionError):
            return False        

# line is valid if it contains only letters or spaces 
def is_line_valid(line):
    return all(c.isalpha() or c.isspace() for c in line)



def is_file_empty(file):
    first_line = file.readline()
    return not first_line
        

def is_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8'):
            return file_path.endswith(".txt")
    except FileNotFoundError:
        return False

def load(file_path):
    with open(file_path,'r', encoding='utf-8') as file:
        words = [line.rstrip('\n') for line in file]
    return words

def extract_category(filepath):
    start_index = filepath.rindex('/') + 1
    end_index = len(filepath) - 4
    return filepath[start_index:end_index].upper()       
