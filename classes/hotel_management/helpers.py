
##########################################################################
from string import ascii_letters, digits
from random import randint, choices
##########################################################################
def generate_id(length=10):
    # Combines letters (a-z, A-Z) and digits (0-9)
    characters = ascii_letters + digits
    # Picks characters at random and joins them
    return ''.join(choices(characters, k=length))
##########################################################################
