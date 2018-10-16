from array import Array


class Grid:
    
    def __init__(self, rows, columns, fillValue=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)

    def getHeight(self):
        return len(self._data)

    def getWight(self):
        return len(self._data[0])

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ''
        for row in range(self.getHeight()):
            for col in range(self.getWight()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result


if __name__ == '__main__':
    grid = Grid(5, 4)
    print(grid.getHeight())
    print(grid.getWight())