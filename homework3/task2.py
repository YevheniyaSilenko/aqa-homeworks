# Введення тексту від користувача
text = input("input text: ")

# Введення слова, яке потрібно знайти
word = input("input word : ")

# Перевірка, чи міститься слово в тексті
if word in text:
    print("YES")
else:
    print("NO")
