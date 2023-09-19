import csv

# Поточний обмінний курс (1 долар = 27 гривень, приклад)
exchange_rate = 27

# Відкриваємо файл "salaries.csv" для читання
with open("/Users/mac/PycharmProjects/aqa-homeworksss/homework6/test_file.csv", "r") as input_file:
    reader = csv.reader(input_file)
    header = next(reader)  # Зчитуємо заголовок

    # Створюємо новий файл "salaries_uah.csv" для запису результату
    with open("salaries_uah.csv", "w", newline='') as output_file:
        writer = csv.writer(output_file)

        # Записуємо заголовок
        writer.writerow(header)

        # Проходимося по рядках файлу та конвертуємо зарплати в гривні
        for row in reader:
            employee_name = row[0]
            salaries_usd = [float(salary) for salary in row[1:]]
            salaries_uah = [salary * exchange_rate for salary in salaries_usd]
            writer.writerow([employee_name] + salaries_uah)

print("Зарплати переведено у гривні та збережено у файлі 'salaries_uah.csv'.")
