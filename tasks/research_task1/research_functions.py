from collections import Counter
from typing import List


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return Counter(x) == Counter(y)


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x,
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    max_prod = -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            max_prod = max(max_prod, x[i] * x[i + 1])
    return max_prod


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    height = len(image)
    width = len(image[0])
    result = [[0.0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            for c in range(len(weights)):
                result[i][j] += image[i][j][c] * weights[c]

    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    x_decoded = []
    for value, count in x:
        x_decoded.extend([value] * count)

    y_decoded = []
    for value, count in y:
        y_decoded.extend([value] * count)

    if len(x_decoded) != len(y_decoded):
        return -1

    result = 0
    for i in range(len(x_decoded)):
        result += x_decoded[i] * y_decoded[i]

    return result


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    n = len(X)
    m = len(Y)
    result = [[0.0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            norm_x = sum(X[i][k] ** 2 for k in range(len(X[i]))) ** 0.5
            norm_y = sum(Y[j][k] ** 2 for k in range(len(Y[j]))) ** 0.5

            if norm_x == 0 or norm_y == 0:
                result[i][j] = 1.0
            else:
                dot_product = sum(X[i][k] * Y[j][k] for k in range(len(X[i])))
                cosine_similarity = dot_product / (norm_x * norm_y)
                result[i][j] = cosine_similarity

    return result