def calculate_even_squares():
    for number in range(0, 1000000001, 2):
        yield number ** 2

if __name__ == '__main__':
    for square in calculate_even_squares():
        print(square)
