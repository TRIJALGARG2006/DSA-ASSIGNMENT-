class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            
    def delete_by_value(self, val):
        if not self.head:
            return "Underflow"
        if self.head.val == val:
            self.head = self.head.next
        else:
            curr = self.head
            nextNode = curr.next
            while nextNode and nextNode.val != val:
                curr = curr.next
                nextNode = nextNode.next
            curr.next = curr.next.next
    
    def traverse(self):
        out = ""
        curr = self.head
        while curr:
            out += str(curr.val) + " , "
            curr = curr.next
        print(f"[{out[:-3]}]")

def main():
    LL = SinglyLinkedList()
    LL.insert_at_end(1)
    for i in range(1,6):
        LL.insert_at_end(i)
    LL.delete_by_value(1)
    LL.traverse()

if __name__ == "__main__":
    main()