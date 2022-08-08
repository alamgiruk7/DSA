'''Linked Lists'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("Linked List is Empty.")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_middle(self, data, pos):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        length = self.get_len()

        count = 0
        while itr:
            if pos == 0:
                self.head = Node(data, itr)
                return
            elif count == pos-1:
                itr.next = Node(data, itr.next)
                return
            elif pos < count or pos > length:
                raise Exception("Index out of range")
            
            itr = itr.next
            count += 1

    def get_len(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_new_list(self, data_list):
        if not len(data_list):
            raise Exception("Please add items to the list")
        if self.head:
            self.head = None
        for item in data_list:
            node = Node(item, self.head)
            self.head = node

    def remove_at(self, pos):
        length = self.get_len()
        if not self.head:
            raise Exception("List is empty")
        elif pos < 0 or pos >= length:
            raise Exception("list index out of range")
        else:
            if pos == 0:
                self.head = self.head.next
            itr = self.head
            count = 0
            while itr:
                if count == pos-1:
                    itr.next = itr.next.next
                    return
                
                itr = itr.next
                count += 1

    def insert_after_value(self, prev_value, data):
        if not self.head:
            raise Exception("List is empty")
        
        itr = self.head
        count = 0
        while itr:
            if itr.data == prev_value:
                itr.next = Node(data, itr.next)
                return
            
            count += 1
            itr = itr.next

        if not itr:
            raise Exception("Item not in the list")

    def remove_by_value(self, value):
        if not self.head:
            raise Exception("List is empty")

        itr = self.head
        while itr:
            if itr.next is None:
                raise Exception("Item not in the list")
            elif itr.next.data == value:
                itr.next = itr.next.next
                return
                
            itr = itr.next              
            

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_new_list(['banana', 'mango', 'apple', 'strawberry'])
    ll.print_list()
    # ll.insert_after_value('mango', 'peach')
    # ll.print_list()
    ll.remove_by_value('banana')
    ll.print_list()