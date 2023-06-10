import sys


class ProcesadorEntrada:
    """
    Descripción
        Clase para recibir datos por entrada estandar.

    Parámetros
        Ninguno

    Devuelve
        Ninguno
    """

    def __init__(self):
        """
        Descripción
            Inicializa el objeto ArrayProcessor.

        Parámetros
            Ninguno

        Devuelve
            Ninguno
        """
        self.num_arrays = 0
        self.arrays = []

    def read_input(self):
        """
        Descripción
            Lee la entrada desde la entrada estándar y extrae las matrices.

        Parámetros
            Ninguno

        Devuelve
            Ninguno
        """
        input_data = sys.stdin.readlines()
        self.num_arrays = int(input_data[0])
        self.arrays = [list(map(int, line.split())) for line in input_data[1:]]

        return self.arrays


if __name__ == '__main__':
    processor = ProcesadorEntrada()
    processor.read_input()
