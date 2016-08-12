'''
Stack implementation with Doubly Linked lists
'''
from DList_tail import *

class stack(object):
    elements = doublyList()

    def myPush(self, val):
        self.elements.pushBack(val)

    def myTop(self):
        self.elements.topBack()

    def myPop(self):
        self.elements.popBack()

    def mySize(self):
        if self.elements.empty():
            return 0
        return len(self.elements.traverse())

    def isEmpty(self):
        return self.elements.empty()


##myStack = stack()
##print myStack.isEmpty()
##print myStack.myPush(1)
##print myStack.isEmpty()
##print myStack.mySize()
##print myStack.myPush(2)
##print myStack.myPush(3)
##print myStack.myTop()
##print myStack.myPush(4)
##print myStack.myPop()
##print myStack.mySize()
