'''
This implementation of Doubly Linked Lists uses two pointers, head and tail. 
'''


class Node(object):
    key = 0
    next = None
    prev = None

    def __init__(self, key):
        self.key = key

class doublyList(object):
    head = None
    tail = None

    # Pushes a new node to the front of the linked list. Time complexity - O(1)
    def pushFront(self, key):
        newNode = Node(key)

        if self.head:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = self.head

        return "pushFront(" + str(key) + ")"

    # Returns the front node of the linked list. Time complexity - O(1)
    def topFront(self):
        if not self.head:
            return "empty - topFront()"
        return self.head.key

    # Pops the front node of the linked list. Time complexity - O(1)
    def popFront(self):
        if not self.head:
            return "empty - popFront()"

        self.head = self.head.next

        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None

        return "success - popFront()"

    # Pushes a new node to the back of the linked list. Time complexity - O(1)
    def pushBack(self, key):
        newNode = Node(key)
        
        if not self.head:
            self.head = newNode
            self.tail = self.head
            return "success - " + "pushBack(" + str(key) + ")"
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return "success - " + "pushBack(" + str(key) + ")"

    # Returns the back of the linked list. Time complexity - O(1)
    def topBack(self):
        if not self.head:
            return "empty - topBack()"
        return self.tail.key

    # Pops the back of the linked list. Time complexity - O(1)
    def popBack(self):
        if not self.head:
            return "empty - popBack()"

        self.tail = self.tail.prev

        if not self.tail:
            self.head = None
        else:
            self.tail.next = None

        return "success - popBack()"


    # Erases the node containing the specified key. Time complexity - O(n)
    def erase(self, key):
        if not self.head:
            return "empty - erase(" + str(key) + ")"

        current = self.head
        while current:
            if current.key == key:
                current.prev.next = current.next
                current.next.prev = current.prev
                return "success - erase(" + str(key) + ")"

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
            current = self.head
            newNode = Node(key2)
            
            while current:
                if current.key == key1:
                    newNode.prev = current.prev
                    current.prev.next = newNode
                    newNode.next = current
                    current.prev = newNode
                    return "success - addBefore(" + str(key1) + ", " + str(key2) + ")"

                current = current.next
                
            return "key not in list - addBefore(" +str(key1)+ ")"


    # Adds a new node with key2 after an existing node with key1. Time complexity - O(n)
    def addAfter(self, key1, key2):
        if not self.head:
            return "empty - addAfter()"
        elif self.tail.key == key1:
            return self.pushBack(key2)+ " - addAfter(" + str(key1) + ", " + str(key2) + ")"
        else:
            current = self.head
            newNode = Node(key2)

            while current:
                if current.key == key1:
                    newNode.next = current.next
                    newNode.prev = current
                    current.next.prev = newNode
                    current.next = newNode
                    return "success - addAfter(" + str(key1) + ", " + str(key2) + ")"

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
    

    # Traverses through the linked list in reverse. Time complexity - O(n)
    def traverseReverse(self):
        if not self.head:
            return "empty - traverse()"

        temp = self.tail
        result = []
        while temp:
            result.append(temp.key)
            temp = temp.prev

        return result                    


newList = doublyList()
print newList.popBack()
print newList.popFront()
print newList.pushBack(1)
print newList.pushBack(2)
print newList.pushBack(3)
print newList.pushBack(4)
print newList.pushFront(0)
print newList.pushFront(-1)
print newList.traverse()
print newList.popBack()
print newList.traverse()
print newList.popFront()
print newList.traverse()
print newList.erase(5)
print newList.traverse()
print newList.addBefore(0,10)
print newList.traverse()
print newList.addAfter(10,11)
print newList.traverse()
print newList.addAfter(3,12)
print newList.traverse()
print newList.traverseReverse()
            
            

    
