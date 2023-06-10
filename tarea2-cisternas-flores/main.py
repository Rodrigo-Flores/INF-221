import sys

def find_maximum_subarray(arr: list):
    def find_max_crossing_subarray(arr, low, mid, high):
        left_sum = float('-inf')
        sum = 0
        max_left = 0
        for i in range(mid, low - 1, -1):
            sum += arr[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float('-inf')
        sum = 0
        max_right = 0
        for i in range(mid + 1, high + 1):
            sum += arr[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return max_left, max_right, left_sum + right_sum

    def find_maximum_subarray_recursive(arr, low, high):
        if low == high:
            return low, high, arr[low]

        mid = (low + high) // 2

        left_low, left_high, left_sum = find_maximum_subarray_recursive(arr, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray_recursive(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    if len(arr) == 0:
        return None

    low, high, max_sum = find_maximum_subarray_recursive(arr, 0, len(arr) - 1)
    return max_sum, list(range(low, high + 1))



if __name__ == "__main__":
    acciones = [int(linea.strip()) for linea in sys.stdin]

    resultado = find_maximum_subarray(acciones)

    print(str(resultado[1][0] + 1)  + " " + str(resultado[1][-1] + 1))
    print(resultado[0])