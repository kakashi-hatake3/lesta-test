"""
Я реализовал обычную очередь и круговую.
 Первая хранит значения в массиве,
  следовательно доступ к последнему элементу будет быстрее,
   но вторая быстрее удаляет и добавляет элементы,
    поскольку используется связный список.
     Преимущество обычной очередью над круговой заключается в том,
      что в нее можно бесконечно добавлять новые элементы,
       но в этом ее и недостаток, поскольку это занимает очень много памяти.
        В круговой очереди используется выделенная в самом начале память.
"""


class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop() if self.size() != 0 else 'Очередь пуста'

    def size(self):
        return len(self.items)


queue = Queue()
queue.add(111)
queue.add(222)
print(queue.get())
print(queue.get())
print(queue.get())


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.head = self.tail = -1

    def add(self, data):
        if (self.tail + 1) % self.size == self.head:
            print("Максимум элементов\n")

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data

    def get(self):
        if self.head == -1:
            print("Нет элементов\n")

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp

    def size(self):
        return self.size


circ_queue = CircularQueue(4)
circ_queue.add(111)
circ_queue.add(222)
circ_queue.add(333)
circ_queue.add(444)
print(circ_queue.get())
print(circ_queue.get())

