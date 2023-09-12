# Введення адреси електронної пошти від користувача
email = input("input email: ")

# Перевірка, чи є символ '@' і '.' в адресі
if '@' in email and '.' in email:
    print("YES")
else:
    print("NO")
