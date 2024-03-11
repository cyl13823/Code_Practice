def sequential_search(arr, target):
    # Iterate through the array
    for i in range(len(arr)):
        # Check if the current element equals the target
        if arr[i] == target:
            # If found, return the index
            return i
    # If the target is not found, return -1
    return -1