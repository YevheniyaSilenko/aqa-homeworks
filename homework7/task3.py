def display_box(width: int, height: int, character="*"):
    if width <= 0 or height <= 0:
        print("Неприпустимі розміри прямокутника.")
        return

    for i in range(height):
        if i == 0 or i == height - 1:
            # Верхня і нижня лінії прямокутника
            print(character * width)
        else:
            # Бічні стінки прямокутника з пробілами усередині
            print(character + " " * (width - 2) + character)

# Приклад використання:
display_box(11, 24, 'x')
