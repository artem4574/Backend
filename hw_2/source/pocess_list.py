import time


def process_list(arr):
    return [i ** 2 if i % 2 == 0 else i ** 3 for i in arr]


def process_list_gen(arr):
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3


test_array = list(range(1, 1000001))


start_time_1 = time.time()
result_list_comp = process_list(test_array)
end_time_1 = time.time()
print(f"List comprehension: Время выполнения - {end_time_1 - start_time_1} секунд")


start_time_2 = time.time()
result_gen = list(process_list_gen(test_array))
end_time_2 = time.time()
print(f"Generator function: Время выполнения - {end_time_2 - start_time_2} секунд")
