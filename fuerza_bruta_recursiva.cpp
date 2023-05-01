#include <iostream>
using namespace std;

void quicksort(int arr[], int left, int right);

int main () {
    int N;
    cin >> N;

    int *arr = new int[N];


    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    quicksort(arr, 0, N - 1);

    // for (int i = 0; i < N; i++) {
    //     cout << arr[i] << " ";
    // }

    

    delete[] arr;
    return 0;
}

void quicksort(int arr[], int left, int right) {
    int i = left, j = right;
    int tmp;
    int pivot = arr[(left + right) / 2];

    /* partition */
    while (i <= j) {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i <= j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    };

    /* recursion */
    if (left < j)
        quicksort(arr, left, j);
    if (i < right)
        quicksort(arr, i, right);
}
