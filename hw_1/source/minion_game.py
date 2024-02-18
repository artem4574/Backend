def minion_game(s):

    vowels = "AEIOU"
    kevin_score, stuart_score = 0, 0

    for i in range(len(s)):

        if s[i] in vowels: kevin_score += len(s) - i

        else: stuart_score += len(s) - i

    if kevin_score > stuart_score: return f"Кевин {kevin_score}"

    elif kevin_score < stuart_score: return f"Стюарт {stuart_score}"

    else: return "Draw"


print(minion_game(input()))
