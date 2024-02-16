input()
scores = set(map(int, input().split()))

print(max([score for score in scores if score != max(scores)]))
