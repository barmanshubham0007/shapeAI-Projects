import hashlib

def hashing():
    name = input("Enter your name:")
    print(name)
    print("Your name is being hashed....")
    hash1 = hashlib.md5(name.encode())       #hashing layer 1
    hash2 = hashlib.sha1(hash1.digest())       #hashing layer 2
    hash3 = hashlib.sha224(hash2.digest())       #hashing layer 3
    print(hash3.digest())

hashing()