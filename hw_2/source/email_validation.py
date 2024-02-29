import re


def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))


def filter_mail(emails):
    result = list(filter(fun, emails))
    result.sort()
    return result
print(filter_mail(['lara@mospolytech.ru', 'brian-23@mospolytech.ru', 'britts_54@mospolytech.russ']))
'''
n = int(input("Введите количество адресов электронной почты: "))
emails = []

for _ in range(n): emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
'''
'''
lara@mospolytech.
briaн-23@mospolytech.ru
britts_54@mospolytech.russ
'''