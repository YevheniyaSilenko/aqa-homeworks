
numbers_str = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

squared_numbers = map(lambda x: int(x)**2, numbers_str)

dict1 = dict(zip(numbers_str, squared_numbers))

print(dict1)
