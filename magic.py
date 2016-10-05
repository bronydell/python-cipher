# Метод

import numpy as np


def encrypt(text, key):
    w = h = len(text) / len(key)
    x = 0
    y = 0
    result = ""
    while x < h:
        result += text[key[x][y] - 1];
        y += 1
        if y > w - 1:
            y = 0
            x += 1
    return result


def decrypt(text, key):
    key = key.flatten()
    result = [' '] * len(key)
    i = 0
    for ch in key:
        result[ch - 1] = text[i]
        i += 1
    return ''.join(result)


key = [
    [2, 9, 4],
    [7, 5, 3],
    [6, 1, 8]
]
encrypted = encrypt('ВЕДОМОСТЬ', np.array(key))
print(encrypted)
decrypted = decrypt(encrypted, np.array(key))
print(decrypted)
