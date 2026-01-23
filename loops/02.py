# build the first 3 people to got the 25% discount
# for every person collect the user's name
# and print "congrats {user_name} you got the 25% discount"
# once all three people are gotten the 25% discount print "all done"

print("first 3 people catcher")
print("-------------------------")

count = 1
while count < 4:
    user_name = input(f"Enter the name of person#{count}: ").upper()
    print(f"congrats {user_name} you got the 25% discount")
    count += 1

print("all done")
print("-------------------------")
