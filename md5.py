import hashlib

print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())
