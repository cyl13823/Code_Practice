#include <stdio.h>
#include <stdlib.h> // Needed for malloc and free

// Function to perform counting sort
void countingSort(int arr[], int n) {
    // Find the maximum value in the array
    int max_value = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max_value) {
            max_value = arr[i];
        }
    }

    // Create an array of size max_value + 1 initialized with zeros
    int count[max_value + 1];
    for (int i = 0; i <= max_value; i++) {
        count[i] = 0;
    }

    // Count occurrences of each element
    for (int i = 0; i < n; i++) {
        count[arr[i]] += 1;
    }

    // Reconstruct the sorted array using count array
    int index = 0;
    for (int i = 0; i <= max_value; i++) {
        while (count[i] > 0) {
            arr[index] = i;
            count[i]--;
            index++;
        }
    }
}

// Function to perform stable counting sort
void countingSort_stable(int arr[], int n) {
    // Find the maximum element to determine the range
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // Allocate memory for the count and output arrays
    int *count = (int *)malloc((max + 1) * sizeof(int));
    int *output = (int *)malloc(n * sizeof(int));

    // Initialize the count array
    for (int i = 0; i <= max; i++) {
        count[i] = 0;
    }

    // Count occurrences of each element
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Convert counts to cumulative counts
    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Copy the sorted elements back to the original array
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }

    // Free dynamically allocated memory
    free(count);
    free(output);
}

int main() {
    int arr[] = {5, 4, 3, 2, 1}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    countingSort(arr, n); // Call counting sort function

    // Print the sorted array
    printf("Sorted array using counting sort: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Reset array for stable counting sort
    int arr_stable[] = {5, 4, 3, 2, 1}; // Input array
    countingSort_stable(arr_stable, n); // Call stable counting sort function

    // Print the sorted array
    printf("Sorted array using stable counting sort: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr_stable[i]);
    }
    printf("\n");

    return 0;
}