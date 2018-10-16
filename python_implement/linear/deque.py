class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.append(0, item)

    def remove_front(self, item):
        self.items.pop()

    def remove_rear(self, item):
        self.items.pop(0)

    def size(self):
        return len(self.items)

from pythonds.basic.deque import Deque

def palchecker(string):
    # 1.将字符串加入队列
    deq = Deque()
    for s in string:
        deq.addRear(s)
    still_equal = True
    while deq.size() >1 and still_equal:
        first = deq.removeFront()
        last = deq.removeRear()
        if first != last:
            still_equal = False
    return still_equal

    # 2.重复首尾出队检查是否回文

if __name__ == '__main__':
    print(palchecker("abcdfeedcba"))