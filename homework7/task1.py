def sum_range(start, end):

    if start > end:
        start, end = end, start

    total = 0

    for i in range(start, end + 1):
        total += i

    return total

# Приклад використання:
start = 7
end = 20
result = sum_range(start, end)
print(f"Сума чисел від {start} до {end} включно: {result}")
