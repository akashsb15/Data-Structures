class stack(object):
    elements = []

    def myPush(self, val):
        self.elements.append(val)

        return "success - myPush(" + str(val) + ")"

    def myPop(self):
        top = self.elements.pop()

        return top

    def myTop(self):
        return self.elements[-1]

    def isEmpty(self):
        if not self.mySize():
            return True
        return False

    def mySize(self):
        return len(self.elements)



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


