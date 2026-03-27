import ctypes

class DynamicArray:

    def __init__(self):
        self.n = 0 
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')
        return self.A[k]

    def append(self, x):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = x
        self.n += 1

    def pop(self):
        if self.n == 0:
            return "Underflow"
        val = self.A[self.n-1]
        self.A[self.n-1] = None
        self.n -= 1
        return val

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B 
        self.capacity = new_cap 

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    
    def display(self):
        elems = [str(self.A[i]) for i in range(self.n)]
        print(f"Array: [{', '.join(elems)}] | Size: {self.n} | Capacity: {self.capacity}")

def main():
    arr = DynamicArray()
    for i in range(1, 6):
        arr.append(i)
        arr.display()
    print(arr.pop())
    arr.display()
    print(arr[0])

if __name__ == "__main__":
    main()