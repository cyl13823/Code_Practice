#include <iostream>
#include <vector>
using namespace std;

// Function to perform merge sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2; // Find the middle point
        mergeSort(arr, left, mid); // Sort first half
        mergeSort(arr, mid + 1, right); // Sort second half
        // Merge the sorted halves
        int i, j, k;
        int n1 = mid - left + 1;
        int n2 = right - mid;
        vector<int> L(n1); // Dynamic array allocation
        vector<int> R(n2);
        for (i = 0; i < n1; i++) {
            L[i] = arr[left + i];
        }
        for (j = 0; j < n2; j++) {
            R[j] = arr[mid + 1 + j];
        }
        i = 0;
        j = 0;
        k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) { // Copy the remaining elements of L, if any
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) { // Copy the remaining elements of R, if any
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}

int main() {
    int arr[] = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Input array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    mergeSort(arr, 0, n - 1); // Call merge sort function

    // Print the sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}