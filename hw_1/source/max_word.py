import re


def find_longest_word(filename):

    with open(filename, encoding='utf-8', mode='r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text, flags=re.UNICODE)

    sorted_words = sorted(words, key=len, reverse=True)

    return [word for word in sorted_words if len(word) == len(sorted_words[0])]


for word in find_longest_word('../files/example.txt'): print(word)
