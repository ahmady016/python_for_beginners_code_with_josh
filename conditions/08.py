# build a customer reviewer program:
# collect the user's name and review rate from 1 to 10
# check if the review rate is 8 or more give him thank you very much message
# and if the review rate is between 5 and 7 ask him how we can improve
# and print what he said and say "we will work hard to improve"
# and if the review rate is less than 5 print "we are sorry to hear that"

print("customer reviewer program")
print("----------------------------")
user_name = input("Enter your name: ").upper()
review_rate = int(input("Enter your review rate from 1 to 10: "))
print("----------------------------")

if review_rate >= 8:
    print(f"Thank you very much {user_name}")
elif review_rate >= 5 and review_rate <= 7:
    review = input("How can we improve? ")
    print(f"{review}\n we will work hard to improve")
else:
    print(f"we are sorry to hear that {user_name}")

print("----------------------------")
