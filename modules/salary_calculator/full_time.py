def full_time_salary(basic_salary, years_of_experience):
    if years_of_experience > 10:
        return (basic_salary * 3) + 3000
    elif years_of_experience >= 5 and years_of_experience <= 10:
        return (basic_salary * 2) + 2000
    elif years_of_experience >= 2 and years_of_experience <= 4:
        return (basic_salary * 1.5) + 1000
    else:
        return basic_salary + 500
