def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


cube = lambda x: x ** 3

n = int(input("Введите целое число n: "))

print(list(map(cube, fibonacci(n))))
