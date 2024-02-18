import os
import sys


def list_files(directory):
    if not os.path.exists(directory):
        print(f"Директории {directory} не существует.")
        return

    all_items = os.listdir(directory)

    files = [item for item in all_items if os.path.isfile(os.path.join(directory, item))]

    files.sort()

    return files


def group_files_by_extension(files):
    grouped_files = {}

    for file in files:
        _, extension = os.path.splitext(file)
        grouped_files.setdefault(extension, []).append(file)

    return grouped_files


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Пожалуйста, укажите путь к директории в качестве аргумента командной строки.")
    else:
        directory_path = sys.argv[1]

        files_list = list_files(directory_path)

        grouped_files = group_files_by_extension(files_list)

        for extension, file_list in sorted(grouped_files.items()):
            for file in file_list:
                print(file)

# python3 hw_2\source\files_sort.py C:\Users\nrvn2\PycharmProjects\Backend
