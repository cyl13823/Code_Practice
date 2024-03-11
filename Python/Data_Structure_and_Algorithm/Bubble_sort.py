# Bubble_sort_v1
def bubble_sort(a_list):
    # Iterate over the list in reverse order
    # Starting from len(a_list) - 1 down to 1 (inclusive) because the last element is already in its final position
    for i in range(len(a_list) - 1, 0, -1):
        # Iterate over the list from index 0 to i - 1
        # Compare each adjacent pair of elements and swap if necessary
        for j in range(i):
            # If the current element is greater than the next element, swap them
            if a_list[j] > a_list[j + 1]:
                # Swap elements
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp


# Bubble_sort_v2
def bubble_sort_short(a_list):
    # Iterate over the list in reverse order
    # Starting from len(a_list) - 1 down to 1 because the last element is already in its final position
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False  # Flag to track if any exchanges were made in this iteration
        # Iterate over the list from index 0 to i - 1
        # Compare each adjacent pair of elements and swap if necessary
        for j in range(i):
            # If the current element is greater than the next element, swap them
            if a_list[j] > a_list[j + 1]:
                # Swap elements
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                exchanges = True  # Set the flag to True indicating an exchange was made
        # If no exchanges were made in this iteration, the list is already sorted, so break out of the loop
        if not exchanges:
            break
