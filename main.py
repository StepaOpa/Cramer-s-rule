import numpy as np

rows = columns = int(input("Введите количество строк: "))
A_matrix = np.zeros((rows, columns), dtype=np.int64)

for i in range(rows):
    for j in range(columns):
        A_matrix[i][j] = float(input(f"Введите элемент a_{i+1}_{j+1}: "))

A_constants = np.zeros((rows, 1))
for i in range(columns):
    A_constants[i][0] = float(input(f"Введите константу b_{i+1}: "))

A_general = np.hstack((A_matrix, A_constants))

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
    solutions = det_replaced(A_matrix, A_constants)
    print(np.round(solutions, 2))
