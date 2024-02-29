n, m = map(int, input().split())

tovars = {}

for _ in range(m):
    key, weight, value = input().split()
    tovars[key] = [int(value) / int(weight), int(weight)]

tovars = dict(sorted(tovars.items(), key=lambda x: x[1][0], reverse=True))

free = n
space = 0

for key, value in tovars.items():
    price = value[0] * value[1]
    selected_quantity = min(free, value[1])
    print(key, selected_quantity, round(selected_quantity * value[0], 2))
    free -= selected_quantity
    space += value[1]

    if free == 0:
        break
