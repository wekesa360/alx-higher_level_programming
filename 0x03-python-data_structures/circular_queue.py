# Circular Queue implementation in python

class myCircular_queue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] *k
        self.head = self.tail = -1

    #Insert an elemnet into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1)
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.]