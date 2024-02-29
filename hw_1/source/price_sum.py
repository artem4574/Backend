import csv


def calculate_total_expenses(filename):

    adult_expenses, pensioner_expenses, child_expenses = 0, 0, 0

    with open(filename, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=";")
        header = next(reader)

        for row in reader:
            adult_expenses += float(row[1])
            pensioner_expenses += float(row[2])
            child_expenses += float(row[3])

    return adult_expenses, pensioner_expenses, child_expenses


result = calculate_total_expenses('../files/products.csv')

print(round(result[0], 2),  round(result[1], 2),  round(result[2], 2))
