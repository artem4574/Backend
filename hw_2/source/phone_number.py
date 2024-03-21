def format_phone_number(number):

    formatted_number = "Wrong number"

    if len(number) == 10:

        formatted_number = f"+7 ({number[:3]}) {number[3:6]}-{number[6:8]}-{number[8:]}"

    elif len(number) == 11 and (number[0] == '8' or number[0] == '0'):

        formatted_number = f"+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:]}"

    elif len(number) == 11 and number[0] == '7':

        formatted_number = f"+{number[:1]} ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:]}"

    return formatted_number


def sort_phone(arr):
    return sorted([format_phone_number(i) for i in arr])


if __name__ == '__main__':
    list_phones = [input() for _ in range(int(input()))]
    print(sort_phone(list_phones), sep='\n')
