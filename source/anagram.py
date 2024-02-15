def is_permutation(str1, str2):

    if len(str1) != len(str2): return "NO"

    if sorted(str1) == sorted(str2): return "YES"

    else: return "NO"


print(is_permutation(input(), input()))