from Crypto.Util import number
from utils import md5_hash


def generate_rsa_keys(bits=3072):
    """Generate RSA keys with specified bit length (minimum 3072 bits)"""
    p = number.getPrime(bits // 2)
    q = number.getPrime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)
    print(f"RSA Key Generation:")
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"d = {d}")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n bit length: {n.bit_length()} bits\n")
    return (n, e, d, p, q)


def sign(message: str, d: int, n: int):
    """Sign message using RSA with MD5 hash"""
    h = md5_hash(message)
    print(f"Hash value (decimal): {h}")
    signature = pow(h, d, n)
    print(f"RSA Signature (decimal): {signature}\n")
    return signature, h


def verify(message: str, signature: int, e: int, n: int):
    """Verify RSA signature using MD5 hash"""
    h = md5_hash(message)
    h_prime = pow(signature, e, n)
    print(f"Original hash (decimal): {h}")
    print(f"Decrypted signature (decimal): {h_prime}")
    is_valid = (h == h_prime)
    print(f"Signature valid: {is_valid}\n")
    return is_valid, h, h_prime
