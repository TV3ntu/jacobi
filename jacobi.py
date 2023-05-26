import numpy as np


def is_symmetric(matrix):
    """
    Verifica si una matriz es simétrica.
    :param matrix:
    :return:
    """
    return np.allclose(matrix, matrix.T)


def input_symmetric_matrix(n):
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
        if is_symmetric(A):
            return A
        else:
            print("ERROR: La matriz no es simétrica, intente nuevamente")


def input_data():
    """
    Solicita al usuario que ingrese los datos de entrada.
    :return:
    """
    n = int(input("Ingrese el valor de n (tamaño de la matriz): "))

    A = input_symmetric_matrix(n)

    print("Ingrese el vector b:")
    b = input().split()

    k = int(input("Ingrese el número de iteraciones (k): "))
    return A, b, k


def compare_solution(A, b, k):
    """
    Compara la solución exacta del sistema con la solución aproximada obtenida con el método de Jacobi.
    :param A:
    :param b:
    :param k:
    :return:
    """
    exact_solution = np.linalg.solve(A, b)  # Solución exacta del sistema

    H, _, approx_solution = jacobi(A, b, k)  # Solución aproximada con Jacobi

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

        x = (b - np.dot(R, x)) / D

        H[i] = x

    return H, np.linalg.norm(H[-1]), x


def main():
    A, b, k = input_data()

    # Conversión de los datos de entrada a valores numéricos
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Ejecución del método de Jacobi
    try:
        H, norm, x = jacobi(A, b, k)
        print("\nMatriz de iteración H:")
        print(H)

        print("\nNorma de la matriz de iteración H:", norm)

        print("\nVector aproximado x:")
        print(x)

        exact_solution, approx_solution, norm_difference = compare_solution(A, b, k)

        print("Solución exacta del sistema:")
        print(exact_solution)

        print("Solución aproximada con Jacobi:")
        print(approx_solution)

        print("Norma de la diferencia entre las soluciones:", norm_difference)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
