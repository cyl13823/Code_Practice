def insertion_sort(a_list):
    # Iterate over the list starting from index 1 because index 0 is considered as sorted.
    for i in range(1, len(a_list)):
        # Store the value of the current element and its index.
        cur_val = a_list[i]
        cur_pos = i
        # Shift elements greater than cur_val to the right.
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos -= 1
        # Insert cur_val into its correct position.
        a_list[cur_pos] = cur_val