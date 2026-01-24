# build a vowels counter program:
# collect the user's name and a sentence
# loop in every letter of the sentence
# and check if the letter is a vowel "aeiou" and count the number of vowels
# at the end print the number of vowels and the user's name

print("vowels counter program")
print("-------------------------")
user_name = input("Enter your name: ").upper()
sentence = input("Enter a sentence: ").lower()
print("-------------------------")

vowels = "aeiou"
vowels_count = 0
constants_count = 0
for letter in sentence:
    if letter in vowels:
        vowels_count += 1
    else:
        constants_count += 1

print(f"Ok {user_name} There are {vowels_count} vowels in your sentence")
print("-------------------------")
