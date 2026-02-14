#######################################################################################
import secrets
from random import randint
from time import mktime, strptime, strftime, localtime
#######################################################################################
def generate_id(length=10):
    # Generate random secure token hex string of length characters
    return secrets.token_hex(length // 2)
#######################################################################################
def get_random_date_between(start_str, end_str, date_format="%d-%m-%Y"):
    # convert string dates to time object then convert to unix timestamps
    start_timestamp = mktime(strptime(start_str, date_format))
    end_timestamp = mktime(strptime(end_str, date_format))
    # generate random timestamp in range using randint
    random_timestamp = randint(int(start_timestamp), int(end_timestamp))
    # convert timestamp to date object then convert to date string and return it
    return strftime(date_format, localtime(random_timestamp))
#######################################################################################
def get_zero_formatted_number(number, length=10):
    # Convert a number to a string with leading zeros
    return str(number).zfill(length)
#######################################################################################
