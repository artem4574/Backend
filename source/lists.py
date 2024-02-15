n = int(input())
array = []

for _ in range(n):

    command = input().split()

    match(command[0]):

        case "insert": array.insert(int(command[1]), int(command[2]))
        case "print": print(array)
        case "remove": array.remove(int(command[1]))
        case "append": array.append(int(command[1]))
        case "sort": array.sort()
        case "pop": array.pop()
        case"reverse": array.reverse()
