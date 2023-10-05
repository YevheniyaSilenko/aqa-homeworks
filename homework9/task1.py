class KoboCompany:
    """
    A class representing the Kobo company.

    Kobo is a company that specializes in e-readers and e-books.

    Attributes:
        name (str): The name of the company.
        headquarters (str): The location of the company's headquarters.
        founder (str): The name of the company's founder.
        year_founded (int): The year the company was founded.
    """

    def __init__(self, name, headquarters, founder, year_founded):
        """
        Initialize a KoboCompany instance.

        Args:
            name (str): The name of the company.
            headquarters (str): The location of the company's headquarters.
            founder (str): The name of the company's founder.
            year_founded (int): The year the company was founded.
        """
        self.name = name
        self.headquarters = headquarters
        self.founder = founder
        self.year_founded = year_founded

    def get_name(self):
        """
        Get the name of the company.

        Returns:
            str: The name of the company.
        """
        return self.name

    def get_headquarters(self):
        """
        Get the location of the company's headquarters.

        Returns:
            str: The headquarters of the company.
        """
        return self.headquarters

    def get_founder(self):
        """
        Get the name of the company's founder.

        Returns:
            str: The name of the founder.
        """
        return self.founder

    def get_year_founded(self):
        """
        Get the year the company was founded.

        Returns:
            int: The year the company was founded.
        """
        return self.year_founded

# Example usage:
if __name__ == "__main__":
    kobo = KoboCompany("Kobo Inc.", "Toronto, Canada", "Michael Serbinis", 2009)
    print("Company Name:", kobo.get_name())
    print("Headquarters:", kobo.get_headquarters())
    print("Founder:", kobo.get_founder())
    print("Year Founded:", kobo.get_year_founded())
