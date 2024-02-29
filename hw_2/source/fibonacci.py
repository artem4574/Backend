def fibonacci(n):
    if n == 0: return [0]
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    cube = lambda x: x ** 3

    return list(map(cube, fib_list))


'''
n = int(input("Введите целое число n: "))
cube = lambda x: x ** 3
print(list(map(cube, fibonacci(n))))
'''