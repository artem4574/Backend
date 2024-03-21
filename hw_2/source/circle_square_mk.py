import random


def circle_square_mk(r, n):

    count_inside = 0

    for _ in range(n):

        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        distance_squared = x ** 2 + y ** 2

        if distance_squared <= r ** 2:
            count_inside += 1

    return int(count_inside / n * (2 * r) ** 2)

print(circle_square_mk(2, 3000000))
'''radius = 5

experiments = [10, 100, 1000, 10000, 100000]

for n in experiments:
    monte_carlo_square = circle_square_mk(radius, n)
    formula_square = 3.14159 * radius**2
    error = abs(formula_square - monte_carlo_square)

    print(f"Кол-во кспериментов: {n}, S окружности (м.Монте-Карло): {monte_carlo_square:.4f}, "
          f"S окружности (по формуле): {formula_square: .4f}, Погрешность: {error: .4f}")
'''