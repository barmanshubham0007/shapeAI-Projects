import hashlib

def hashing():
    name = input("Enter your name:")
    print(name)
    print("Your name is being hashed....")
    hash = hashlib.md5(name.encode())
    print(hash.digest())

hashing()