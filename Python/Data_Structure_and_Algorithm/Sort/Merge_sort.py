def merge_sort(arr):
    # Step 1: Divide
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into left half
        right_half = arr[mid:]  # Divide the array into right half
        
        # Recursively sort the left half
        merge_sort(left_half)
        # Recursively sort the right half
        merge_sort(right_half)
        
        # Step 2: Merge
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Add remaining elements from the left half to the sorted subarray
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Add remaining elements from the right half to the sorted subarray
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1