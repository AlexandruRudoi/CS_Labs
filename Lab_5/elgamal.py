import random
from sympy import gcd, mod_inverse
from utils import message_to_number, number_to_message, P, G

def generate_elgamal_keys():
    # Generate ElGamal keys using given p and g
    print("Generating ElGamal keys...")
    
    # Choose private key x randomly
    x = random.randint(2, P - 2)
    
    # Calculate public key y = g^x mod p
    y = pow(G, x, P)
    
    print(f"p = {P}")
    print(f"g = {G}")
    print(f"Private key x = {x}")
    print(f"Public key y = {y}")
    
    return {
        'public_key': (P, G, y),
        'private_key': x,
        'p': P, 'g': G
    }

def elgamal_encrypt(message, public_key):
    # Encrypt message using ElGamal
    p, g, y = public_key
    m = message_to_number(message)
    
    print(f"Original message: {message}")
    print(f"Numeric representation: {m}")
    
    if m >= p:
        raise ValueError("Message is too large for parameter p")
    
    # Choose k randomly
    k = random.randint(2, p - 2)
    while gcd(k, p - 1) != 1:
        k = random.randint(2, p - 2)
    
    # Calculate ciphertext (c1, c2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    
    print(f"k = {k}")
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    
    return (c1, c2)

def elgamal_decrypt(ciphertext, private_key, p):
    # Decrypt message using ElGamal
    c1, c2 = ciphertext
    x = private_key
    
    # Calculate s = c1^x mod p
    s = pow(c1, x, p)
    
    # Calculate modular inverse of s
    s_inv = mod_inverse(s, p)
    
    # Recover message
    m = (c2 * s_inv) % p
    
    print(f"s = c1^x mod p = {s}")
    print(f"s^(-1) = {s_inv}")
    print(f"Decrypted message (numeric): {m}")
    
    message = number_to_message(m)
    print(f"Decrypted message: {message}")
    
    return message