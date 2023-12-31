class Вагон:
    def __init__(self, номер):
        self.номер = номер
        self.пасажири = []

    def додати_пасажира(self, пасажир):
        if len(self.пасажири) < 10:
            self.пасажири.append(пасажир)

    def __len__(self):
        return len(self.пасажири)

    def __str__(self):
        return f"[{self.номер}]"


class Поїзд:
    def __init__(self):
        self.вагони = []

    def додати_вагон(self, вагон):
        self.вагони.append(вагон)

    def __len__(self):
        return len(self.вагони) - 1  # Віднімаємо 1, щоб відобразити кількість вагонів без локомотива

    def __str__(self):
        вагони_строка = "-".join(str(вагон) for вагон in self.вагони)
        return f"<=[HEAD]-{вагони_строка}"

# Приклад використання:
поїзд = Поїзд()
поїзд.додати_вагон(Вагон(1))
поїзд.додати_вагон(Вагон(2))
поїзд.додати_вагон(Вагон(3))

вагон4 = Вагон(4)
вагон4.додати_пасажира("Пасажир 1")
вагон4.додати_пасажира("Пасажир 2")
поїзд.додати_вагон(вагон4)

print(поїзд)  # Виведе: "<=[HEAD]-[1]-[2]-[3]-[4]"
