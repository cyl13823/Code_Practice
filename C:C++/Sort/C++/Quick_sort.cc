#include <iostream>
using namespace std;

// Function to perform Quick sort
void quickSort(int arr[], int left, int right) {
    if (left < right) {
        int pivot = arr[left]; // Select the pivot element
        int i = left;
        // Partitioning step
        for (int j = left + 1; j <= right; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr[j], arr[i]); // Swap elements if they are less than pivot
            }
        }
        swap(arr[i], arr[left]); // Move pivot to its correct position
        // Recursive calls to sort sub-arrays
        quickSort(arr, left, i - 1); // Sort elements before the pivot
        quickSort(arr, i + 1, right); // Sort elements after the pivot
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    quickSort(arr, 0, n - 1); // Call Quick sort function

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}