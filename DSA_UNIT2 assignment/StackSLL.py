class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackSLL:
    def __init__(self):
        self.head = None
        
    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if not self.head:
            return "Empty"
        value = self.head.val        
        self.head = self.head.next
        return value
        
    def peek(self):
        if not self.head:
            return "Empty"
        return self.head.val
    
    def traverse(self):
        if not self.head:
            print("[ ]")
        out = ""
        curr = self.head
        while curr:
            out += str(curr.val) + " , "
            curr = curr.next
        print(f"[{out[:-3]}]")

def main():
    LL = StackSLL()
    for i in range(1,6):
        LL.push(i)
    print(LL.pop())
    print(LL.peek())
    LL.traverse()

if __name__ == "__main__":
    main()