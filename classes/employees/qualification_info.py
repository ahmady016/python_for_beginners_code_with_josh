class QualificationInfo:
    def __init__(self, grade_name, grade_year, grade_percentage):
        self.grade_name = grade_name
        self.grade_year = grade_year
        self.grade_percentage = grade_percentage

    def __str__(self):
        return f"Grade: {self.grade_name}, Year: {self.grade_year}, Percentage: {self.grade_percentage}"
    def __repr__(self):
        return f"Qualification('{self.grade_name}', {self.grade_year}, {self.grade_percentage})"
