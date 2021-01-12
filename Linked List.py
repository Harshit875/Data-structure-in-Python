# Single Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_beginnig(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at(self, index, data):
        c = 0
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginnig(data)
            return
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        itr = self.head
        while c < index - 1:
            itr = itr.next
            c += 1
        node = Node(data, itr.next)
        itr.next = node

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        c = 0
        while c < index - 1:
            itr = itr.next
            c += 1
        itr.next = itr.next.next

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, value, data):
        ptr = self.head
        while ptr.data != value:
            ptr = ptr.next
        ptr.next = Node(data, ptr.next)

    def remove_by_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next


ll = LinkedList()
ll.insert_at_beginnig(5)
ll.insert_at_beginnig(6)
ll.insert_at_end(7)
ll.insert_at(2, 8)
ll.insert_at(2, 9)
ll.insert_at(1, 10)
ll.insert_at(0, 11)
ll.insert_values([5, 6, 7, 8, 13])
ll.insert_after_value(11, 10)
ll.print()
ll.remove_by_value(10)
ll.print()
ll.remove_by_value(6)
ll.print()
ll.remove_by_value(5)
ll.print()
ll.remove_by_value(55)
ll.print()