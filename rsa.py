import random


def genprimes(limit):
    D = {}
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generateKeys(strong):
    nums = random.sample(set(genprimes(strong)), 2)
    a = nums[0]
    # a = 3
    b = nums[1]
    # b = 7
    n = a * b
    eler = (a - 1) * (b - 1)
    rs = list()
    for num in genprimes(eler):
        if eler % num > 0:
            rs.append(num)
    open = [random.choice(rs), n]
    e = 1
    inv = -1
    while e < open[1]:
        if (e * open[0]) % eler == 1:
            inv = e
            break
        # print(str(e) + ' = ' + str((e * open[0]) % open[1]))
        e += 1

    private = [int(inv), n]

    return [open, private]


def encrypt(pubkey, number):
    return pow(number, pubkey[0]) % pubkey[1]


def decrypt(prkey, number):
    return pow(number, prkey[0]) % prkey[1]


def encrypt_text(pubkey, text):
    result = ""
    for ch in text:
        result += chr(encrypt(pubkey, ord(ch)))
    return result


def decrypt_text(prkey, text):
    result = ""
    for ch in text:
        result += chr(decrypt(prkey, ord(ch)))
    return result


keys = generateKeys(1000)
print(keys)
encrypted = encrypt_text(keys[0], 'Example')
print(encrypted)
print(decrypt_text(keys[1], encrypted))
