from string import ascii_letters, digits
from random import randint, choices
##########################################################################
def generate_id(length=10):
    # Combines letters (a-z, A-Z) and digits (0-9)
    characters = ascii_letters + digits
    # Picks characters at random and joins them
    return ''.join(choices(characters, k=length))
##########################################################################
def generate_color():
    # Generate a random integer between 0 and 0xFFFFFF (16777215) and Format it as a 6-digit hex string with a leading '#'
    return f"#{randint(0, 0xFFFFFF):06x}"
##########################################################################
