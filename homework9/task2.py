class QAEngineer:
    """
    A class representing a Quality Assurance (QA) Engineer.

    Attributes:
        name (str): The name of the QA engineer.
        experience (int): The years of experience in QA testing.
        skills (list): A list of technical skills possessed by the QA engineer.

    Methods:
        __init__(self, name, experience, skills): Initializes a new QAEngineer object.
        get_name(self): Returns the name of the QA engineer.
        get_experience(self): Returns the years of experience.
        get_skills(self): Returns the list of technical skills.
        introduce(self): Prints an introduction message about the QA engineer.
    """

    def __init__(self, name, experience, skills):
        """
        Initializes a new QAEngineer object.

        Args:
            name (str): The name of the QA engineer.
            experience (int): The years of experience in QA testing.
            skills (list): A list of technical skills possessed by the QA engineer.
        """
        self.name = name
        self.experience = experience
        self.skills = skills

    def get_name(self):
        """
        Returns the name of the QA engineer.

        Returns:
            str: The name of the QA engineer.
        """
        return self.name

    def get_experience(self):
        """
        Returns the years of experience.

        Returns:
            int: The years of experience in QA testing.
        """
        return self.experience

    def get_skills(self):
        """
        Returns the list of technical skills.

        Returns:
            list: A list of technical skills possessed by the QA engineer.
        """
        return self.skills

    def introduce(self):
        """
        Prints an introduction message about the QA engineer.
        """
        print(f"Hello, I'm {self.name}, a QA Engineer with {self.experience} years of experience.")
        print("My technical skills include:")
        for skill in self.skills:
            print(f"- {skill}")

# Example usage:
if __name__ == "__main__":
    qa_engineer = QAEngineer("Yevheniia", 1, ["Manual Testing", "Automation Testing", "Test Planning"])
    qa_engineer.introduce()

