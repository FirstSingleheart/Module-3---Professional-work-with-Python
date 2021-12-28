nested_list = [
    'sam', [['Test', [['one', [], []]], [[u'file.txt', ['id', 1, 0]]], ['Test2', [], [u'file2.txt', ['id', 1, 2]]]], []]
]


def nested_values(nested_dict):
    for item in nested_dict:
        if isinstance(item, list):
            for element in nested_values(item):
                yield element
        else:
            yield item


for item in nested_values(nested_list):
    print(item)