class QAEngineer:
    """
    Клас, що представляє QA інженера.
    """

    # Атрибути класу
    _employee_count = 0  # Приватний атрибут, який зберігає кількість QA інженерів

    def __init__(self, name, experience):
        """
        Конструктор класу QAEngineer.

        :param name: Ім'я QA інженера.
        :param experience: Рівень досвіду QA інженера (у роках).
        """
        self._name = name  # Атрибут класу зі змінним доступом (protected)
        self.__experience = experience  # Приватний атрибут

        QAEngineer._employee_count += 1  # Збільшуємо кількість QA інженерів при створенні нового об'єкта

    @property
    def name(self):
        """
        Getter для імені QA інженера.

        :return: Ім'я QA інженера.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter для імені QA інженера.

        :param value: Нове ім'я QA інженера.
        """
        self._name = value

    @staticmethod
    def get_employee_count():
        """
        Статичний метод для отримання загальної кількості QA інженерів.

        :return: Загальна кількість QA інженерів.
        """
        return QAEngineer._employee_count

    def _perform_testing(self, test_case):
        """
        Захищений метод для виконання тестування.

        :param test_case: Назва тестового випробування.
        """
        print(f"{self._name} виконує тестування для '{test_case}'")

    def __str__(self):
        """
        Перевизначений метод для представлення об'єкту як рядка.

        :return: Рядок, що містить ім'я та рівень досвіду QA інженера.
        """
        return f"{self._name}, Досвід: {self.__experience} років"


# Приклад використання класу QAEngineer
if __name__ == "__main__":
    qa1 = QAEngineer("Анна", 5)
    qa2 = QAEngineer("Євгенія", 1)

    print(qa1.name)  # Використовуємо getter
    qa1.name = "Марія"  # Використовуємо setter
    print(qa1.name)

    qa1._perform_testing("Реєстрація")  # Викликаємо захищений метод

    print(qa1)
    print(qa2)

    print("Загальна кількість QA інженерів:", QAEngineer.get_employee_count())



