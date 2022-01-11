

import string

def update_char(string, position, character):
    return string[ :position] + character + string[position + 1: ]
