class Ferrari:
    """
    This class represents the Ferrari company.
    """

    # Class attribute
    _total_ferraris = 0  # Hidden attribute

    def __init__(self, model, year, color):
        """
        Initialize a Ferrari object.

        :param model: The model of the Ferrari.
        :param year: The manufacturing year of the Ferrari.
        :param color: The color of the Ferrari.
        """
        self._model = model  # Protected attribute
        self._year = year    # Protected attribute
        self._color = color  # Protected attribute
        Ferrari._total_ferraris += 1  # Increment the total Ferrari count

    @property
    def model(self):
        """
        Get the model of the Ferrari.

        :return: The model of the Ferrari.
        """
        return self._model

    @model.setter
    def model(self, new_model):
        """
        Set the model of the Ferrari.

        :param new_model: The new model to set.
        """
        self._model = new_model

    def get_year(self):
        """
        Get the manufacturing year of the Ferrari.

        :return: The manufacturing year of the Ferrari.
        """
        return self._year

    def set_year(self, new_year):
        """
        Set the manufacturing year of the Ferrari.

        :param new_year: The new manufacturing year to set.
        """
        self._year = new_year

    @staticmethod
    def get_total_ferraris():
        """
        Get the total number of Ferrari objects created.

        :return: The total number of Ferrari objects.
        """
        return Ferrari._total_ferraris

    def __str__(self):
        """
        Return a string representation of the Ferrari.

        :return: A string describing the Ferrari.
        """
        return f"A {self._color} Ferrari {self._model} manufactured in {self._year}"

# Example usage:
if __name__ == "__main__":
    ferrari1 = Ferrari("488 GTB", 2023, "Red")
    ferrari2 = Ferrari("F8 Tributo", 2022, "Yellow")

    print(ferrari1)
    print(ferrari2)

    ferrari1.model = "812 Superfast"
    ferrari1.set_year(2024)

    print(ferrari1)

    print(f"Total Ferrari cars created: {Ferrari.get_total_ferraris()}"
