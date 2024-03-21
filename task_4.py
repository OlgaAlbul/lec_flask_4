# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной
# директории и выводить результаты в консоль.
# Используйте потоки.
import threading
import os
from time import time

MY_PATH = '.'


def count_words_in_file(file_):
    with open(file_, 'r', encoding='utf-8') as f:
        content = f.read()
        num_words = len(content.split())
        print(f'Слов в файле {file_}: {num_words}')


def process_files_in_directory(directory):
    threads = []

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            t = threading.Thread(target=count_words_in_file, args=(file_path,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    start_time = time()
    process_files_in_directory(MY_PATH)
    print(f'Execution time: {(time() - start_time):.3f} seconds')