# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        INPUT: Any object
        MECHANICS: View the end of the DynamicArray as the front and push objects in front of objects!
        EDGE CASES:
        OUTPUT: A DynamicArray with a newly added object at the top of the Stack`
        """
        self.da_val.append(value)

    def pop(self) -> object:
        """
        INPUT: None
        MECHANICS: View the end of the DynamicArray as the top of a stack and remove that (FILO)
        EDGE CASES:
                    1. Stack is empty
        OUTPUT: A Dynamic Array with a removed object from the top of the stack and returned is that object.
        """
        if self.size() == 0:
            raise StackException
        value = self.da_val.data[self.size() - 1]
        self.da_val.remove_at_index(self.size() - 1)
        return value

    def top(self) -> object:
        """
        INPUT: None
        MECHANICS: View the end of the DynamicArray as the top of the stack, so return that top w/o removing
        EDGE CASES:
                    1. Stack is empty
        OUTPUT: The object at the top of the stack
        """
        if self.size() == 0:
            raise StackException
        return self.da_val.data[self.size() - 1]


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
