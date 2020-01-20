class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        self.sentinal = Node(None)
        self.sentinal.next = self.sentinal
        self.sentinal.prev = self.sentinal
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        if self.sentinal.next == self.sentinal:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        new = Node(item)
        cur = self.sentinal
        while cur.next != self.sentinal:
            cur = cur.next
            if item < cur.item:
                break
            # print('current end while: ', cur.item)
        try:
            if item > cur.item:
                prevCurNext = cur.next
                new.prev = cur
                cur.next = new
                new.next = prevCurNext
            else:
                cur.prev.next = new
                new.prev = cur.prev
                new.next = cur
                cur.prev = new
        except:
            cur.prev.next = new
            new.prev = cur.prev
            new.next = cur
            cur.prev = new

    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        cur = self.sentinal
        foundFlag = False
        while cur.next != self.sentinal and foundFlag == False:
            cur = cur.next
            if cur.item == item:
                foundFlag = True
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
        return foundFlag

    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = -1
        foundFlag = False
        cur = self.sentinal
        while cur.next != self.sentinal and foundFlag == False:
            cur = cur.next
            index += 1
            if cur.item == item:
                foundFlag = True
        if foundFlag == False:
            return None
        return index

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index >= self.size():
            raise IndexError
        cur = self.sentinal.next
        for i in range(index):
            cur = cur.next
        curReturn = cur.item
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        return curReturn

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_help(item, self.sentinal.next)

    def search_help(self, item, node):
        if node.item == item:
            return True
        if node.next == self.sentinal:
            return False
        return self.search_help(item, node.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        pyList = []
        cur = self.sentinal
        while cur.next != self.sentinal:
            pyList.append(cur.next.item)
            cur = cur.next
        return pyList

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.reverse_helper(self.python_list())

    def reverse_helper(self, pyList):
        if pyList == []:
            raise ValueError
        if len(pyList) == 1:
            return pyList
        return [pyList[-1]] + self.reverse_helper(pyList[:-1])

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_help(0, self.sentinal.next)

    def size_help(self, counter, node):
        if node.next == self.sentinal:
            if node != self.sentinal:
                counter += 1
            return counter
        counter += 1
        return self.size_help(counter, node.next)