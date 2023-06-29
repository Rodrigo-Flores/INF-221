def get_input():
    largo_arreglo = int(input())
    arreglo = [int(x) for x in input().strip().split(' ')]
    cantidad_consultas = int(input())
    consultas = []
    for i in range(cantidad_consultas):
        consultas.append([int(x) for x in input().strip().split(' ')])

    return arreglo, consultas

def consultar(arreglo, consultas):
    resultado = []
    for i,j in consultas:
        nueva_consulta = set(arreglo[i - 1: j])
        resultado.append(len(nueva_consulta))

    return resultado

if __name__ == "__main__":
    arreglo, consultas = get_input()
    resultado = consultar(arreglo, consultas)
    [print(x) for x in resultado]
