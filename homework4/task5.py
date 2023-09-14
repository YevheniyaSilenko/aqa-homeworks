names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names:
    # Check if the element is not a string
    if not isinstance(name, str):
        continue  # Skip this iteration if it's not a string
    print(name)
