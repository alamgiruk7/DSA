'''Double Linked List'''

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_items(self, data):
        if not self.head:
            self.head = Node(data, None, self.head)
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node
        
        
    def printForward(self):
        if not self.head:
            raise Exception("List Empty")

        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data)+'-->'
            itr = itr.next
        
        print(dllstr)

    def printBackward(self):
        if not self.head:
            raise Exception("List Empty")

        ddlstr = ''
        itr = self.last_node()

        while itr:
            ddlstr += str(itr.data)+'-->'
            itr = itr.prev

        print(ddlstr)

    def last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data, None, None)
            return
        else:
            itr = self.head

            while itr.next:
                itr = itr.next
            
            node = Node(data, itr, None)
            itr.next = node
            return

    def insert_at_middle(self, data, index):
        if not self.head:
            self.head = Node(data, None, None)
            return

        itr = self.head
        count = 0 

        while itr:
            if index == 0:
                node = Node(data, None, self.head)
                self.head = node
                self.head.next.prev = node
                return
            elif index < count or index > self.get_len():
                raise Exception("Index out of range")
            if (index-1) == count:
                itr.next = Node(data, itr, itr.next)
                return

            itr = itr.next
            count += 1


    def get_len(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count
        
 
dll = DoubleLinkedList()


# dll.add_items(4)
# dll.add_items(5)
# dll.add_items(6)
# dll.printForward()
# dll.printBackward()

dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.printForward()
dll.insert_at_middle(10, 4)

dll.printForward()