import random
import hashlib
from utils import P, G

def diffie_hellman_exchange():
    # Implement Diffie-Hellman key exchange
    print("Diffie-Hellman key exchange between Alice and Bob...")
    print(f"Public parameters: p = {P}, g = {G}")
    
    # Alice chooses private key a
    a = random.randint(2, P - 2)
    print(f"Alice chooses private key a = {a}")
    
    # Bob chooses private key b  
    b = random.randint(2, P - 2)
    print(f"Bob chooses private key b = {b}")
    
    # Alice calculates and sends A = g^a mod p
    A = pow(G, a, P)
    print(f"Alice calculates A = g^a mod p = {A}")
    
    # Bob calculates and sends B = g^b mod p
    B = pow(G, b, P)
    print(f"Bob calculates B = g^b mod p = {B}")
    
    # Alice calculates shared key
    shared_key_alice = pow(B, a, P)
    print(f"Alice calculates shared key: B^a mod p = {shared_key_alice}")
    
    # Bob calculates shared key
    shared_key_bob = pow(A, b, P)
    print(f"Bob calculates shared key: A^b mod p = {shared_key_bob}")
    
    # Verify keys are identical
    assert shared_key_alice == shared_key_bob, "Keys are not identical!"
    print(f"Shared key established: {shared_key_alice}")
    
    # Derive 256-bit AES key from shared key
    shared_bytes = shared_key_alice.to_bytes((shared_key_alice.bit_length() + 7) // 8, 'big')
    aes_key = hashlib.sha256(shared_bytes).digest()
    print(f"Derived AES-256 key: {aes_key.hex()}")
    
    return {
        'alice_private': a,
        'bob_private': b,
        'alice_public': A,
        'bob_public': B,
        'shared_key': shared_key_alice,
        'aes_key': aes_key
    }

def simple_aes_demo(aes_key, message):
    # Simple AES-like encryption demonstration
    print(f"\nEncryption/decryption demonstration with derived key:")
    print(f"Original message: {message}")
    
    # Use first 16 bytes as key
    print(f"Derived key (first 128 bits): {aes_key[:16].hex()}")
    
    # Convert message to bytes
    message_bytes = message.encode('utf-8')
    
    # Simple XOR encryption for demonstration
    encrypted_bytes = bytearray()
    key_bytes = aes_key[:16]  # 128 bits
    
    for i, byte in enumerate(message_bytes):
        encrypted_bytes.append(byte ^ key_bytes[i % len(key_bytes)])
    
    print(f"Encrypted message (hex): {encrypted_bytes.hex()}")
    
    # Decrypt (XOR again with same key)
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        decrypted_bytes.append(byte ^ key_bytes[i % len(key_bytes)])
    
    decrypted_message = decrypted_bytes.decode('utf-8')
    print(f"Decrypted message: {decrypted_message}")
    
    return encrypted_bytes, decrypted_message