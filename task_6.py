# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной
# директории и выводить результаты в консоль.
# Используйте асинхронный подход.

import os
import asyncio
from time import time

MY_PATH = '.'


def count_words_in_file(file_):
    with open(file_, 'r', encoding='utf-8') as f:
        content = f.read()
        num_words = len(content.split())
        print(f'Слов в файле {file_}: {num_words}')


async def process_files_in_directory(directory):
    for file_ in os.listdir(directory):
        file_ = os.path.join(directory, file_)
        if os.path.isfile(file_):
            count_words_in_file(file_)


async def main():
    directory = MY_PATH
    await process_files_in_directory(directory)


if __name__ == '__main__':
    start_time = time()
    asyncio.run(main())
    print(f'Время выполнения: {(time() - start_time):.10f}')