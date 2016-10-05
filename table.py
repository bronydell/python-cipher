import copy

import numpy as np


# Шифрующие таблицы



def encrypt(text, key, shuffle, shuffler):
    h = key
    if len(text) % key == 0:
        w = int(len(text) / key)
    else:
        w = int(len(text) / key) + len(text) % key

    matrix = [[' ' for x in range(w)] for y in range(h)]
    matrix = np.array(matrix)
    x = 0
    y = 0
    for ch in text:
        matrix[x][y] = ch
        x += 1
        if x > h - 1:
            x = 0
            y += 1
    print('---ENCRYPTION. STEP 1---')
    print(matrix)
    matrix = np.rot90(matrix, 1)
    matrix = matrix[::-1]
    tmp = copy.copy(matrix)
    i = 0
    for line in shuffle:
        tmp[i] = matrix[line - 1]
        i += 1
    tmp = tmp[::-1]
    tmp = np.rot90(tmp, -1)
    matrix = copy.copy(tmp)

    print('---ENCRYPTION. STEP 2---')
    print(matrix)
    i = 0
    tmp = copy.copy(matrix)
    for line in shuffler:
        tmp[i] = matrix[line - 1]
        i += 1

    matrix = copy.copy(tmp)
    print('---ENCRYPTION. STEP 3---')
    print(matrix)
    x = 0
    y = 0
    result = ""
    while x < h:
        result += matrix[x][y];
        y += 1
        if y > w - 1:
            y = 0
            x += 1
    return result


def decryption(text, key, shuffle, shuffler):
    h = key
    if len(text) % key == 0:
        w = int(len(text) / key)
    else:
        w = int(len(text) / key) + len(text) % key

    matrix = [[' ' for x in range(w)] for y in range(h)]
    matrix = np.array(matrix)
    x = 0
    y = 0

    for ch in text:
        matrix[x][y] = ch
        y += 1
        if y > w - 1:
            y = 0
            x += 1

    print('---DECRYPTION. STEP 1---')
    print(matrix)
    tmp = copy.copy(matrix)
    i = 0
    for line in shuffler:
        tmp[line - 1] = matrix[i]
        i += 1
    matrix = copy.copy(tmp)
    print('---DECRYPTION. STEP 2---')
    print(matrix)
    matrix = np.rot90(matrix, 1)
    matrix = matrix[::-1]
    i = 0
    for line in shuffle:
        tmp[line - 1] = matrix[i]
        i += 1
    tmp = np.rot90(tmp, 1)
    tmp = tmp[::-1]
    matrix = copy.copy(tmp)
    result = ""
    x = 0
    y = 0
    while y < w:
        result += matrix[x][y];
        x += 1
        if x > h - 1:
            x = 0
            y += 1

    return result


print(encrypt('ВРЕМЕНА МЕНЯЮТСЯ', 4, [1, 3, 4, 2], [4, 3, 2, 1]))
print(decryption(encrypt('ВРЕМЕНА МЕНЯЮТСЯ', 4, [1, 3, 4, 2], [4, 3, 2, 1]), 4, [1, 3, 4, 2], [4, 3, 2, 1]))
