# Course: CS261 - Data Structures
# Student Name: Alec Moldovan
# Assignment: Assignment 2
# Description: Implement a Dynamic Array class by completing the skeleton code provided in the 
#                   file dynamic_array.py. The DynamicArray class will use a StaticArray object as its 
#                   underlying data storage container and will provide many methods similar to those we 
#                   are used to when working with Python lists. Once completed, your implementation 
#                   will include the following methods:
#                       resize()
#                       append()
#                       insert_at_index()
#                       remove_at_index()
#                       slice()
#                       merge()
#                       map()
#                       filter()
#                       reduce()

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        INPUT: A positive integer (new capacity) and greater than or equal to current number of elements
        MECHANICS: Checks if passed new_capacity argument is greater than equal to current number of elements
                        1. If conditions are met, then create a new DynamicArray of size new_capacity.
                                AND iterate through original DynamicArray and assign at the same index each 
                                        value to the new resized DynamicArray.
        OUTPUT: None (An internal modification)
        """
        if (new_capacity < self.size) or (new_capacity <= 0):
            pass
        else:
            # Create a new StaticArray with size = new_capacity
            resized_array =  StaticArray(new_capacity)
            # Copy items from OG StaticArray to the new resized StaticArray iteratively 
            for i in range(self.size):
                resized_array[i] = self.data[i]
 
            # Assign the resized StaticArrray to the OG StaticArray
            # We keep the same DynamicArray object
            self.data = resized_array

            # Update the capacity of our DynamicArray object
            self.capacity = new_capacity




    def append(self, value: object) -> None:
        """
        INPUT: Any object
        MECHANICS: Append passed object to the end of the DynamicArray.
        EDGE CASES:
                    1. Appending invokes "Index Out of Bounds"
                    2. Empty DynamicArray
        OUTPUT: None (An internal modification)
        """
        # Check for Edge Case (1)
        if self.size + 1 > self.capacity:
            self.resize(self.capacity * 2)
            self.data[self.length()] = value
            self.size += 1

        # Check for Edge Case (2)
        elif self.size == 0:
            self.data[0] = value
            self.size += 1

        # All is well.
        else:
            self.data[self.length() ] = value
            self.size += 1
        

    def insert_at_index(self, index: int, value: object) -> None:
        """
        INPUT: Integer (target index), Any object (value)
        MECHANICS: Insert the passed object at the target index, if all conditions pass.
        EDGE CASES:
                    1. Target Index is 'Out of Bounds'
                    2. DynamicArray capacity filled to the TOP
        OUTPUT: A DynamicArray with a successfully inserted value at target index or no change if otherwise
        """
        # Check Edge Case (1)

        if (index < 0) or (index > self.size ):
            raise DynamicArrayException

        # Check Edge Case (2)
        elif (self.size == self.capacity):
            self.resize(self.capacity * 2)

        # Insert Value~
        for idx in range(self.size-1, index -1, -1):
            self.data[idx+1] = self.data[idx]
        self.data[index] = value
        self.size += 1

    def remove_at_index(self, index: int) -> None:
        """
        INPUT: Integer (target index)
        MECHANICS: Remove the value at the target index, if all conditions pass.
        EDGE CASES:
                    1. Target Index is 'Out of Bounds'
                    2. DynamicArray is empty
                    3. DynamicArray size is 1/4 of capacity
                        a. Current Capacity is 10 element or less, No rezie
                        b. Current Capacity is 10 elements or greater, resize no less than 10 elements 
        OUTPUT: A DynamicArray with a successfully removed value at target index or no change if otherwise
        """
        # Check Edge Case (1)
        if (index < 0) or (index > self.size):
            raise DynamicArrayException

        elif (self.size == 0):
            pass

        elif (self.size < self.capacity//4):

            if (self.capacity <= 10):
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i+1]
                self.data[self.size - 1] = None
                self.size -= 1

            elif (self.capacity//2 <= 10):
                self.resize(10)
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i+1]
                self.data[self.size - 1] = None
                self.size -= 1

            else:
                self.resize(self.capacity//2)
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i+1]
                self.data[self.size - 1] = None
                self.size -= 1

        elif index == self.size-1:
            self.data[index] = None
            self.size -= 1
        else:
            for i in range(index, self.size - 1):
                self.data[i] = self.data[i+1]
            self.data[self.size - 1] = None
            self.size -= 1
        

    def slice(self, start_index: int, size: int) -> object:
        """
        INPUT: Integer [start_index], Integer [size]
        MECHANICS: At start_index copy elements until size of slice equals [size], or till end of DynamicArray.
        EDGE CASES: 
                    1. Invalid arguments
                    2. start_index is out of bounds
                    3. Not enough elements to fill the slice from start 
        OUTPUT: A new DynamicArray object that contains the range(start_index, size-1) from the OG DynamicArray
        """
        slice_array = DynamicArray()
        if (start_index < 0) or (start_index >= self.size):
                raise DynamicArrayException
        elif(size > self.size) or (size + start_index > self.size) or (size < 0):
                raise DynamicArrayException

        # Resize slice_array to accomdate the number of elements
        for i in range(start_index, size+start_index):
            slice_array.append(self.data[i])

        return slice_array

    def merge(self, second_da: object) -> None:
        """
        INPUT: A DynamicArray object
        MECHANICS: Appends the passed DynamicArray object to the OG DynamicArray object
        EDGE CASES: N/A
        OUTPUT: The OG DynamicArray object with the appendeed elements from the passed DynamicArray
        """
        for i in range(second_da.length()):
            self.append(second_da.data[i])


    def map(self, map_func) -> object:
        """
        INPUT: A map function -> non-boolean
        MECHANICS: The passed map function is applied to each value in the OG DynamicArray iterable object
                    and appended to the new DynamicArray iterable object
        EDGE CASEs: N/A
        OUTPUT: A new iterable DynamicArray object with its element derived from the mapped function.
        """
        mapped_array = DynamicArray()

        # Iterate and map!
        for i in range(self.length()):
            mapped_array.append(map_func(self.data[i]))
        return mapped_array

    def filter(self, filter_func) -> object:
        """
        INPUT: A filter function -> boolean
        MECHANICS: The passed filter function is applied to each value in the OG DynamicArray iterable object
                    and the value is only appended to the new DynamicArray, if the filter function returns
                            true for that current value.
        EDGE CASES: N/A
        OUTPUT: A new iterable DynamicArray object with values filtered by the passed filter function.
        """
        filter_array = DynamicArray()

        # Iterate and filter!
        for i in range(self.length()):
            if filter_func(self.data[i]) == True:
                filter_array.append(self.data[i])
        return filter_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        INPUT: A function
        MECANICS: This method sequentially applies the reduce_func to all elements of the Dynamic Array and 
        returns the resulting value. The method takes an optional initializer parameter. If this 
        parameter is not provided, the first value in the array is used as the initializer. If the 
        Dynamic Array is empty, the method returns the value of the initializer (or None, if it was 
        not provided)
        EDGE CASES:
                    1. OG DynamicArray is empty but initializer given
                    2. OG DynamicArray is empty
                    3. OG DynamicArray has one element
                    4. Initializer is given
                    5. Initializer not given
        OUTPUT: A single object from the reduction process or None if OG DynamicArray is empty
        """
        reduced_value = 0
        # Edge Case (1)
        if (initializer != None) and (self.size == 0):
            return initializer

        # Edge Case (2)
        elif self.size == 0:
            return None

        # Edge Case (3)
        elif (initializer == None) and (self.size == 1):
            return self.data[0]

        # Edge Case (4)
        elif (initializer != None):
            reduced_value = initializer
            for i in range(self.size):
                reduced_value = reduce_func(reduced_value, self.data[i])

        # Edge Case (5)
        else:
            reduced_value = self.data[0]
            for i in range(1, self.size):
                reduced_value = reduce_func(reduced_value, self.data[i])

        return reduced_value






# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
