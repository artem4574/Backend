while True:
    a = int(input())
    b = int(input())

    try:
        print(a // b)
        print(a / b)
    except ZeroDivisionError:
        print('Type error: division by 0.')
        raise


