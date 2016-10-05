'''
If u're russian, then u can make your own alphabet in generateKeyMatrix(),
just DON'T FORGET TO CHANGE 5X5 MATRIX on another size
'''

import numpy as np


def removeAllSpaces(text):
    return "".join(text.split())


def generateKeyMatrix(keyword):
    start_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = "".join(keyword.split()).upper()
    from collections import OrderedDict

    return "".join(OrderedDict.fromkeys(keyword + start_alphabet))


def generateBionims(msg, dec):
    i = 0
    bionims = list()
    if dec == -1:
        while i < len(msg) - 1:
            bion = msg[i] + msg[i + 1]
            bionims.append(bion)
            i += 2
    else:
        while i < len(msg) - 1:
            bion = msg[i]
            if i + 1 == len(msg):
                bion += 'X'
            elif msg[i] == msg[i + 1]:
                msg = msg[:i + 1] + 'X' + msg[i + 1:]
                return generateBionims(msg, 1)
            else:
                bion += msg[i + 1]
            bionims.append(bion)
            i += 2
        if i < len(msg):
            bionims.append(msg[i] + 'X')
    return bionims


def getNewBiom(biom, key, dec):
    x = 0
    y = 0
    h = len(key)
    w = len(key[0])

    aX = 0
    aY = 0
    bX = 0
    bY = 0

    while x < h:
        if key[x][y] == biom[0]:
            aX = x
            aY = y
        elif key[x][y] == biom[1]:
            bX = x
            bY = y
        y += 1
        if y > w - 1:
            y = 0
            x += 1

    if aX == bX:
        aY += dec
        bY += dec
        if aY >= w:
            aY = 0
        if bY >= w:
            bY = 0

        if aY < 0:
            aY = w - 1
        if bY < 0:
            bY = w - 1
        return key[aX][aY] + key[bX][bY]

    elif aY == bY:
        aX += dec
        bX += dec
        if aX >= h:
            aX = 0
        if bX >= h:
            bX = 0

        if aX < 0:
            aX = h - 1
        if bX < 0:
            bX = h - 1
        return key[aX][aY] + key[bX][bY]
    else:
        return key[aX][bY] + key[bX][aY]


def decrypt(msg, key):
    key = np.array(list(key)).reshape(5, 5)
    bionims = generateBionims(msg, -1)
    print(key)
    i = 0
    while i < len(bionims):
        bionims[i] = getNewBiom(bionims[i], key, -1)
        i += 1
    return "".join(bionims)


def encrypt(msg, key):
    msg = removeAllSpaces(msg).upper()
    key = np.array(list(key)).reshape(5, 5)
    print(key)
    bionims = generateBionims(msg, 1)
    i = 0
    while i < len(bionims):
        bionims[i] = getNewBiom(bionims[i], key, 1)
        i += 1
    print(bionims)
    return "".join(bionims)


key = generateKeyMatrix('WHEATSTONE')
secret = encrypt('My magic will tear u apart', key)
print(secret)
print(decrypt(secret, key))
