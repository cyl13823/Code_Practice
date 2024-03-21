#include <iostream>
using namespace std;

// Function to perform interpolation search
int interpolationSearch(int arr[], int n, int target) {
    int low = 0;
    int high = n - 1;

    while (low <= high && target >= arr[low] && target <= arr[high]) {
        // Calculate the probable position of the target
        int pos = low + ((double)(high - low) / (arr[high] - arr[low])) * (target - arr[low]);

        // If target is found at pos
        if (arr[pos] == target) {
            return pos;
        }

        // If target is less, search in the left subarray
        if (arr[pos] > target) {
            high = pos - 1;
        }
        // If target is more, search in the right subarray
        else {
            low = pos + 1;
        }
    }

    // If target is not present in array
    return -1;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 50;
    int result = interpolationSearch(arr, n, target);
    if (result != -1) {
        cout << "Element found at index " << result << endl;
    } else {
        cout << "Element not found" << endl;
    }
    return 0;
}