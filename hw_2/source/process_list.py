import time


def process_list(arr):
    return [i ** 2 if i % 2 == 0 else i ** 3 for i in arr]


def process_list_gen(arr):
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3
'''
test_array = list(range(7))


start_time_1 = time.time()
result_list_comp = process_list(test_array)
end_time_1 = time.time()
print(f"List comprehension: Время выполнения - {end_time_1 - start_time_1} секунд")


start_time_2 = time.time()
result_gen = list(process_list_gen(test_array))
end_time_2 = time.time()
print(result_gen)
print(f"Generator function: Время выполнения - {end_time_2 - start_time_2} секунд")

#List comprehension: Время выполнения - 0.10100126266479492 секунд
#Generator function: Время выполнения - 0.1179955005645752 секунд'''