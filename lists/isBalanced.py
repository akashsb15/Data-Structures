'''
Check if given input of brackets is balanced
'''
from stack import *

def isBalanced(string):
    myStack = stack()

    for i in string:
        if i in ["(", "[", "{"]:
            myStack.myPush(i)
        else:
            if myStack.isEmpty():
                return False
            else:
                top = myStack.myPop()
                if (top == "(" and i != ")") or (top == "{" and i != "}") or (top == "[" and i != "]"):
                    return False
                
    return myStack.isEmpty()
                    

string = "([{}]())"
print isBalanced(string)    
