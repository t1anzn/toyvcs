import hashlib

h1 = hashlib.sha256(b"test").hexdigest()
h2 = hashlib.sha256(b"test2").hexdigest()
h3 = hashlib.sha256(b"test3").hexdigest()

print(h1)
print(h2)
print(h3)