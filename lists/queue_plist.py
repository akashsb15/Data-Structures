class queue(object):
    elements = []

    def myEnqueue(self, val):
        self.elements.append(val)
        return "success - myEnqueue(" + str(val) + ")"

    def myDequeue(self):
        temp = self.elements[0]
        self.elements = self.elements[1:]
        return temp

    def myFront(self):
        return self.elements[0]

    def isEmpty(self):
        return bool(self.mySize())

    def mySize(self):
        return len(self.elements)

myQueue = queue()
print myQueue.isEmpty()
print myQueue.myEnqueue(1)
print myQueue.isEmpty()
print myQueue.mySize()
print myQueue.myEnqueue(2)
print myQueue.myEnqueue(3)
print myQueue.myFront()
print myQueue.myEnqueue(4)
print myQueue.myDequeue()
print myQueue.mySize()
