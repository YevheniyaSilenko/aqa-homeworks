class QAEngineer:
    def __init__(self, name, years_of_experience, skills):
        self.name = name
        self.years_of_experience = years_of_experience
        self.skills = skills

    def __str__(self):
        return f"QA Engineer: {self.name}\nYears of Experience: {self.years_of_experience}\nSkills: {', '.join(self.skills)}"

# Usage:
qa_engineer = QAEngineer("Yevheniia Silenko", 1, ["Manual Testing", "Automated Testing", "Test Case Design"])
print(qa_engineer)

