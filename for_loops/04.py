# build a persons generation indicator program:
# collect the number of persons
# loop in every person and get the person's name and birth year
# then calculate the person's generation based on the birth year
# as from 1965 to 1980 is [Gen X]
# and from 1981 to 1996 is [Gen Y]
# and from 1997 to 2012 is [Gen Z]
# and from 2013 to 2024 is [Gen Alpha]
# and from 2025 to 2039 is [Gen Beta]
# at the end print the person's name and generation

print("persons generation indicator program")
print("-------------------------")
number_of_persons = int(input("Enter the number of persons: "))
print("-------------------------")

for item in range(number_of_persons):
    person_name = input("Enter the person's name: ").upper()
    birth_year = int(input("Enter the person's birth year: "))
    print("-------------------------")

    generation = ""
    if birth_year >= 1965 and birth_year <= 1980:
        generation = "Gen X"
    elif birth_year >= 1981 and birth_year <= 1996:
        generation = "Gen Y"
    elif birth_year >= 1997 and birth_year <= 2012:
        generation = "Gen Z"
    elif birth_year >= 2013 and birth_year <= 2024:
        generation = "Gen Alpha"
    elif birth_year >= 2025 and birth_year <= 2039:
        generation = "Gen Beta"
    else:
        generation = "Unknown"

    print(f"Hi {person_name}, your generation is {generation}")
    print("-------------------------")
