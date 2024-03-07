def av_score(scores):

    av_score = [0.0] * len(scores[0])

    for sub_score in scores:
        for i in range(len(scores[0])):
            av_score[i] += sub_score[i]

    av_score = [round(score / len(scores), 1) for score in av_score]

    return tuple(av_score)


n, x = map(int, input().split())
input_scores = []
for _ in range(x):
    sub_score = list(map(float, input().split()))
    input_scores.append(sub_score)

answer = av_score(input_scores)
for avg_score in answer: print(avg_score)