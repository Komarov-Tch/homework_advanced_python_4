class FlatIterator:
    """
    The class is an iterator for nested lists.
    Flattern method removes list nesting
    """

    def __init__(self, nested_list):
        self.n_list = self.flattern(nested_list)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.n_list):
            self.result = self.n_list[self.count]
            self.count += 1
            return self.result
        else:
            raise StopIteration

    def flattern(self, nested_list):
        flatted_list = []
        for obj in nested_list:
            if isinstance(obj, (list, tuple)):
                flatted_list.extend(self.flattern(obj))
            else:
                flatted_list.append(obj)
        return flatted_list


def flat_generator(nest_list):
    for item in nest_list:
        if isinstance(item, (tuple, list)):
            for x in flat_generator(item):
                yield x
        else:
            yield item


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False, [1, 2, 3, 4, 5]],
    [1, 2, None]
]
print('-' * 10, 'работа через итератор', '-' * 10)
for item in FlatIterator(nested_list):
    print(item)
print('-' * 10, 'работа через генератор', '-' * 10)
for item in flat_generator(nested_list):
    print(item)
