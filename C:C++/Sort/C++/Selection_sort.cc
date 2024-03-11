#include <iostream>
using namespace std;

// Function to perform selection sort
void selectionSort(int arr[], int n) {
    // Traverse through all elements in the array
    for (int i = 0; i < n; i++) {
        // Find the minimum element in the unsorted part of the array
        int mini = i;
        for (int j = i; j < n; j++) {
            if (arr[mini] > arr[j]) {
                mini = j;
            }
        }
        // Swap the found minimum element with the first element of the unsorted part
        if (mini != i) {
            swap(arr[mini], arr[i]);
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    selectionSort(arr, n); // Call selection sort function

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}