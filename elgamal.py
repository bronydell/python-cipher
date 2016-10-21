import random


def modexp(base, exp, modulus):
    return pow(base, exp, modulus)


# finds a primitive root for prime p
# this function was implemented from the algorithm described here:
# http://modular.math.washington.edu/edu/2007/spring/ent/ent-html/node31.html
def find_primitive_root(p):
    if p == 2:
        return 1
    # the prime divisors of p-1 are 2 and (p-1)/2 because
    # p = 2x + 1 where x is a prime
    p1 = 2
    p2 = (p - 1) // p1

    # test random g's until one is found that is a primitive root mod p
    while (1):
        g = random.randint(2, p - 1)
        # g is a primitive root if for all prime factors of p-1, p[i]
        # g^((p-1)/p[i]) (mod p) is not congruent to 1
        if not (modexp(g, (p - 1) // p1, p) == 1):
            if not modexp(g, (p - 1) // p2, p) == 1:
                return g


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


def generateKeys(strong):
    p = random.choice(list(genprimes(strong)))
    g = find_primitive_root(p)
    x = random.randint(1, p)
    h = modexp(g, x, p)
    # x = private!!
    return [p, g, h, x]


def encrypt(key, msg):
    p = key[0]
    g = key[1]
    h = key[2]
    rs = list()
    for num in genprimes(p):
        if p % num > 0:
            rs.append(num)
    result = ""
    for ch in msg:
        k = random.choice(rs)
        result += chr(modexp(g, k, p))
        result += chr((ord(ch) * modexp(h, k, p)) % p)
    return result


def decrypt(key, msg):
    p = key[0]
    x = key[2]

    if not len(msg) % 2 == 0:
        print("Wrong crypted text")
    else:
        i = 0
        result = ""
        while i < len(msg) - 1:
            f = ord(msg[i])
            s = ord(msg[i + 1])
            buf_f = modexp(f, x, p)
            result += chr((s * modexp(buf_f, p - 2, p)) % p)
            i += 2
        print('End of decryption')
        return "".join([ch for ch in result if ch != '\x00'])


keys = generateKeys(1024)
public = keys[:3]
private = keys[:2] + [keys[3]]
encrypted = encrypt(public, 'My magic will tear you apart')

print(encrypted)
print(decrypt(private, encrypted))
