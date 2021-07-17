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


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
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
        if self.da_max.is_empty() == True:
            self.da_max.append(value)

        elif value >= self.top():
            self.da_max.append(value)

        self.da_val.append(value)


    def pop(self) -> object:
        """
        INPUT: None
        MECHANICS: View the end of the DynamicArray as the top of a stack and remove that (FILO)
        EDGE CASES:
                    1. Stack is empty
        OUTPUT: A Dynamic Array with a removed object from the top of the stack and returned is that object.
        """
        if self.is_empty() == True:
            raise StackException
        value = self.da_val.data[self.size() - 1]
        self.da_val.remove_at_index(self.size() - 1)

        # If max value in da_max is being removed, then that max DNE in da_val or da_max.
        if self.da_max.data[self.da_max.length() - 1] == value:
            self.da_max.remove_at_index(self.da_max.length() - 1)
        return value

    def top(self) -> object:
        """
        INPUT: None
        MECHANICS: View the end of the DynamicArray as the top of the stack, so return that top w/o removing
        EDGE CASES:
                    1. Stack is empty
        OUTPUT: The object at the top of the stack
        """
        if self.is_empty() == True:
            raise StackException
        return self.da_val.data[self.size() - 1]

    def get_max(self) -> object:
        """
        INPUT: NONE
        MECHANICS: 
        EDGE CASES:
                    1. Stack is empty_da`
        OUTPUT: The global maximum value in the Stack`
        """
        if self.da_max.is_empty() == True:
            raise StackException
        else:
            max = self.da_max.data[0]
            for i in range(self.da_max.length()):
                if max < self.da_max.data[i]:
                    max = self.da_max.data[i]

        return max



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
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
    s = MaxStack()
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


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
