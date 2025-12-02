import random
from Crypto.Util import number
from utils import md4_hash


def generate_elgamal_keys(p: str, g: str):
    """Generate ElGamal keys using provided p and g"""
    p_int = int(p)
    g_int = int(g)
    print(f"ElGamal Parameters:")
    print(f"p = {p_int}")
    print(f"g = {g_int}")
    print(f"p bit length: {p_int.bit_length()} bits")
    x = random.randint(2, p_int - 2)
    y = pow(g_int, x, p_int)
    print(f"Private key x = {x}")
    print(f"Public key y = {y}\n")
    return x, y, p_int, g_int


def sign(message: str, x: int, p: int, g: int):
    """Sign message using ElGamal with MD4 hash"""
    h = md4_hash(message)
    print(f"Hash value (decimal): {h}")
    while True:
        k = random.randint(2, p - 2)
        if number.GCD(k, p - 1) == 1:
            break
    r = pow(g, k, p)
    k_inv = pow(k, -1, p - 1)
    s = ((h - x * r) * k_inv) % (p - 1)
    print(f"ElGamal Signature:")
    print(f"r = {r}")
    print(f"s = {s}\n")
    return (r, s, h)


def verify(message: str, signature, y: int, p: int, g: int):
    """Verify ElGamal signature using MD4 hash"""
    r, s, _ = signature
    h = md4_hash(message)
    print(f"Hash value (decimal): {h}")
    left = pow(g, h, p)
    right = (pow(y, r, p) * pow(r, s, p)) % p
    is_valid = (left == right)
    print(f"Verification:")
    print(f"g^h mod p = {left}")
    print(f"y^r * r^s mod p = {right}")
    print(f"Signature valid: {is_valid}\n")
    return is_valid, h, left, right
