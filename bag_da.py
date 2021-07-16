# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        INPUT: Any object
        MECHANICS: Add an object to the list
        EDGE CASES:
        OUTPUT: OG DynamicArray object includes the added object [value]
        """
        # The Amortized Analysis of the append method is already O(1)
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        INPUT: Target value to remove
        MECHANICS: Scan for target value
        EDGE CASES:
                    1. Value DNE
        OUTPUT: OG DynamicArray object with target value removed, if it exists.
        """
        # A bag is unsorted. Must do linear search
        for i in range(self.size()):
            peek = self.da.data.get(i)
            if value == peek:
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        INPUT: Value to match
        MECHANICS: Increment count every match for target value
        EDGE CASES: 
                    1. Value DNE
        OUTPUT: An integer that represents the number of occurences of target value.
        """
        count = 0
        for i in range(self.da.length()):
            peek = self.da.data.get(i)
            if value == peek:
                count += 1
        return count

            

    def clear(self) -> None:
        """
        INPUT: None
        MECHANICS: Clear the contents of the DynamicArray!
        EDGE CASES:
                    1.  DynamicArray is empty
        OUTPUT: A cleared DynamicArray
        """
        if self.size() == 0:
            pass
        else:
            empty_da = DynamicArray()
            self.da = empty_da

    def equal(self, second_bag: object) -> bool:
        """
        INPUT: A DynamicArray object
        MECHANICS: If they have the same elements, and everything is represented by a number,
                    then a reduction of each list should equal each other!
        EDGE CASES:
                    1. Empty bags
                    2. Bags same size but do not contain same elements
        OUTPUT: True/False (True if bags are equal; False otherwise)
        """
        if (self.size() == second_bag.size()):
            # Linear search each element in our bag and see if it is in the second bag.
            match_count = 0
            prev_match_index = None
            for i in range(self.size()):
                value = self.da.data[i]
                for j in range(self.size()):
                    poss_match = second_bag.da.data[j]
                    if value == poss_match and prev_match_index != j:
                        match_count += 1
                        prev_match_index = j
                        break
            if (match_count == self.size()):
                return True
            else:
                return False
        else:
            return False



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag4 = Bag(['eY', 'gE`^QkWOb', 'XDHX', 'JGeEuLK\\`', 'pQKPBIk', 'RTlT', 'uBdB^o', 'bBKVUqawD'])
    bag5 = Bag(['uBdB^o', 'gE`^QkWOb', 'XDHX', 'eY', 'pQKPBIk', 'RTlT', 'JGeEuLK\\`', 'bBKVUqawD'])
    bag6 = Bag([1,2,2])
    bag7 = Bag([2,1,2])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag6.equal(bag7), bag7.equal(bag6))
    print(bag4.equal(bag5), bag5.equal(bag4))
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
