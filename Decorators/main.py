import time
from datetime import datetime
import json


'''
Написать декоратор из п.1, но с параметром – путь к логам.
Применить написанный логгер к приложению из любого предыдущего д/з'''


def write_logs(function):
    def new_function(*args, **kwargs):
        date_time = datetime.now()
        func_name = function.__name__
        result = function(*args, **kwargs)
        with open('logs.json', 'w+', encoding='utf-8') as file:
            file.write(f'Date/time creating: {date_time}\n'
                       f'function name: {func_name}\n'
                       f'Arguments: {args}, {kwargs}\n'
                       f'Result: {result}\n'
                       f'{"*" * 100}')
        return result
    return new_function


if __name__ == '__main__':
    @ write_logs
    def factorial(a):
        if a == 1:
            return a
        else:
            next_meaning = a - 1
        return a * factorial(next_meaning)

    print(factorial(56))