
import os

# сканування папки
def scan_directory(directory):
    file_sizes = {}  # Словник для збереження інформації про файли (назва: розмір)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes[file_path] = file_size

    return file_sizes

# Головна функція
def main():
    root_directory = "/Users/mac/PycharmProjects/aqa-homeworksss/homework6"
    file_sizes = scan_directory(root_directory)

    # Зберігаємо інформацію про файли
    with open("files_size.txt", "w") as file:
        for file_path, file_size in file_sizes.items():
            file.write(f"{file_path}: {file_size} bytes\n")

    # Знаходимо найбільший файл та його розмір
    largest_file = max(file_sizes, key=file_sizes.get)
    largest_file_size = file_sizes[largest_file]

    print(f"Найбільший файл: {largest_file}")
    print(f"Розмір найбільшого файлу: {largest_file_size} bytes")

if __name__ == "__main__":
        main()

