def get_input():
    largo_arreglo = int(input())
    arreglo = [int(x) for x in input().strip().split(' ')]
    cantidad_consultas = int(input())
    consultas = []
    for i in range(cantidad_consultas):
        consultas.append([int(x) for x in input().strip().split(' ')])

    return arreglo, consultas

def consultar(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    # Dividir el arreglo en mitades
    mitad = len(arreglo) // 2
    arreglo_izquierdo = arreglo[:mitad]
    arreglo_derecho = arreglo[mitad:]

    # Resolver recursivamente los subarreglos
    unicos_izquierdos = consultar(arreglo_izquierdo)
    unicos_derechos = consultar(arreglo_derecho)

    # Combinar las soluciones eliminando duplicados
    i = 0
    j = 0
    unicos = []

    while i < len(unicos_izquierdos) and j < len(unicos_derechos):
        if unicos_izquierdos[i] < unicos_derechos[j]:
            unicos.append(unicos_izquierdos[i])
            i += 1
        elif unicos_izquierdos[i] > unicos_derechos[j]:
            unicos.append(unicos_derechos[j])
            j += 1
        else:
            unicos.append(unicos_izquierdos[i])
            i += 1
            j += 1

    # Agregar los elementos restantes de los subarreglos
    unicos.extend(unicos_izquierdos[i:])
    unicos.extend(unicos_derechos[j:])

    return unicos


if __name__ == "__main__":
    resultado = []
    arreglo, consultas = get_input()
    for i,j in consultas:
        resultado.append(consultar(arreglo[i - 1: j]))

    [print(len(x)) for x in resultado]

        