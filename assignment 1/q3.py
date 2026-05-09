# Function to perform binary search recursively
def binary_search_recursive(arr, target, low, high):
    # Base Case: Search space is exhausted
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Check if target is at mid
    if arr[mid] == target:
        return mid
    
    # If target is smaller, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    
    # If target is larger, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)
# The Time Complexity is O(log n) as our search space gets halved after every function call
# The Space Complexity is O(log n) due to the recursive call stack depth

# Main method
def main():
    arr = [10, 20, 30, 40, 50] # List to test the algorithm
    target = 30
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Index of {target}: {result}")
    
if __name__ == "__main__":
    main()