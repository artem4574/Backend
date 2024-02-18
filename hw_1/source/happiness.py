n, m = map(int, input().split())
array = list(input().split())

set_a = {element for element in input()}
set_b = {element for element in input()}

happiness = 0

for i in array:
    if i in set_a: happiness += 1
    if i in set_b: happiness -= 1

print(happiness)
