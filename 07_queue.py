
'''QUEUE'''

from collections import deque
from time import sleep, time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def additem(self, value):
        self.buffer.appendleft(value)

    def pop(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

def place_order(orders):
    # Place Order
    for order in orders:
        que.additem(order)
        print(f'{order} - order placed')
        sleep(0.5)

def deliver_order():
    # Deliver Order
    while not que.isEmpty():
        order = que.pop()
        print(f'{order} - order delivered')
        sleep(2)

if __name__ == '__main__':
    que = Queue()

    start_time = time()
    orders = ['Pizza', 'Burger', 'Chicken', 'Pasta', 'Samosa', 'Biryani']

    t1 = threading.Thread(target=place_order, args=(orders,))  
    sleep(1)
    t2 = threading.Thread(target=deliver_order)  

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time = time()
    print(f"Time Elapsed: {end_time - start_time}")

    