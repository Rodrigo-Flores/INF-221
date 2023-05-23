from procesador_entrada import ProcesadorEntrada


def fuerza_bruta(arr):
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

    del_izquierda = 1 + \
        fuerza_bruta(arr[1:]) if arr[0] > arr[1] else fuerza_bruta(arr[1:])
    del_derecha = 1 + \
        fuerza_bruta(arr[:-1]) if arr[-1] < arr[-2] else fuerza_bruta(arr[:-1])

    return min(del_izquierda, del_derecha)


if __name__ == "__main__":
    procesador = ProcesadorEntrada()
    arrays = procesador.read_input()
    for i in range(len(arrays)):
        print(fuerza_bruta(arrays[i][1:]))
