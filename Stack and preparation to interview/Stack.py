from pprint import pprint

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
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def check_list(list_: list):
    open_stack = Stack()
    closing_stack = Stack()
    for string_ in list_:
        for item_ in string_:
            if item_ in ['([{']:
                open_stack.push(item_)
            elif item_ in [')]}']:
                closing_stack.push(item_)
        if open_stack.size == closing_stack.size:
            print("Сбалансированно")
        print("Несбалансированно")


if __name__ == '__main__':
    check_list(checking_list)