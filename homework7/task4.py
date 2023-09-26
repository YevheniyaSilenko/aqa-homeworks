def custom_map(callback, iterable):
    result = []
    for item in iterable:
        result.append(callback(item))
    return result

# Приклад callback-функції:
def square(x):
    return x ** 2

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = custom_map(square, data)
    print(result)
