from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class ListIterator:
    def __init__(self, iter_list: list):
        self.new_list = [element for element in chain.from_iterable(iter_list)]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]


flat_list = [item for item in ListIterator(nested_list)]
print(flat_list)

for item in ListIterator(nested_list):
    print(item)


