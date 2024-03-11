def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    
    # Continue searching while the target is within the range of the array
    while low <= high and arr[low] <= target <= arr[high]:
        # Calculate the position using interpolation formula
        position = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[position] == target:
            return position  # If the target is found at the calculated position, return the index
        
        elif arr[position] < target:
            low = position + 1  # If the target is greater than the value at the calculated position, search in the right half
        
        else:
            high = position - 1  # If the target is less than the value at the calculated position, search in the left half
    
    return -1  # If the target is not found, return -1