def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    # Iterate until the left pointer is less than or equal to the right pointer
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        
        if arr[mid] == target:
            return mid  # If the target is found, return the index
        
        elif arr[mid] < target:
            left = mid + 1  # If the target is greater than the middle element, search in the right half
        
        else:
            right = mid - 1  # If the target is less than the middle element, search in the left half
    
    return -1  # If the target is not found, return -1