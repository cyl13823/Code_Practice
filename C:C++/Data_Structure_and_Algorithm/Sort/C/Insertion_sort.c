#include <stdio.h>

// Function to perform insertion sort
void insertionSort(int arr[], int n) {
    // Iterate over the array starting from the second element
    for (int i = 1; i < n; i++) {
        int temp = arr[i]; // Store the current element to be inserted
        int j = i; // Initialize a pointer to the current position

        // Shift elements to the right to make space for the current element
        while (j > 0 && arr[j - 1] > temp) {
            arr[j] = arr[j - 1];
            j -= 1;
        }
        
        arr[j] = temp; // Insert the current element into its correct position
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    insertionSort(arr, n); // Call insertion sort function
    
    // Print the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}