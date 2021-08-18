#!/usr/bin/env python3

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None


    def count(self):
        return self.recursive_count(self.head)

    def recursive_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_count(ptr.next)

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
            
        return tmp_str



    def contains(self, item):
        ptr = self.head
        while ptr != None:
            if ptr.item == item:
                return True
            ptr = ptr.next
        return False

    def after(self, item):
        ptr = self.head
        while ptr != None:
            if ptr.item == item:
                return ptr.next.item
            ptr = ptr.next
        return None

    def before(self, item):
        ptr = self.head
        previous = None

        while ptr != None:
            if ptr.item == item:
                return previous

            previous = ptr.item
            ptr = ptr.next

        return None

    def append(self, item):
        ptr = self.head
        while ptr != None:
            if ptr.next == None:
                ptr.next = Node(item, None)
                break

            ptr = ptr.next


        if ptr == None:
            self.add(item)


    def rotate(self):
        ptr = self.head
        rotated_end = self.remove()
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = Node(rotated_end, None)

