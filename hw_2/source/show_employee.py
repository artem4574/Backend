def show_employee(name, salary=None):
    return f"{name}: {100000 if salary is None else salary} ₽"


print(show_employee("Иванов Петр Иванович"))