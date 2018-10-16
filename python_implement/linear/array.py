class Array:
    """Reprensents an array"""

    def __init__(self, capacity, fillValue=None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, newValue):
        self._items[index] = newValue


if __name__ == '__main__':
    a = Array(5)
    len(a)
    print(a)
    for i in range(len(a)):
        a[i] = i + 1
    for item in a:
        print(item)
