#######################################################################################
import secrets
from random import randint, choices
from string import ascii_letters, digits
from time import mktime, strptime, strftime, localtime
#######################################################################################
def generate_random_id(length=10):
    # Combines letters (a-z, A-Z) and digits (0-9)
    characters = ascii_letters + digits
    # Picks characters at random and joins them
    return ''.join(choices(characters, k=length))
#######################################################################################
def generate_random_hex_color():
    # Generate a random integer between 0 and 0xFFFFFF (16777215) and Format it as a 6-digit hex string with a leading '#'
    return f"#{randint(0, 0xFFFFFF):06x}"
##########################################################################@############
def generate_id(length=10):
    # Generate random secure token hex string of length characters
    return secrets.token_hex(length // 2)
#######################################################################################
def get_zero_formatted_number(number, length=10):
    # Convert a number to a string with leading zeros
    return str(number).zfill(length)
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
def calculate_duration(start_str, end_str, datetime_format="%d-%m-%Y %H:%M:%S"):
    # convert datetime strings to datetime objects
    start_time = strptime(start_str, datetime_format)
    end_time = strptime(end_str, datetime_format)
    # get the time difference (duration) in seconds and parse it as int
    total_seconds = int((end_time - start_time).total_seconds())
    # use divmod to extract duration as HH, MM, SS
    hours, seconds_remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(seconds_remainder, 60)
    # return duration as HH:MM:SS
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#######################################################################################
def get_bmi_rate(weight, height):
    return weight / height ** 2
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    else:
        return "Overweight"
def get_person_bmi(weight, height):
    bmi = get_bmi_rate(weight, height)
    category = get_bmi_category(bmi)
    return f"Your BMI is {bmi:.2f} and you are {category} person"
#######################################################################################
def get_person_age(birth_year):
    current_year = int(strftime("%Y"))
    return current_year - birth_year
#######################################################################################
def get_person_generation(birth_year):
    if birth_year >= 1965 and birth_year <= 1980:
        return "Gen X"
    elif birth_year >= 1981 and birth_year <= 1996:
        return "Gen Y"
    elif birth_year >= 1997 and birth_year <= 2012:
        return "Gen Z"
    elif birth_year >= 2013 and birth_year <= 2025:
        return "Gen Alpha"
    else:
        return "Gen Beta"
#######################################################################################
