import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконана за {execution_time:.2f} секунд")
        return result
    return wrapper

# Приклад використання декоратора:
@timing_decorator
def some_function():

    time.sleep(4)  # Приклад затримки на 4 секунди

some_function()
