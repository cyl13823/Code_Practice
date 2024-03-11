#include <stdio.h>

// Function to perform Quick Sort
void quickSort(int arr[], int low, int high) {
    // Check if there is more than one element in the subarray
    if (low < high) {
        int pivot = arr[high]; // Select the last element as the pivot
        int i = low - 1;
        
        // Partition the array around the pivot
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                // Increment the index of smaller element and swap
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // Swap the pivot element with the element at (i + 1)th position
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        
        // Recursively sort the elements before and after partition
        quickSort(arr, low, i);
        quickSort(arr, i + 2, high); // Note: Incremented by 2 to exclude the pivot element
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    quickSort(arr, 0, n - 1); // Call quick sort function
    // Print the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}