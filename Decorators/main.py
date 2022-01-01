from datetime import datetime


logs_path = "logs.txt"


def decoration(path):
    def write_logs(function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            func_name = function.__name__
            result = function(*args, **kwargs)
            with open('logs.txt', 'a', encoding='utf-8') as file:
                file.write(f'Date/time creating: {date_time}\n'
                           f'function name: {func_name}\n'
                           f'Arguments: {args}, {kwargs}\n'
                           f'Result: {result}\n'
                           f'{"*" * 50}\n')
            return result
        return new_function
    return write_logs


if __name__ == '__main__':

    @ decoration(logs_path)
    def factorial(a):
        if a == 1:
            return a
        else:
            next_meaning = a - 1
        return a * factorial(next_meaning)

    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))