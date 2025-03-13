import hashlib

data = input("Data to hash:")

hash_object = hashlib.md5()
hash_object.update(data.encode())

hash_hex = hash_object.hexdigest()

print("md5 hash:", hash_hex)