import random
from sympy import randprime, gcd, mod_inverse
from utils import message_to_number, number_to_message

def generate_rsa_keys(bits=2048):
    # Generate RSA keys with n at least 2048 bits
    print(f"Generating RSA keys with {bits} bits...")
    
    # Generate two prime numbers p and q
    p = randprime(2**(bits//2 - 1), 2**(bits//2))
    q = randprime(2**(bits//2 - 1), 2**(bits//2))
    
    # Edge case: ensure p != q
    while p == q:
        q = randprime(2**(bits//2 - 1), 2**(bits//2))
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose e (usually 65537)
    e = 65537
    while gcd(e, phi_n) != 1:
        e += 2
    
    # Calculate d
    d = mod_inverse(e, phi_n)
    
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n} ({n.bit_length()} bits)")
    print(f"phi(n) = {phi_n}")
    print(f"e = {e}")
    print(f"d = {d}")
    
    return {
        'public_key': (n, e),
        'private_key': (n, d),
        'p': p, 'q': q, 'phi_n': phi_n
    }

def rsa_encrypt(message, public_key):
    # Encrypt message using RSA
    n, e = public_key
    m = message_to_number(message)
    
    print(f"Original message: {message}")
    print(f"Numeric representation: {m}")
    
    if m >= n:
        raise ValueError("Message is too large for the RSA key")
    
    c = pow(m, e, n)
    print(f"Encrypted message: {c}")
    
    return c

def rsa_decrypt(ciphertext, private_key):
    # Decrypt message using RSA
    n, d = private_key
    
    m = pow(ciphertext, d, n)
    print(f"Decrypted message (numeric): {m}")
    
    message = number_to_message(m)
    print(f"Decrypted message: {message}")
    
    return message