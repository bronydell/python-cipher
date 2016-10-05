def crypt(msg, key, decrypt):
    i = 0
    key *= decrypt
    print(key)
    result = ""
    while i < len(msg):
        result += chr(ord(msg[i]) + key)
        i += 1
    return result


msg = 'Hello World'
# Encrypt
encrypted = crypt(msg, 5, 1)
print('Encrypted: ' + encrypted)
# Decrypt
decrypted = crypt(encrypted, 5, -1)
print('Decrypted: ' + decrypted)
