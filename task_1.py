# Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с
# каждого адреса. После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.
import requests
from threading import Thread


def download_data(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


# Список URL адресов
urls = [
    'url1',
    'url2',
    'url3',
    'url4',
    'url5',
    'url6',
    'url7',
    'url8',
    'url9',
    'url10'
]

# Создаем и запускаем потоки для загрузки данных
threads = []
for i, url in enumerate(urls):
    filename = f'data_{i}.txt'
    thread = Thread(target=download_data, args=(url, filename))
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

print('All data downloaded and saved.')