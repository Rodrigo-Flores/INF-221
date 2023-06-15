#include <iostream>
#include <vector>
#include <limits>

struct Subarray
{
    int low;
    int high;
    int sum;
};

Subarray findMaxCrossingSubarray(const std::vector<int> &arr, int low, int mid, int high);
/**
 * @brief Encuentra el máximo crecimiento
 *
 * Busca el mayor crecimiento desde un punto intermedio en el arreglo dado.
 * No busca de forma explícita por la izquierda y derecha, por eso lo busca cruzado.
 *
 * @param arr Arreglo de enteros.
 * @param low El índice más bajo del arreglo.
 * @param mid El pivote medio del arreglo.
 * @param high El índive más alto del arreglo.
 * @return Un objeto (para inicializar el Subarray) con el nuevo máximo encontrado sus límites.
 */

Subarray findMaximumSubarrayRecursive(const std::vector<int> &arr, int low, int high);
/**
 * @brief Encuentra el máximo crecimiento de forma recursiva (para dividir -> conquistar -> combinar (al final))
 *
 * De forma recusiva esta función encuentra el máximo crecimiento para un arreglo de número dados.
 * Invocará a la función findMaxCrossingSubarray y a sí misma para tener tres comparaciones:
 * * Por la izquierda
 * * Por la derecha
 * * De forma cruzada (desde un pivote)
 * Así se conseguirá dividir de varias formas el arreglo de enteros para posteriormente hacer el proceso de "combinar"
 * y encontrar el máximo crecimiento entre todas las divisiones.
 *
 * @param arr Arreglo de enteros.
 * @param low El índice más bajo del arreglo.
 * @param high El índive más alto del arreglo.
 * @return Un objeto (para inicializar el Subarray) con el nuevo máximo encontrado sus límites.
 *
*/

Subarray findMaximumSubarray(const std::vector<int> &arr);
/**
 * @brief Encuentra el máximo crecimiento total de todo el arreglo
 *
 * Dado el arreglo de enteros (que serán leídos por entrada estándar), determinará el mayor crecimiento del mismo.
 *
 * @param arr Arreglo de enteros.
 * @return Un objeto de tipo Subarray que contendrá el máximo crecimiento y los índices de un inicio y fin del mismo.
 */

int main()
{
    std::vector<int> numbers;
    int num;
    while (std::cin >> num) numbers.push_back(num);

    Subarray result = findMaximumSubarray(numbers);

    std::cout << result.low + 1  << " " << result.high + 1 << std::endl;
    std::cout << result.sum << std::endl;

    std::cout << std::endl;

    return 0;
}

Subarray findMaxCrossingSubarray(const std::vector<int> &arr, int low, int mid, int high)
{
    int leftSum = std::numeric_limits<int>::min(); // el equivalente a hacer float('-float') en Python
    int sum = 0;
    int maxLeft = 0;
    for (int i = mid; i >= low; i--)
    {
        sum += arr[i];
        if (sum > leftSum)
        {
            leftSum = sum;
            maxLeft = i;
        }
    }

    int rightSum = std::numeric_limits<int>::min();  // el equivalente a hacer float('-float') en Python
    sum = 0;
    int maxRight = 0;
    for (int i = mid + 1; i <= high; i++)
    {
        sum += arr[i];
        if (sum > rightSum)
        {
            rightSum = sum;
            maxRight = i;
        }
    }

    return {maxLeft, maxRight, leftSum + rightSum};
}

Subarray findMaximumSubarrayRecursive(const std::vector<int> &arr, int low, int high)
{
    if (low == high) return {low, high, arr[low]};

    int mid = (low + high) / 2;

    Subarray left = findMaximumSubarrayRecursive(arr, low, mid);
    Subarray right = findMaximumSubarrayRecursive(arr, mid + 1, high);
    Subarray crossing = findMaxCrossingSubarray(arr, low, mid, high);

    if (left.sum >= right.sum && left.sum >= crossing.sum) return left;
    else if (right.sum >= left.sum && right.sum >= crossing.sum) return right;
    else return crossing;
}

Subarray findMaximumSubarray(const std::vector<int> &arr)
{
    if (arr.empty()) return {0, 0, 0};

    return findMaximumSubarrayRecursive(arr, 0, arr.size() - 1);
}
