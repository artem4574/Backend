n = int(input())
scores = set(map(int, input().split()))

scores = [score for score in scores if score != max(scores)]

print(max(scores))
