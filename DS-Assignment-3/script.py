import time
import sys
import random

sys.setrecursionlimit(20000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)

def get_datasets(size):
    random_ds = [random.randint(0, size) for _ in range(size)]
    sorted_ds = sorted(random_ds)
    reverse_ds = sorted_ds[::-1]
    return {"Random": random_ds, "Sorted": sorted_ds, "Reverse": reverse_ds}

def main():
    sizes = [1000, 5000, 10000]
    algorithms = {
        "InsertionSort": insertion_sort,
        "MergeSort": merge_sort,
        "QuickSort": quick_sort
    }
    
    with open("results.txt", "w") as f:
        for size in sizes:
            datasets = get_datasets(size)
            f.write(f"--- Dataset Size: {size} ---\n")
            for algo_name, algo_func in algorithms.items():
                for ds_type, data in datasets.items():
                    data_copy = data.copy()
                    start = time.time()
                    algo_func(data_copy)
                    end = time.time()
                    f.write(f"{algo_name} ({ds_type}): {end - start:.5f}s\n")
            f.write("\n")

if __name__ == "__main__":
    main()