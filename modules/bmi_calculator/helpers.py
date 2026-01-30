def get_bmi_rate(weight, height):
    return weight / height ** 2

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    else:
        return "Overweight"

def bmi_calculator(username, weight, height):
    bmi = get_bmi_rate(weight, height)
    category = get_bmi_category(bmi)
    return f"{username} Your BMI is {bmi:.2f} and you are {category} person"

