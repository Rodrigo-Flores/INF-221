#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int count_min_moves(vector<int>& arr) {
    // base case: array is already sorted
    if (is_sorted(arr.begin(), arr.end())) {
        return 0;
    }

    int min_moves = arr.size(); // initialize to maximum possible moves
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size(); j++) {
            if (i == j) {
                continue;
            }
            swap(arr[i], arr[j]);
            int moves = count_min_moves(arr) + 1; // recursive call
            min_moves = min(min_moves, moves);
            swap(arr[i], arr[j]); // undo the swap
        }
    }

    return min_moves;
}

int main() {
    vector<int> arr = {1, 8, 9, 2};
    cout << count_min_moves(arr) << endl; // expected output: 1
    return 0;
}
