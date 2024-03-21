#include <stdio.h>

// Function to swap two integers
void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// Function to perform bubble sort
void bubbleSort(int arr[], int n) {
    // Iterate over the array from the end to the beginning
    for (int i = n - 1; i > 0; i--) {
        int exchange = 0; // Flag to check if any swaps are made
        // Iterate over the unsorted portion of the array
        for (int j = 0; j < i; j++) {
            // Swap adjacent elements if they are in the wrong order
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]); // Call swap function
                exchange = 1; // Set the exchange flag to true
            }
        }
        // If no swaps are made in a pass, the array is already sorted
        if (!exchange) {
            break;
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    bubbleSort(arr, n); // Call bubble sort function
    // Print the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}