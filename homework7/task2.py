import math

def square(side):
    # Обчислюємо периметр квадрата
    perimeter = 4 * side

    # Обчислюємо площу квадрата
    area = side ** 2

    diagonal = math.sqrt(2) * side

    return perimeter, area, diagonal

# Приклад використання:
side_length = 5
result = square(side_length)
print(f"Периметр квадрата: {result[0]}")
print(f"Площа квадрата: {result[1]}")
print(f"Діагональ квадрата: {result[2]}")
