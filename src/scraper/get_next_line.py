def get_next_line(string):
    """ Returns everything from the start of string to the first null byte """
    
    return string[:string.find("\n")]
