#include <iostream>
#include <vector>
#include <limits> // Add this line to include the <limits> header

struct Subarray {
    int low;
    int high;
    int sum;
};

Subarray findMaxCrossingSubarray(const std::vector<int>& arr, int low, int mid, int high) {
    int leftSum = std::numeric_limits<int>::min();
    int sum = 0;
    int maxLeft = 0;
    for (int i = mid; i >= low; i--) {
        sum += arr[i];
        if (sum > leftSum) {
            leftSum = sum;
            maxLeft = i;
        }
    }

    int rightSum = std::numeric_limits<int>::min();
    sum = 0;
    int maxRight = 0;
    for (int i = mid + 1; i <= high; i++) {
        sum += arr[i];
        if (sum > rightSum) {
            rightSum = sum;
            maxRight = i;
        }
    }

    return { maxLeft, maxRight, leftSum + rightSum };
}

Subarray findMaximumSubarrayRecursive(const std::vector<int>& arr, int low, int high) {
    if (low == high) {
        return { low, high, arr[low] };
    }

    int mid = (low + high) / 2;

    Subarray left = findMaximumSubarrayRecursive(arr, low, mid);
    Subarray right = findMaximumSubarrayRecursive(arr, mid + 1, high);
    Subarray crossing = findMaxCrossingSubarray(arr, low, mid, high);

    if (left.sum >= right.sum && left.sum >= crossing.sum) {
        return left;
    }
    else if (right.sum >= left.sum && right.sum >= crossing.sum) {
        return right;
    }
    else {
        return crossing;
    }
}

Subarray findMaximumSubarray(const std::vector<int>& arr) {
    if (arr.empty()) {
        return { 0, 0, 0 };
    }

    return findMaximumSubarrayRecursive(arr, 0, arr.size() - 1);
}

int main() {
    std::vector<int> numbers;
    int num;
    while (std::cin >> num) {
        numbers.push_back(num);
    }

    Subarray result = findMaximumSubarray(numbers);

    std::cout << "Maximum sum: " << result.sum << std::endl;
    std::cout << "Indices: ";
    for (int i = result.low; i <= result.high; i++) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
