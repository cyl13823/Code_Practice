#include <stdio.h>

// Function to swap two integers
void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// Function to perform selection sort
void selectionSort(int arr[], int n) {
    // Iterate over the array
    for (int i = 0; i < n; i++) {
        int mini = i; // Assume the current index has the minimum value
        // Iterate over the unsorted portion of the array
        for (int j = i; j < n; j++) {
            // Find the index of the minimum element in the unsorted portion
            if (arr[mini] > arr[j]) {
                mini = j;
            }
        }
        // If the minimum element is not at its original position, swap it with the current element
        if (mini != i) {
            swap(&arr[mini], &arr[i]);
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    selectionSort(arr, n); // Call selection sort function
    // Print the sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}