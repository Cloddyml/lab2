import timeit as ti
import  copy

def det_a(b, c):
    row, col = b, c

    a = copy.deepcopy(m)
    a.pop(row)
    for k in range(0, 2, 1):
        a[k].pop(col)
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def det():
    return (m[0][0] * m[1][1] * m[2][2] + m[2][0] * m[0][1] * m[1][2] + m[0][2] * m[1][0] * m[2][1] - (m[0][2] * m[1][1] * m[2][0] + m[0][0] * m[2][1] * m[1][2] + m[2][2] * m[1][0] * m[0][1]))


m = [[], [], []]
at = [[], [], []]
print('Введите элементы матрицы 3x3:')
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        m[i].append(int(input()))
start_time = ti.default_timer()
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        at[i].append(((-1) ** ((i+1) + (j + 1)) * det_a(j, i)))
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        if i != j or (i != 1 and j != 0) or (i != 2 and j != 0) or (i != 2 and j != 1):
            temp = at[i][j]
            at[i][j] = at[j][i]
            at[j][i] = temp
if det() == 0:
    print('Вычислить обратную матрицу невозможно: детерминант матрицы равен 0.')
else:
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            at[i][j] = 1/det() * at[i][j]
    print(at)
print('Время работы программы: ', ti.default_timer() - start_time)

"""1
2
1
1
1
4
2
3
6"""