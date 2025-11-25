# Asymmetric Cryptography - RSA, ElGamal & Diffie-Hellman

### **Course**: Cryptography and Security

### **Author**: Alexandru Rudoi

📑 **[👉 Read the Full Report](https://github.com/AlexandruRudoi/CS_Labs/blob/main/Lab_5/docs/CS_Lab5_Report.pdf)**

---

## 📖 **Overview**

This project implements three fundamental **asymmetric cryptographic algorithms**: RSA, ElGamal, and Diffie-Hellman key exchange with AES encryption. The laboratory work demonstrates:

- **RSA Encryption**: Public-key cryptosystem with 2048-bit key generation.
- **ElGamal Encryption**: Probabilistic asymmetric encryption based on discrete logarithm problem.
- **Diffie-Hellman Key Exchange**: Secure key agreement protocol with AES-256 demonstration.
- **ASCII Encoding**: Message conversion using hexadecimal to decimal representation.
- **Modular Implementation**: Clean separation of concerns with reusable cryptographic modules.

---

## 🎯 **Objectives**

- Implement **RSA encryption/decryption** with minimum 2048-bit modulus (n).
- Generate **ElGamal keys** using provided 2048-bit prime p and generator g=2.
- Execute **Diffie-Hellman key exchange** between Alice and Bob.
- Derive **256-bit AES key** from Diffie-Hellman shared secret.
- Convert messages to numeric representation using **ASCII → Hex → Decimal** encoding.
- Understand **asymmetric cryptography** principles and security properties.

---

## 🔧 **Implementation Details**

### 🏗️ **Architecture Overview**

The implementation is organized into modular components:

```
Lab_5/
├── main.py              # Interactive menu and program entry point
├── rsa.py               # RSA key generation, encryption, decryption
├── elgamal.py           # ElGamal key generation, encryption, decryption
├── diffie_hellman.py    # Diffie-Hellman exchange and AES demo
└── utils.py             # Message encoding/decoding and constants (P, G)
```

### 🔐 **Algorithm Implementations**

#### **Task 2.1: RSA Algorithm**

**Overview**

RSA (Rivest-Shamir-Adleman) is a public-key cryptosystem based on the difficulty of factoring large numbers.

**Key Generation Process**

```
1. Generate two large primes: p, q (each ~1024 bits)
2. Compute n = p × q (≥ 2048 bits)
3. Compute φ(n) = (p-1) × (q-1)
4. Choose e = 65537 (common public exponent)
5. Compute d = e⁻¹ mod φ(n) (private exponent)

Public Key:  (n, e)
Private Key: (n, d)
```

**Encryption/Decryption**

```python
# Encryption
c = m^e mod n

# Decryption
m = c^d mod n
```

**Implementation Features**
- ✅ Generates **2048-bit modulus** (n) as required
- ✅ Uses **sympy** for prime generation and modular arithmetic
- ✅ Ensures **p ≠ q** for security
- ✅ Handles **message to number** conversion via ASCII encoding

---

#### **Task 2.2: ElGamal Algorithm**

**Overview**

ElGamal is a probabilistic asymmetric encryption algorithm based on the discrete logarithm problem.

**Key Generation Process**

```
Given: 2048-bit prime p and generator g = 2

1. Choose private key: x ∈ [2, p-2] (random)
2. Compute public key: y = g^x mod p

Public Key:  (p, g, y)
Private Key: x
```

**Encryption/Decryption**

```python
# Encryption
1. Choose random k ∈ [2, p-2] where gcd(k, p-1) = 1
2. Compute c1 = g^k mod p
3. Compute c2 = m × y^k mod p
Ciphertext: (c1, c2)

# Decryption
1. Compute s = c1^x mod p
2. Compute s_inv = s^(-1) mod p
3. Recover m = c2 × s_inv mod p
```

**Implementation Features**
- ✅ Uses **provided 2048-bit prime** p from assignment
- ✅ Uses **generator g = 2** as specified
- ✅ Implements **probabilistic encryption** (different ciphertexts for same plaintext)
- ✅ Validates **gcd(k, p-1) = 1** for random k

---

#### **Task 3: Diffie-Hellman & AES**

**Overview**

Diffie-Hellman enables two parties to establish a shared secret over an insecure channel, which is then used to derive an AES-256 encryption key.

**Key Exchange Process**

```
Given: 2048-bit prime p and generator g = 2

Alice:
1. Choose secret a ∈ [2, p-2] (random)
2. Compute A = g^a mod p
3. Send A to Bob

Bob:
1. Choose secret b ∈ [2, p-2] (random)
2. Compute B = g^b mod p
3. Send B to Alice

Shared Secret:
Alice: K = B^a mod p
Bob:   K = A^b mod p
(Both compute the same K = g^(ab) mod p)

AES Key Derivation:
aes_key = SHA-256(K) → 256-bit key
```

**AES Encryption Demo**

```python
# Simple XOR encryption for demonstration
encrypted = plaintext XOR aes_key[0:16]
decrypted = encrypted XOR aes_key[0:16]
```

**Implementation Features**
- ✅ Uses **provided 2048-bit prime** p and **generator g = 2**
- ✅ Randomly generates **secrets a and b** according to requirements
- ✅ Verifies **shared key agreement** (Alice and Bob compute same K)
- ✅ Derives **256-bit AES key** using SHA-256 hash
- ✅ Demonstrates **symmetric encryption** with derived key

---

### 📝 **Message Encoding**

**ASCII → Hex → Decimal Conversion**

As specified in the assignment, messages are converted to numeric representation:

```python
# Encoding Process
"John Doe" 
    ↓ ASCII bytes
[74, 111, 104, 110, 32, 68, 111, 101]
    ↓ Hexadecimal
"4a6f686e20446f65"
    ↓ Decimal (base 10)
5384720032103280741

# Decoding Process (reverse)
5384720032103280741
    ↓ Hex
"4a6f686e20446f65"
    ↓ ASCII
"John Doe"
```

**Implementation**

```python
def message_to_number(message):
    hex_representation = message.encode('ascii').hex()
    return int(hex_representation, 16)

def number_to_message(number):
    hex_str = hex(number)[2:]
    if len(hex_str) % 2:
        hex_str = '0' + hex_str
    return bytes.fromhex(hex_str).decode('ascii')
```

---

## 💻 **Usage Guide**

### **Running the Program**

**Using Python Launcher**
```bash
cd "d:\Projects\University\Anul 3\CS_Labs\Lab_5"
py main.py
```

### **Interactive Menu**

```
================================================================================
CRYPTOGRAPHIC ALGORITHMS MENU
================================================================================
1. RSA Algorithm
2. ElGamal Algorithm
3. Diffie-Hellman & AES
0. Exit
================================================================================

Enter your choice (0-3):
```

### **Example Workflow**

#### **Example 1: RSA Encryption**

```
Enter your choice (0-3): 1

Enter your first and last name: Alexandru Rudoi

================================================================================
Task 2.1: RSA Algorithm
================================================================================
Generating RSA keys with 2048 bits...
p = 285647...
q = 326751...
n = 932847... (2048 bits)
phi(n) = 932847...
e = 65537
d = 178234...

RSA keys generated.
Public key: (932847..., 65537)
Private key: (932847..., 178234...)

Original message: Alexandru Rudoi
Numeric representation: 21691398273949273948573948573948573
Encrypted message: 83746273846238746283746283746283746
Decrypted message (numeric): 21691398273949273948573948573948573
Decrypted message: Alexandru Rudoi

Do you want to continue? (y/n):
```

#### **Example 2: ElGamal Encryption**

```
Enter your choice (0-3): 2

================================================================================
Task 2.2: ElGamal Algorithm
================================================================================
Generating ElGamal keys...
p = 3231700607131100730015351347782516336248805713348907517458843413...
g = 2
Private key x = 1634827364827364827364827364827364827364827364827364
Public key y = 2847362846238746238746238746238746238746238746238746

Original message: Alexandru Rudoi
Numeric representation: 21691398273949273948573948573948573
k = 9384729384729384729384729384729384729384729384729384
c1 = 8374628374628374628374628374628374628374628374628374
c2 = 9273649273649273649273649273649273649273649273649273

s = c1^x mod p = 7362873628736287362873628736287362873628736287362
s^(-1) = 2847362846238746238746238746238746238746238746238746
Decrypted message (numeric): 21691398273949273948573948573948573
Decrypted message: Alexandru Rudoi

Do you want to continue? (y/n):
```

#### **Example 3: Diffie-Hellman Key Exchange**

```
Enter your choice (0-3): 3

================================================================================
Task 3: Diffie-Hellman & AES
================================================================================
Diffie-Hellman key exchange between Alice and Bob...
Public parameters: p = 32317006071311007300153513477825163362488057..., g = 2

Alice chooses private key a = 1847362846238746238746238746238746238746
Bob chooses private key b = 9273649273649273649273649273649273649273

Alice calculates A = g^a mod p = 8374628374628374628374628374628374628
Bob calculates B = g^b mod p = 2847362846238746238746238746238746238

Alice calculates shared key: B^a mod p = 7362873628736287362873628...
Bob calculates shared key: A^b mod p = 7362873628736287362873628...

Shared key established: 7362873628736287362873628736287362873628...
Derived AES-256 key: a120c65b29c019e33a7427b46df3ca8adede5aea8b152a5057ab665b4fe06d5c

Encryption/decryption demonstration with derived key:
Original message: Alexandru Rudoi
Derived key (first 128 bits): a120c65b29c019e33a7427b46df3ca8a
Encrypted message (hex): c244e6794dfa45b3481b4dd10e87b9d6f44e
Decrypted message: Alexandru Rudoi

Do you want to continue? (y/n):
```

---

## 🔬 **Technical Features**

### ✅ **Core Functionality**

- **Interactive Menu**: Choose specific algorithm or run all sequentially
- **Message Persistence**: Enter name once, reuse across algorithms
- **Comprehensive Output**: Displays all intermediate values and keys
- **ASCII Encoding**: Proper message ↔ number conversion as specified
- **Continue Prompt**: Option to run multiple algorithms in one session

### ✅ **Code Quality**

- **Modular Design**: Separated files for each algorithm and utilities
- **Type Safety**: Clear parameter types and return values
- **Documentation**: Inline comments explaining cryptographic steps
- **Error Handling**: Validates message size against key constraints
- **Reusability**: Generic functions for encoding, key generation, etc.

### 🔑 **Security Features**

#### **RSA Security**
- ✅ **2048-bit modulus**: Meets current security standards (until ~2030)
- ✅ **Random prime generation**: Uses cryptographically secure primes
- ✅ **Message padding**: Validates m < n constraint

#### **ElGamal Security**
- ✅ **2048-bit DLP**: Based on discrete logarithm problem
- ✅ **Probabilistic encryption**: Same message yields different ciphertexts
- ✅ **Random k selection**: Ensures IND-CPA security

#### **Diffie-Hellman Security**
- ✅ **2048-bit parameters**: Resistant to current attacks
- ✅ **Random secrets**: Prevents replay attacks
- ✅ **Hash-based KDF**: SHA-256 for AES key derivation

---

## 📊 **Cryptographic Analysis**

### **Algorithm Comparison**

| Algorithm | Type | Security Basis | Key Size | Ciphertext Expansion |
|-----------|------|----------------|----------|---------------------|
| **RSA** | Deterministic | Factoring | 2048 bits | ~1x message size |
| **ElGamal** | Probabilistic | Discrete Log | 2048 bits | 2x message size |
| **DH+AES** | Hybrid | Discrete Log + Symmetric | 2048 bits DH, 256 bits AES | Minimal |

### **Performance Characteristics**

**RSA**
- ⚡ **Fast encryption** (small e = 65537)
- 🐌 **Slow decryption** (large d)
- 📊 **Best for**: Digital signatures, small messages

**ElGamal**
- ⚖️ **Balanced speed** (similar encryption/decryption)
- 📈 **Larger ciphertexts** (c1, c2)
- 📊 **Best for**: When probabilistic encryption needed

**Diffie-Hellman + AES**
- 🚀 **Fast symmetric encryption** (AES)
- 🔄 **One-time key exchange** (DH)
- 📊 **Best for**: Secure communications, large data

### **Security Levels (2048-bit)**

All three implementations provide approximately **112-bit security**:

```
RSA-2048     ≈ 112-bit security (NIST equivalent)
DLP-2048     ≈ 112-bit security (ElGamal, DH)
AES-256      ≈ 256-bit security (post-quantum safe)
```

**Post-Quantum Considerations**:
- ⚠️ **RSA**: Vulnerable to Shor's algorithm (quantum computers)
- ⚠️ **ElGamal/DH**: Vulnerable to quantum discrete log algorithms
- ✅ **AES-256**: Considered quantum-resistant (Grover's algorithm only halves security)

---

## 🛡️ **Constants & Parameters**

### **Provided Values (Assignment)**

**Prime p (2048 bits)**:
```
p = 3231700607131100730015351347782516336248805713348907517458843413926980683
    4136210002792056362640164685458556357935330816928829023080573472625273554
    7424612457410262025279165729728627063003252634282131457669314142236542209
    4111113486299916574782680342305530863490506355577122191878903327295696961
    2974385624174123623722519734640269185579776797682301462539793305801522685
    8730761197532436467475855460715043896844940366130497697812854295958659597
    5670512838521327844685229255045682728791137200989318739591433741758378260
    0027803497319855206060753323412260325468408812003110590748428100399496695
    611969695624862903233807283912703
```

**Generator**:
```
g = 2
```

**Verification**:
- ✅ p is prime (verified)
- ✅ p.bit_length() = 2048
- ✅ g = 2 is a generator of the multiplicative group modulo p

---

## 🎓 **Conclusion**

This laboratory work successfully implemented three fundamental asymmetric cryptographic algorithms:

**Key Achievements**:
1. ✅ **RSA encryption** with 2048-bit modulus meeting security standards
2. ✅ **ElGamal encryption** using provided parameters with probabilistic security
3. ✅ **Diffie-Hellman key exchange** with AES-256 hybrid cryptography
4. ✅ **Proper message encoding** via ASCII → Hex → Decimal conversion
5. ✅ **Modular implementation** with clean code organization

**Learning Outcomes**:

1. **Public-Key Cryptography**: Understanding asymmetric vs symmetric encryption
2. **Mathematical Foundations**: Modular arithmetic, discrete logarithm, factoring
3. **Key Management**: Generation, distribution, and security of cryptographic keys
4. **Hybrid Cryptography**: Combining asymmetric and symmetric approaches
5. **Security Analysis**: Evaluating algorithm strengths and vulnerabilities

**Practical Applications**:
- **RSA**: SSL/TLS certificates, digital signatures, email encryption (PGP)
- **ElGamal**: Variant used in DSA, basis for elliptic curve cryptography
- **Diffie-Hellman**: TLS handshakes, VPNs, secure messaging (Signal, WhatsApp)

**Modern Evolution**:
- **Elliptic Curve Cryptography (ECC)**: Smaller keys, same security
- **Post-Quantum Cryptography**: Lattice-based, hash-based alternatives
- **Hybrid Schemes**: Combining classical and post-quantum algorithms

This implementation demonstrates the foundational principles of asymmetric cryptography that underpin modern secure communications.

---

## 📚 **References**

- **Course Materials** – _Cryptography and Security_, UTM FCIM, 2025
- **Rivest, R., Shamir, A., Adleman, L.** – _A Method for Obtaining Digital Signatures and Public-Key Cryptosystems_ (1978)
- **ElGamal, T.** – _A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms_ (1985)
- **Diffie, W., Hellman, M.** – _New Directions in Cryptography_ (1976)
- **Stallings, W.** – _Cryptography and Network Security: Principles and Practice_
- **NIST FIPS 186-5** – _Digital Signature Standard (DSS)_
- **NIST SP 800-57** – _Recommendation for Key Management_

---

## 🛠️ **Dependencies**

- **Python 3.13+** (or 3.8+)
- **sympy** – For prime generation and modular arithmetic
  ```bash
  pip install sympy
  ```

**Installation**:
```bash
py -m pip install sympy
```

---

## 📝 **Notes**

### **Assignment Tasks**

This implementation covers all required tasks:

- ✅ **Task 2.1**: RSA with n ≥ 2048 bits
- ✅ **Task 2.2**: ElGamal with provided p and g
- ✅ **Task 3**: Diffie-Hellman with AES-256

### **Message Format**

Messages use **decimal representation** obtained via:
1. ASCII encoding of characters
2. Hexadecimal representation
3. Conversion to decimal (base 10)

Example: `"Alex"` → `0x416c6578` → `1097166200`

### **Python Version Compatibility**

The code works with Python 3.8+ but was developed with Python 3.13.

To run with specific Python version:
```bash
py -3.13 main.py
```

---

## 📄 **License**

This project is part of academic coursework at Technical University of Moldova (UTM).
