#include <iostream>
using namespace std;

// Function to perform bubble sort
void bubbleSort(int arr[], int n) {
    // Traverse through all elements in the array
    for (int i = n - 1; i > 0; i--) {
        // Last i elements are already sorted, so we traverse only till the (i-1)th element
        for (int j = 0; j < i; j++) {
            // Swap adjacent elements if they are in the wrong order
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]); // Swap operation
            }
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    bubbleSort(arr, n); // Call bubble sort function

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}