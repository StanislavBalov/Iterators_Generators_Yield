class FlatIterator:
    def __init__(self, list_of_list):
        self.stack = [iter(list_of_list)]
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                self.current = next(self.stack[-1])
                if isinstance(self.current, list):
                    self.stack.append(iter(self.current))
                else:
                    return self.current
            except StopIteration:
                self.stack.pop()
        raise StopIteration

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_3()