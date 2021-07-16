# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        INPUT: Any object
        MECHANICS: view the end of the index as the front of the line!
        EDGE CASES: N/A
        OUTPUT: An DynamicArray with its newly added value!
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        INPUT: None
        MECHANICS: View index 0 as the end of the queue in the DynamicArray
        EDGE CASES: N/A
        OUTPUT: A DynamicArray object with its previously stored value at index 0 removed.
        """
        if self.is_empty() == True:
            raise QueueException
        value = self.da.data[0]
        self.da.remove_at_index(0)
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    p = Queue()
    try:
        import pdb; pdb.set_trace()
        p.dequeue()
    except Exception as e:
        print("No elements in queue", type(e))


    print("\n# dequeue example 2")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
