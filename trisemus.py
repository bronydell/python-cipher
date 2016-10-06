import numpy as np

def generateKeyMatrix(keyword):
    start_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = "".join(keyword.split()).upper()
    from collections import OrderedDict

    return "".join(OrderedDict.fromkeys(keyword + start_alphabet))

def removeAllSpaces(text):
    return "".join(text.split())

def getInversedDec(ch, key):
    w = len(key)
    h = len(key[0])
    x = 0
    y = 0
    aX = 0
    aY = 0
    while x < h:
        if key[x][y] == ch:
            aX = x
            aY = y
        y += 1
        if y > w - 1:
            y = 0
            x += 1
    #key = key[::-1]
    if aX-1 < 0:
        aX = h
    return key[aX-1][aY]

def getInversedEnc(ch, key):
    w = len(key)
    h = len(key[0])
    x = 0
    y = 0
    aX = 0
    aY = 0
    while x < h:
        if key[x][y] == ch:
            aX = x
            aY = y
        y += 1
        if y > w - 1:
            y = 0
            x += 1
    #key = key[::-1]
    if aX+1 >= h:
        aX = -1
    return key[aX+1][aY]


def encrypt(msg, key):
    msg = removeAllSpaces(msg).upper()
    key = np.array(list(key)).reshape(5, 5)
    print(key)
    result = ""
    for ch in msg:
        result+=getInversedEnc(ch, key)
    return result

def decrypt(msg, key):
    msg = removeAllSpaces(msg).upper()
    key = np.array(list(key)).reshape(5, 5)
    print(key)
    result = ""
    for ch in msg:
        result+=getInversedDec(ch, key)
    return result



key = generateKeyMatrix('DEVELOPER')
secret = encrypt('Nikishin Rostislav', key)
print(secret)
decoded = decrypt(secret, key)
print(decoded)