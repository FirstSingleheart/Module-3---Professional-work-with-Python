def calculate_salary():
    name = input(f'Введите имя работника: ')
    hours = float(input(f'Введите количество отработанных {name} часов: '))
    summa = float(input(f'Введите размер оплаты труда {name} за 1 час: '))
    bonus = float(input(f'Укажите прочие денежные бонусы {name} (если есть): '))
    pay = hours * summa
    all_sum = pay + bonus
    return f'Размер заработной платы {name} за месяц составил: {all_sum}'

