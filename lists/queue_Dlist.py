from DList_tail import *

class queue(object):

    elements = doublyList()

    def myEnqueue(self, val):
        return self.elements.pushBack(val)

    def myDequeue(self):
        return self.elements.popFront()

    def myFront(self):
        return self.elements.topFront()

    def isEmpty(self):
        return self.elements.empty()

    def mySize(self):
        return len(self.elements.traverse())



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
