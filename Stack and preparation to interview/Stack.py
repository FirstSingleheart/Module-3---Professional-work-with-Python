from pprint import pprint
from typing import Any

checking_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item: Any):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def check_dict(list_: list):
    open_list = ['(', '[', '{']
    close_list = [')', ']', '}']
    open_stack = Stack
    closing_stack = Stack
    for string_ in list_:
        for item in string_:
            if item in open_list:
                open_stack.push(item)
            elif item in close_list:
                closing_stack.push(item)
            if open_stack.is_empty == closing_stack.is_empty:
                return "Сбалансированно"
            return "Несбалансированно"


if __name__ == '__main__':
    pprint(check_dict(checking_list))