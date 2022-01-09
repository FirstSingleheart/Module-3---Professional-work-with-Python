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


def check_list(my_list: list):
    for sublist in my_list:
        open_list = ['(', '[', '{']
        closing_list = [')', ']', '}']
        stack = Stack()
        flag = 0
        for elem in sublist:
            if elem in open_list:
                stack.push(elem)
            elif elem in closing_list:
                position = closing_list.index(elem)
                if stack.size() > 0 and open_list[position] == stack.peek():
                    stack.pop()
                else:
                    flag = 1
                    break
        if stack.size() == 0 and flag != 1:
            print('Cбалансированный')
        else:
            print('Несбалансированный')


if __name__ == '__main__':
    check_list(checking_list)