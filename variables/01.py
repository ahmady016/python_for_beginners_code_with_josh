# estimate the traveling flight cost for passengers:
# given the flight ticket price of $200
# and the insurance fee is $600
# and the passport fee is $750
# and the baggage fee is $75
# and the number of people is 5

number_of_people = 5
flight_cost = 200
insurance_cost = 600
passport_cost = 750
baggage_cost = 75

cost_per_person = flight_cost + insurance_cost + passport_cost + baggage_cost
total_cost = cost_per_person * number_of_people

print("cost for passengers")
print("-------------------------")
print("total cost per person:", cost_per_person)
print("total cost:", total_cost)
print("-------------------------")
