from typing import Any


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(my_list: list):
    new_list = [element for item in my_list for element in item]
    return new_list


for item in flat_generator(nested_list):
    print(item)



