class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class QueueSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
    
    def dequeue(self):
        if not self.head:
            return "Empty"
        else:
            val = self.head.val
            self.head = self.head.next
            return val
        
    def display(self):
        if not self.head:
            print("[ ]")
        out = ""
        curr = self.head
        while curr:
            out += str(curr.val) + " , "
            curr = curr.next
        print(f"[{out[:-3]}]")
    
def main():
    queue = QueueSLL()
    for i in range(1,6):
        queue.enqueue(i)
    queue.display()
    queue.dequeue()
    queue.display()
    
if __name__ == "__main__":
    main()