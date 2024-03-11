# Selection_sort_v1
def selection_sort_v1(a_list):
    # Iterate through the list
    for i, _ in enumerate(a_list):
        # Assume the current index as the index of the minimum element
        min_idx = i
        # Find the index of the minimum element in the unsorted part of the list
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        # If the index of the minimum element is not the same as the current index, swap them
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]

# Selection_sort_v2
def selection_v2(arr):
    # Iterate through the list
    for i in range(len(arr)):
        # Assume the current index as the index of the minimum element
        mini = i
        # Find the index of the minimum element in the unsorted part of the list
        for j in range(i, len(arr)):
            if arr[mini] > arr[j]:
                mini = j
        # If the index of the minimum element is not equal to i, swap them
        if mini != i:
            arr[mini], arr[i] = arr[i], arr[mini]

