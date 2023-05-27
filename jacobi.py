import numpy as np
import warnings
from tabulate import tabulate

# Ignorar advertencias de numpy
warnings.simplefilter(action='ignore', category=FutureWarning)
# Establecer opciones de alineación
options = {"floatfmt": ".0f", "stralign": "center"}


def es_apta_para_jacobi(A):
    """
    Verifica si la matriz A es apta para aplicar el método de Jacobi.
    :param A:
    :return:
    """
    n = A.shape[0]  # Tamaño de la matriz A
    diagonal = np.abs(A.diagonal())  # Valores absolutos de los elementos de la diagonal
    resto = np.sum(np.abs(A),
                   axis=1) - diagonal  # Suma de los valores absolutos de los elementos de cada fila, excluyendo la diagonal

    for i in range(n):
        if diagonal[i] <= resto[i]:
            return False

    return True


def input_matrix(n):
    """
    Solicita al usuario que ingrese una matriz simétrica.
    :param n:
    :return:
    """
    while True:
        print("Ingrese la matriz A:")
        A = np.zeros((n, n))
        for i in range(n):
            A[i] = input().split()
        if es_apta_para_jacobi(A):
            return A
        else:
            print("ERROR: La matriz no es apta para jacobi, intente nuevamente")


def input_data():
    """
    Solicita al usuario que ingrese los datos de entrada.
    :return:
    """
    n = int(input("Ingrese el valor de n (tamaño de la matriz): "))

    A = input_matrix(n)

    print("Ingrese el vector b:")
    b = input().split()

    k = int(input("Ingrese el número de iteraciones (k): "))
    return A, b, k


def solve(A, b, k):
    """
    Compara la solución exacta del sistema con la solución aproximada obtenida con el método de Jacobi.
    :param A:
    :param b:
    :param k:
    :return:
    """
    exact_solution = np.linalg.solve(A, b)  # Solución exacta del sistema

    H, norm, approx_solution = jacobi(A, b, k)  # Solución aproximada con Jacobi

    print("\nMatriz de iteración H:")
    print(tabulate(H, tablefmt="fancy_grid"))

    print("\nNorma de la matriz de iteración H:", norm)

    norm_difference = np.linalg.norm(exact_solution - approx_solution)  # Norma de la diferencia entre las soluciones

    return exact_solution, approx_solution, norm_difference


def jacobi(A, b, k):
    """
    Método de Jacobi para resolver un sistema de ecuaciones lineales.
    :param A:
    :param b:
    :param k:
    :return:
    """
    n = len(A)
    x = np.zeros(n)
    H = np.zeros((k, n, n))

    for i in range(k):
        D = np.diag(A)  # Diagonal de A
        R = A - np.diagflat(D)  # Resto de A

        print(f"Iteración {i + 1}:")
        print("Matriz A:")
        print(tabulate(A, tablefmt="fancy_grid"))
        print("Diagonal D:")
        print(D)
        print("Matriz resto R:")
        print(tabulate(R, tablefmt="fancy_grid"))
        print("Vector solución x:")
        print(x)

        x = (b - np.dot(R, x)) / D

        H[i] = x

        print("Nuevo vector solución x:")
        print(x)
        print("--------------------")

    return H, np.linalg.norm(H[-1]), x


def main():
    A, b, k = input_data()

    # Conversión de los datos de entrada a valores numéricos
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Ejecución del método de Jacobi
    try:
        exact_solution, approx_solution, norm_difference = solve(A, b, k)

        print("Solución exacta del sistema:")
        print(exact_solution)

        print("Solución aproximada con Jacobi:")
        print(approx_solution)

        print("Norma de la diferencia entre las soluciones:", norm_difference)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
