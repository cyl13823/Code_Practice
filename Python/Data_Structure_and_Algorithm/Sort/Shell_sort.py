def shell_sort(arr):
    # Length of array
    n = len(arr)
    # Set initial gap
    gap = n // 2
    
    # Start the loop
    while gap > 0:
        # Perform gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Insertion sort
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2