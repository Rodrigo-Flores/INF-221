def encontrar_subarreglo_maximo(arr):
    def encontrar_subarreglo_maximo_rec(arr, inicio, fin):
        # Caso base: solo hay un elemento en el subarreglo
        if inicio == fin:
            return inicio, fin, arr[inicio]

        # Encontrar la posición del elemento del medio
        medio = (inicio + fin) // 2

        # Encontrar el subarreglo máximo que cruza el punto medio
        cruzando_inicio, cruzando_fin, cruzando_max = encontrar_subarreglo_maximo_cruzando(arr, inicio, fin, medio)

        # Encontrar el subarreglo máximo en el subarreglo izquierdo
        izquierda_inicio, izquierda_fin, izquierda_max = encontrar_subarreglo_maximo_rec(arr, inicio, medio)

        # Encontrar el subarreglo máximo en el subarreglo derecho
        derecha_inicio, derecha_fin, derecha_max = encontrar_subarreglo_maximo_rec(arr, medio + 1, fin)

        # Combinar los resultados para obtener el subarreglo máximo global
        if cruzando_max >= izquierda_max and cruzando_max >= derecha_max:
            return cruzando_inicio, cruzando_fin, cruzando_max
        elif izquierda_max >= cruzando_max and izquierda_max >= derecha_max:
            return izquierda_inicio, izquierda_fin, izquierda_max
        else:
            return derecha_inicio, derecha_fin, derecha_max

    def encontrar_subarreglo_maximo_cruzando(arr, inicio, fin, medio):
        # Encontrar la suma máxima en el subarreglo que cruza el punto medio (desde medio hacia la izquierda)
        izquierda_max = float('-inf')
        izquierda_suma = 0
        izquierda_indice = medio
        for i in range(medio, inicio - 1, -1):
            izquierda_suma += arr[i]
            if izquierda_suma > izquierda_max:
                izquierda_max = izquierda_suma
                izquierda_indice = i

        # Encontrar la suma máxima en el subarreglo que cruza el punto medio (desde medio+1 hacia la derecha)
        derecha_max = float('-inf')
        derecha_suma = 0
        derecha_indice = medio + 1
        for i in range(medio + 1, fin + 1):
            derecha_suma += arr[i]
            if derecha_suma > derecha_max:
                derecha_max = derecha_suma
                derecha_indice = i

        # Devolver los índices y la suma máxima del subarreglo que cruza el punto medio
        return izquierda_indice, derecha_indice, izquierda_max + derecha_max

    inicio, fin, suma_maxima = encontrar_subarreglo_maximo_rec(arr, 0, len(arr) - 1)

    return inicio, fin, suma_maxima


# Ejemplo de uso
# lista = [9, -10, 4, 3, -2, -8, 20, -2, 1, -1]
lista = [9,-10,4,3,-2,-8,20,-2,3,-1]
inicio, fin, suma_maxima = encontrar_subarreglo_maximo(lista)
subarreglo = lista[inicio:fin + 1]

print("Subarreglo:", subarreglo)
print("Suma máxima:", suma_maxima)
print("Índices:", inicio, fin)