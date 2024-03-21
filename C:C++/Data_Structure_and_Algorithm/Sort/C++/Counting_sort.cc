#include <iostream>
#include <vector>
using namespace std;

// Function to perform counting sort on a vector
void countingSort(vector<int>& arr) {
    int n = arr.size(); // Get the size of the vector
    if (n <= 1) {
        return; // Already sorted or empty, no need to sort
    }

    int max = arr[0]; // Find the maximum element in the vector
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // Create count vector and initialize all elements to 0
    vector<int> count(max + 1, 0);

    // Count occurrences of each element
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Modify count vector to store actual position of elements in output
    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    vector<int> output(n);
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Copy the sorted elements back to the original vector
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

int main() {
    vector<int> arr = {5, 4, 3, 2, 1, 5, 7, 3, 9, 23, 6}; // Dynamic initialization of vector
    countingSort(arr); // Call counting sort function

    // Print the sorted vector
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}