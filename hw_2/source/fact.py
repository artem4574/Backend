import time
import sys
sys.set_int_max_str_digits(1000000)


def fact_rec(n):

    if n in [0, 1]: return 1

    else: return n * fact_rec(n - 1)


def fact_it(n):

    result = 1
    for i in range(1, n + 1): result *= i

    return result


n = int(input())

'''start_time_1 = time.time()
result_rec = fact_rec(n)
end_time_1 = time.time()
print(f"Рекурсивная функция: Результат - {result_rec}, Время выполнения - {end_time_1 - start_time_1} секунд")'''


start_time_2 = time.time()
result_it = fact_it(n)
end_time_2 = time.time()
print(f"Итерационная функция: Результат - {result_it}, Время выполнения - {end_time_2 - start_time_2} секунд")