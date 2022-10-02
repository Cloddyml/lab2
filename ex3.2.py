import timeit as ti
import numpy as np


start_time = ti.default_timer()
m = np.zeros((3, 3), dtype="float32")
print('Введите элементы матрицы 3x3:')
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        m[i][j] = int(input())
print(np.linalg.det(m))
try:
    print(np.linalg.inv(m))
except np.linalg.LinAlgError:
    print("Вычислить обратную матрицу невозможно: детерминанта матрицы равна 0.")
print('Время работы программы: ', ti.default_timer() - start_time)

"""1 / -1 * [[-6, 2, 1], [-9, 4, 1], [7, -3, -1]]
Время работы программы:  7.149698700057343"""
"""Ввод 1 2 1   1 1 4   2 3 6"""