from typing import Any


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class ListIterator:
    def __init__(self, iter_list):
        self.iter_list = iter_list

    def __iter__(self):
        self.global_list_cursor = -1
        self.cursor = -1
        return self

    def __next__(self):
        if self.global_list_cursor != len(self.iter_list):
            self.global_list_cursor += 1
            for item in self.iter_list:
                if self.cursor != len(self.iter_list[self.global_list_cursor]):
                    self.cursor += 1
        if self.iter_list.cursor == len(self.iter_list) and len(self.iter_list[self.cursor]) == self.cursor:
            raise StopIteration
        return self.iter_list[self.global_list_cursor][self.cursor]


for item in ListIterator(nested_list):
    print(item)