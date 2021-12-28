nested_list = [
    'sam', [['Test', [['one', [], []]], [[u'file.txt', ['id', 1, 0]]], ['Test2', [], [u'file2.txt', ['id', 1, 2]]]], []]
]


class ListIterator:

    def __init__(self, my_list):
        self.list = my_list

    def __iter__(self):
        self.iter_List = [iter(self.list)]
        return self

    def __next__(self):
        while len(self.iter_List):
            try:
                value = next(self.iter_List[-1])
            except StopIteration:
                self.iter_List.pop()
                continue
            if isinstance(value, list):
                self.iter_List.append(iter(value))
                continue
            else:
                return value
        raise StopIteration


for item in ListIterator(nested_list):
    print(item)
