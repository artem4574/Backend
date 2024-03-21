import os
import sys


def search_file_recursive(target_file, current_directory="."):
    try:
        for root, dirs, files in os.walk(current_directory):
            if target_file in files:
                file_path = os.path.join(root, target_file)
                with open(file_path, 'r') as file:

                    for _ in range(5): print(file.readline().strip())

                return True
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False


if __name__ == "__main__":

    if len(sys.argv) != 2: print("Enter filename:")
    else:
        file_name = sys.argv[1]

        current_directory = os.path.dirname(os.path.realpath(__file__))

        file_found = search_file_recursive(file_name, current_directory)

        if file_found: print(f"Файл {file_name} найден.")

        else: print(f"Файл {file_name} не найден.")
