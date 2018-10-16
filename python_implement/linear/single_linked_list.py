class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def append(self, item):
        if not self.head:
            self.head = Node(item)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(item)

    def insert(self, item):
        pass

    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        if previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next)

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    
    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


if __name__ == "__main__":
    link = SingleLinkedList()
    link.append(10)
    print(link.head.data)

