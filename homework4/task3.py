
programming_languages = { "Python": "Rossum","Java": "Gosling","JavaScript": "Eich", "C++": "Stroustrup"}

# Виводимо повідомлення для кожної пари "мова: розробник"
for language, developer in programming_languages.items():
    print(f"My favorite programming language is {language}. It was created by {developer}.")

# Видаляємо одну пару "мова: розробник"
del programming_languages["Java"]

# Виводимо оновлений словник
print(programming_languages)










