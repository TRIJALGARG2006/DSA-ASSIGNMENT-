class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_after_node(self, target, x):
        curr = self.head
        while curr and curr.val != target:
            curr = curr.next
            
        if not curr:
            print("Error: Value not found in list")
            return
            
        newNode = Node(x)
        newNode.next = curr.next
        newNode.prev = curr
        
        if curr.next:
            curr.next.prev = newNode
        else:
            self.tail = newNode
            
        curr.next = newNode
    
    def delete_at_position(self, pos):
        if not self.head:
            return

        curr = self.head
        for i in range(pos):
            if curr.next:
                curr = curr.next
            else:
                print("Position out of bounds")
                return

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.val))
            curr = curr.next
        print(" <-> ".join(elems) if elems else "Empty List")
    
def main():
    DLL = DoublyLinkedList()
    DLL.head = DLL.tail = Node(0)
    for i in range(5):
        DLL.insert_after_node(i,i+1)
    DLL.display()
    
if __name__ == "__main__":
    main()