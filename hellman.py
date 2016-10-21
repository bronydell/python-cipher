def isInt(n):
    return type(1) == type(n)


def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


base = int(input("Введите первое простое число: "))  # Request user for (shared) prime base
modulus = int(input("Введите второе простое число: "))  # Request user for (shared) prime modulus
secret = int(input("Введите секретный ключ: "))  # Request secret key

if not isPrime(base):
    print("Число не простое...")  # Is not prime
    exit()
if not isPrime(modulus):
    print("Число не простое...")  # Is not prime
    exit()
if not isInt(secret):
    print("Секрертный ключ не число...")  # Is not number
    exit()

print("Поделитесь этим с собеседником: ", base ** secret % modulus)  # Ask to share key with partner
uresult = int(input("Введите результат: "))  # Result
print("Вот ваш секретный ключ: ", uresult ** secret % modulus)  # Secret key
