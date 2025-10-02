from typing import List
from copy import deepcopy


def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m. Гарантируется что m >= 500
    Вернуть: двумерный массив, состоящий из каждого 4го элемента по оси размерности n
    и c 120 по 500 c шагом 5 по оси размерности m
    """
    result = []
    for i in range(0, len(X), 4):
        row = []
        for j in range(120, 500, 5):
            row.append(X[i][j])
        result.append(row)
    return result


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X.
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    total = 0
    has_non_neg = False
    n = len(X)
    m = len(X[0]) if n > 0 else 0
    diag_len = min(n, m)

    for i in range(diag_len):
        if X[i][i] >= 0:
            total += X[i][i]
            has_non_neg = True

    return total if has_non_neg else -1


def replace_values(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
    result = deepcopy(X)
    n = len(X)
    m = len(X[0]) if n > 0 else 0

    for j in range(m):
        # Calculate column mean
        col_sum = 0.0
        for i in range(n):
            col_sum += X[i][j]
        mean = col_sum / n

        # Replace values that are < 0.25 * mean or > 1.5 * mean
        for i in range(n):
            if result[i][j] < 0.25 * mean or result[i][j] > 1.5 * mean:
                result[i][j] = -1

    return result
