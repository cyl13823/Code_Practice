#include <iostream>
using namespace std;

// Function to perform insertion sort
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int temp = arr[i]; // Store the current element to be inserted
        int j = i;
        // Move elements of arr[0..i-1], that are greater than temp, to one position ahead of their current position
        while (j >= 1 && arr[j - 1] > temp) {
            arr[j] = arr[j - 1];
            j--;
        }
        arr[j] = temp; // Insert temp into the correct position
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    insertionSort(arr, n); // Call insertion sort function

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}