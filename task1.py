class FlatIterator:

    def __init__(self, list_of_list:list):
        self.lst = list_of_list

    def __iter__(self):
        self.index1 = 0
        self.index2 = -1
        return self

    def __next__(self):
        if self.index2 == len(self.lst[self.index1]) - 1:
            self.index1 += 1
            self.index2 = -1
        if self.index1 == len(self.lst):
            raise StopIteration
        self.index2 += 1
        
        return self.lst[self.index1][self.index2]
    
result = list(FlatIterator([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(result)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()