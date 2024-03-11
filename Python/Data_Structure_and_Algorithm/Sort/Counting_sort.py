def countingSort(arr):
    # Find the maximum number in the array
    max_num = max(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_num + 1)
    
    # Count the occurrences of each element in the array
    for num in arr:
        count[num] += 1
    
    # Reconstruct the sorted array using the count array
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            count[i] -= 1
            index += 1