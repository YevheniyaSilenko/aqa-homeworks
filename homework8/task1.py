# Створення декоратора для виведення назви функції
def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Викликано функцію: {func.__name__}, Результат: {result}")
        return result
    return wrapper

# Декоруємо функції для додавання та множення
@print_function_name
def add(a, b):
    return a + b

@print_function_name
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    result1 = add(8, 2)
    result2 = multiply(2, 10)
