camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []

for variable in camel_case_list:
    snake_case = ''.join(['_'+c.lower() if c.isupper() else c for c in variable]).lstrip('_')
    snake_case_list.append(snake_case)

print(snake_case_list)

