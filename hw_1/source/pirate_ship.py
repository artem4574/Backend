def knapsack_max_value(weights, values, capacity):

    dp = [[0] * (capacity + 1) for _ in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w: dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else: dp[i][w] = dp[i - 1][w]

    result = []
    w = capacity

    for i in range(len(values), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]

    return result


n, capacity = map(int, input().split())
weights, values = [], []

for _ in range(n):
    name, w, v = input().split()
    weights.append(int(w))
    values.append(int(v))

selected_items = knapsack_max_value(weights, values, capacity)

for item in reversed(selected_items):
    w = min(capacity, weights[item])
    v = values[item] * (w / weights[item])
    print(f"{item} {w} {v:.2f}")