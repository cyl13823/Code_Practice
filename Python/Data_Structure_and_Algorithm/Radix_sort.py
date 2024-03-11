def radix_sort(arr):
    # Find the maximum number and calculate the maximum number of digits
    max_num = max(arr)
    max_digit = len(str(max_num))
    
    # Initialize buckets for each digit
    buckets = [[] for _ in range(10)]
    
    # Iterate through each digit position from right to left
    for digit in range(max_digit):
        # Distribute numbers into buckets based on the current digit
        for num in arr:
            digit_value = (num // 10**digit) % 10
            buckets[digit_value].append(num)
        
        # Update the array with numbers from buckets
        arr = [num for bucket in buckets for num in bucket]
        
        # Reset buckets for next iteration
        buckets = [[] for _ in range(10)]
    
    return arr