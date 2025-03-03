import numpy as np

rows = columns = int(input("Введите размер матрицы n: "))

print("----- Ввод главной матрицы -----")

A_matrix = np.zeros((rows, columns), dtype=np.complex128)
for i in range(rows):
    for j in range(columns):
        A_matrix[i][j] = complex(
            input(f"Введите элемент a_{i+1}_{j+1} в формате (a+bj): "))

print("----- Ввод вектора свободных членов b -----")

b_vector = np.zeros((rows, 1), dtype=np.complex128)
for i in range(rows):
    b_vector[i][0] = complex(
        input(f"Введите элемент b_{i+1} в формате (a+bj): "))

A_general = np.hstack((A_matrix, b_vector))

det_Main = np.linalg.det(A_matrix)


def det_replaced(A_matrix, A_constants):
    solutions = []
    for i in range(rows):
        temp = A_matrix.copy()
        temp[:, i] = A_constants[:, 0]
        det_temp = np.linalg.det(temp)
        solutions.append(det_temp/det_Main)

    return sorted(solutions)


if det_Main != 0:
    solutions = det_replaced(A_matrix, b_vector)
    print(np.round(solutions, 2))
else:
    print("Нет решений")
