
input_text = input("Введіть текст через пробіл: ")
text_list = input_text.split()

if len(text_list) >= 3:
    # Виведення останніх трьох елементів списку
    last_three_elements = text_list[-3:]
    print("Останні три елементи:", last_three_elements)
else:
    print(f"Кількість елементів менша за 3: {len(text_list)} елементів у списку.")
