from procesador_entrada import ProcesadorEntrada


def memoization(arr, memo={}):
    """
    Descripcion
        Programacion dinamica con metodo "memoization"

    Parametros
        arr: Arreglo para encontrar los minimos movimientos para ser ordenado

    retornos
        min_mov: Minima cantidad de movimiento para ser ordenado
    """
    if len(arr) <= 1:
        return 0

    if tuple(arr) in memo:
        return memo[tuple(arr)]

    del_izquierda = 1 + \
        memoization(arr[1:], memo) if arr[0] > arr[1] else memoization(
            arr[1:], memo)
    del_derecha = 1 + \
        memoization(
            arr[:-1], memo) if arr[-1] < arr[-2] else memoization(arr[:-1], memo)
    min_mov = min(del_izquierda, del_derecha)
    memo[tuple(arr)] = min_mov

    return min_mov


if __name__ == "__main__":
    procesador = ProcesadorEntrada()
    arrays = procesador.read_input()
    for i in range(len(arrays)):
        print(memoization(arrays[i][1:]))
