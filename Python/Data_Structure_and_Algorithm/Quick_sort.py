def quick_sort(arr):
    # Base case: if the array has 1 element or less, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as the pivot
        pivot = arr[0]
        # Divide the array into two parts: elements less than or equal to the pivot, and elements greater than the pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Recursively sort the two partitions and concatenate them with the pivot
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)