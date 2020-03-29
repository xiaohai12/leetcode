# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if iterator.hasNext():
            self.Next = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.Next

    def next(self):
        """
        :rtype: int
        """
        tmp = self.Next
        if self.iterator.hasNext():
            self.Next = self.iterator.next()
        else:
            self.Next = None

        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.Next != None