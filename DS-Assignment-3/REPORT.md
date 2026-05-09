# Algorithm Performance Report

### 1. Observed Performance vs. Theory

| Algorithm      | Best Case     | Average Case  | Worst Case    |
| -------------- | ------------- | ------------- | ------------- |
| Insertion Sort | O($n$)        | O($n^2$)      | O($n^2$)      |
| Merge Sort     | O($n \log n$) | O($n \log n$) | O($n \log n$) |
| Quick Sort     | O($n \log n$) | O($n \log n$) | O($n^2$)      |

- Insertion Sort: Performance degrades significantly as $n$ increases. In the "Sorted" dataset, it performs near-linearly, but it is highly inefficient for large "Random" or "Reverse" datasets.

- Merge Sort: Displays consistent $O(n \log n)$ behavior across all dataset types. The overhead of recursion and array splitting makes it slower than Insertion Sort for very small $n$, but it dominates at 5,000+.

- Quick Sort: Generally the fastest for "Random" data. However, using the last element as a pivot (as implemented) leads to $O(n^2)$ performance on "Sorted" or "Reverse" data, which is evident in the drastically higher execution times for those specific datasets.

### 2. Stability and In-Place Nature

#### Stability

- Insertion Sort: Stable. Does not change the relative order of elements with equal keys.
- Merge Sort: Stable. The merging process preserves the original order of equal elements.
- Quick Sort: Unstable. Swapping elements across the pivot can reorder equal elements.

#### In-Place Nature

- Insertion Sort: In-place. Requires $O(1)$ auxiliary space.
- Merge Sort: Not In-place. Requires $O(n)$ additional space for the temporary subarrays during the merge process.
- Quick Sort: In-place. It sorts the array by swapping elements within the original bounds, though it requires $O(\log n)$ stack space for recursion.
