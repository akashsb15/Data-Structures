'''
This implementation of Linked Lists uses two pointers, head and tail, as
a result of which the time complexity of certain functions, to be specific 
popBack() and topBack() are better than when using a single pointer (head). 
'''

class Node(object):
    key = 0
    next = None

    def __init__(self, key):
        self.key = key

class linkedList(object):
    head = None
    tail = None

    # Pushes a new node to the front of the linked list. Time complexity - O(1)
    def pushFront(self, key):
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode

        if self.tail == None:
            self.tail = self.head

        return "success - " + "pushFront(" + str(key) + ")"

    # Returns the front node of the linked list. Time complexity - O(1)
    def topFront(self):
        if self.head:
            return self.head.key
        
        return "empty - topFront()"

    # Pops the front node of the linked list. Time complexity - O(1)
    def popFront(self):
        if not self.head:
            return "empty - popFront()"
        
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return "success - popFront()"

    # Pushes a new node to the back of the linked list. Time complexity - O(1)
    def pushBack(self, key):
        newNode = Node(key)
        
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return "success - " + "pushBack(" + str(key) + ")"
    
        self.tail.next = newNode
        self.tail = newNode

        return "success - " + "pushBack(" + str(key) + ")"

    # Returns the back of the linked list. Time complexity - O(1)
    def topBack(self):
        if self.tail:
            return self.tail.key

        return "empty - topBack()"

    # Pops the back of the linked list. Time complexity - O(n)
    def popBack(self):
        if self.head:
            temp = self.head

            while temp and temp.next is not self.tail:
                temp = temp.next

            if not temp:
                self.head = None
                self.tail = None
                return "success - popBack()"

            temp.next = None
            self.tail = temp

            return "success - popBack()"
        return "empty - popBack()" 

    # Erases the node containing the specified key. Time complexity - O(n)
    def erase(self, key):
        if not self.head:
            return "empty - erase()"

        elif self.head.key == key:
            return self.popFront()

        elif self.tail.key == key:
            return self.popBack()

        else:
            previous = self.head
            current = self.head.next

            while current:
                if current.key == key:
                    previous.next = current.next
                    return "success - erase(" + str(key) + ")"
                previous = current
                current = current.next

            return "key not in list - erase(" +str(key)+ ")"

    # Determines whether the linked list empty. Time complexity - O(1)
    def empty(self):
        if not self.head:
            return True
        return False

    # Adds a new node with key2 before an existing node with key1. Time complexity - O(n)
    def addBefore(self, key1, key2):
        if not self.head:
            return "empty - addBefore()"

        elif self.head.key == key1:
            return self.pushFront(key2)+ " - addBefore(" + str(key1) + ", " + str(key2) + ")"

        else:
            previous = self.head
            current = self.head.next

            newNode = Node(key2)
            while current:
                if current.key == key1:
                    previous.next = newNode
                    newNode.next = current
                    return "success - addBefore(" + str(key1) + ", " + str(key2) + ")"
                previous = current
                current = current.next

            return "key not in list - addBefore(" +str(key1)+ ")"

    # Adds a new node with key2 after an existing node with key1. Time complexity - O(n)
    def addAfter(self, key1, key2):
        if not self.head:
            return "empty - addAfter()"

        elif self.tail.key == key1:
            return self.pushBack(key2) + " - addAfter(" + str(key1) + ", " + str(key2) + ")"

        else:
            current = self.head

            newNode = Node(key2)
            while current:
                if current.key == key1:
                    newNode.next = current.next
                    current.next = newNode
                    return "success - addAfter(" + str(key1) + ", " + str(key2) + ")"
                current = current.next

            return "key not in list - addAfter(" +str(key1)+ ")"

    # Traverses through the linked list. Time complexity - O(n)
    def traverse(self):
        if not self.head:
            return "empty - traverse()"

        temp = self.head
        result = []
        while temp:
            result.append(temp.key)
            temp = temp.next

        return result
            


##Test cases
##newList = linkedList()
##print newList.popBack()
##print newList.popFront()
##print newList.pushBack(1)
##print newList.pushBack(2)
##print newList.pushBack(3)
##print newList.pushBack(4)
##print newList.pushFront(0)
##print newList.pushFront(-1)
##print newList.traverse()
##print newList.popBack()
##print newList.traverse()
##print newList.popFront()
##print newList.traverse()
##print newList.erase(5)
##print newList.traverse()
##print newList.addBefore(0,10)
##print newList.traverse()
##print newList.addAfter(10,11)
##print newList.traverse()
##print newList.addAfter(3,12)
##print newList.traverse()
