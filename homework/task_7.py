import asyncio
import multiprocessing
from random import randint
from threading import Thread
import time

arr = [randint(1, 100) for _ in range(10000)]
sum_arr = 0
sum_mult = multiprocessing.Value('i', 0)
processes = []
num_operations = int(len(arr) // 100)


def sum_array_threads(start_idx, stop_idx):
    global sum_arr
    for i in range(start_idx, stop_idx):
        sum_arr += arr[i]


def threadings_calc():
    start_time = time.time()
    threads = []
    for i in range(num_operations):
        start_idx = i * len(arr) // num_operations
        stop_idx = (i + 1) * len(arr) // num_operations
        thread = Thread(target=sum_array_threads, args=(start_idx, stop_idx))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    with open("thread_result.txt", "w", encoding='utf-8') as file:
        file.write(f"Время многопоточного исполнения: {time.time() - start_time:.2f} секунд\nрезультат: {sum_arr}")


def sum_array_mult(arr, start_idx, end_idx, sum_):
    local_sum = 0
    for i in range(start_idx, end_idx):
        local_sum += arr[i]
    with sum_.get_lock():
        sum_.value += local_sum


def multy_summ():
    start_time = time.time()
    for i in range(num_operations):
        start_idx = i * len(arr) // num_operations
        end_idx = (i + 1) * len(arr) // num_operations
        process = multiprocessing.Process(target=sum_array_mult, args=(arr, start_idx, end_idx, sum_mult))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    with open("process_result.txt", "w", encoding='utf-8') as file:
        file.write(f"Время многопроцессорного исполнения: {time.time() - start_time:.2f} секунд\nрезультат: {sum_arr}")


async def sum_array_async(arr, start_idx, stop_idx):
    temp_sum_arr = 0
    for i in range(start_idx, stop_idx):
        temp_sum_arr += arr[i]


async def async_calc():
    global sum_arr
    start_time = time.time()
    tasks = []
    num_tasks = num_operations
    start_time = time.time()
    for i in range(num_tasks):
        start_idx = i * len(arr) // num_tasks
        end_idx = (i + 1) * len(arr) // num_tasks
        task = asyncio.create_task(sum_array_async(arr, start_idx, end_idx))
        tasks.append(task)
    await asyncio.gather(*tasks)
    with open("async_result.txt", "w", encoding='utf-8') as file:
        file.write(f"Время асинхронного выполнения: {time.time() - start_time:.2f} секунд\nрезультат: {sum_arr}")


if __name__ == '__main__':
    threadings_calc()
    asyncio.run(async_calc())
    multy_summ()
    print(num_operations)
