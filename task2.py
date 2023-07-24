import types


def flat_generator(list_of_lists:list):
    index1 = 0
    index2 = 0
    lst = list_of_lists
    while True:
        if index2 == len(lst[index1]):
            index2 = 0
            index1 += 1
        if index1 == len(lst):
            break

        yield lst[index1][index2]
        index2 += 1

result = list(flat_generator([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(result)


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()