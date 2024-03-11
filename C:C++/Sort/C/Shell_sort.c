#include <stdio.h>

// Function to perform Shell Sort
void ShellSort(int arr[], int n) {
    // Start with a large gap, then reduce the gap
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // Perform insertion sort for elements at a distance of gap
        for (int i = gap; i < n; i++) {
            int temp = arr[i]; // Store the current element to be inserted
            int j = i; // Initialize a pointer to the current position
            
            // Shift elements to the right to make space for the current element
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }
            
            arr[j] = temp; // Insert the current element into its correct position
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    ShellSort(arr, n); // Call Shell Sort function
    
    // Print the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}