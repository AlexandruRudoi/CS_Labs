import hashlib
from Crypto.Hash import MD4

def md5_hash(message: str) -> int:
    """MD5 hash function for RSA digital signature"""
    h = hashlib.md5()
    h.update(message.encode())
    hash_hex = h.hexdigest()
    print("MD5 Hash:", hash_hex)
    return int(hash_hex, 16)

def md4_hash(message: str) -> int:
    """MD4 hash function for ElGamal digital signature"""
    h = MD4.new()
    h.update(message.encode())
    hash_hex = h.hexdigest()
    print("MD4 Hash:", hash_hex)
    return int(hash_hex, 16)

