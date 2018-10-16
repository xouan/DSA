
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
           
    def size(self):
        return len(self.items)
    


def hot_patato(name_list, num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        print(q.dequeue())
    print('end')
    return q.dequeue()

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.pagerate

class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)
    
    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, curent_time):
        return curent_time - self.time_stamp

if __name__ == "__main__":
    print(hot_patato(['bill', 'david', 'susan', 'jane', 'kent', 'brad'], 2))
