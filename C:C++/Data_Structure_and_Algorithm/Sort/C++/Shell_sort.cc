#include <iostream>
using namespace std;

// Function to perform Shell sort
void ShellSort(int arr[], int n) {
    // Start with a big gap, then reduce the gap
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // Do a gapped insertion sort for this gap size.
        // The first gap elements arr[0..gap-1] are already in gapped order
        // Keep adding one more element until the entire array is gap sorted
        for (int i = gap; i < n; i++) {
            // Add arr[i] to the elements that have been gap sorted
            // Save arr[i] in temp and make a hole at position i
            int temp = arr[i];
            // Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            int j = i;
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }
            // Put temp (the original arr[i]) in its correct location
            arr[j] = temp;
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    ShellSort(arr, n); // Call Shell sort function

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}