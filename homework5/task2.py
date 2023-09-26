
attempts = 3

while attempts > 0:
    try:
        formula = input("Введіть формулу (наприклад, 2 * 5): ")
        num1, operator, num2 = formula.split()

        num1 = float(num1)
        num2 = float(num2)

        if operator not in ('*', '/'):
            raise WrongOperatorError("Підтримуються лише оператори '*' та '/'")

        if operator == '/' and num2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")

        result = num1 * num2 if operator == '*' else num1 / num2
        print(f"Результат: {result:.2f}")
    except ValueError:
        print("Помилка перетворення на число")
    except FormulaError as e:
        print(f"Помилка у формулі: {e}")
    except WrongOperatorError as e:
        print(f"Помилковий оператор: {e}")
    except ZeroDivisionError:
        print("Ділення на нуль неможливе")
    else:
        attempts = 3
    finally:
        print(f"Спроб залишилося: {attempts}")
        attempts -= 1

if attempts == 0:
    print("Ви використали всі спроби. Програма завершила роботу.")
