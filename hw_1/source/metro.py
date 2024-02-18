n = int(input())
time_list = []

for i in range(n):
    a, b = map(int, input().split())
    time_list.append([a, b])

t = int(input())
count = 0

for i in time_list:
    if i[0] <= t <= i[1]: count+=1

print(count)
