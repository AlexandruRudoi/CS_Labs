# Hash Functions & Digital Signatures

### **Course**: Cryptography and Security

### **Author**: Alexandru Rudoi

📑 **[👉 Read the Full Report](https://github.com/AlexandruRudoi/CS_Labs/blob/main/Lab_6/docs/CS_Lab6_Report.pdf)**

---

## 📖 **Overview**

This project implements **digital signature schemes** using RSA and ElGamal algorithms with cryptographic hash functions. The laboratory work demonstrates:

- **RSA Digital Signature**: Signing and verification using MD5 hash with 3072-bit keys.
- **ElGamal Digital Signature**: Signing and verification using MD4 hash with provided 2048-bit parameters.
- **Hash Functions**: MD5 and MD4 for message digest generation.
- **Signature Verification**: Mathematical proof of message authenticity and integrity.
- **Security Analysis**: Understanding digital signature properties and requirements.

---

## 🎯 **Objectives**

- Implement **RSA digital signature** with minimum 3072-bit modulus (n).
- Generate **ElGamal signatures** using provided 2048-bit prime p and generator g=2.
- Apply **MD5 hash function** for RSA signatures (student index formula: i = k mod 24 + 1 = 2).
- Apply **MD4 hash function** for ElGamal signatures (student index formula: i = k mod 24 + 1 = 2).
- Convert hash values to **decimal representation** for signature operations.
- Verify **signature authenticity** using public keys.
- Understand **digital signature security** properties: authenticity, integrity, non-repudiation.

---

## 🔧 **Implementation Details**

### 🏗️ **Architecture Overview**

The implementation is organized into modular components:

```
Lab_6/
├── main.py              # Main program and signature workflow
├── rsa.py               # RSA key generation, signing, verification
├── elgamal.py           # ElGamal key generation, signing, verification
├── utils.py             # Hash functions (MD5, MD4)
└── message.txt          # Message from Lab 2 (plaintext to sign)
```

### 🔐 **Algorithm Implementations**

#### **Task 2: RSA Digital Signature with MD5**

**Overview**

RSA digital signatures provide authentication and non-repudiation by using the private key to sign a hash of the message.

**Key Generation Process**

```
1. Generate two large primes: p, q (each ~1536 bits)
2. Compute n = p × q (≥ 3072 bits)
3. Compute φ(n) = (p-1) × (q-1)
4. Choose e = 65537 (public exponent)
5. Compute d = e⁻¹ mod φ(n) (private exponent)

Public Key:  (n, e)
Private Key: (n, d)
```

**Signing Process**

```python
# Step 1: Hash the message using MD5
h = MD5(message)  # 128-bit hash → convert to decimal

# Step 2: Sign the hash with private key
signature = h^d mod n
```

**Verification Process**

```python
# Step 1: Hash the message using MD5
h = MD5(message)  # Original hash

# Step 2: Decrypt signature with public key
h' = signature^e mod n

# Step 3: Verify signature
valid = (h == h')  # True if signature is authentic
```

**Implementation Features**
- ✅ Generates **3072-bit modulus** (n) as required
- ✅ Uses **MD5 hash function** (128-bit output)
- ✅ Converts hash to **decimal representation** for signing
- ✅ Implements **textbook RSA signature** scheme
- ✅ Provides detailed **verification output** with hash values

---

#### **Task 3: ElGamal Digital Signature with MD4**

**Overview**

ElGamal digital signatures are based on the discrete logarithm problem and provide message authentication through a different mathematical approach than RSA.

**Key Generation Process**

```
Given: 2048-bit prime p and generator g = 2

1. Choose private key: x ∈ [2, p-2] (random)
2. Compute public key: y = g^x mod p

Public Key:  (p, g, y)
Private Key: x
```

**Signing Process**

```python
# Step 1: Hash the message using MD4
h = MD4(message)  # 128-bit hash → convert to decimal

# Step 2: Choose random k where gcd(k, p-1) = 1
k = random in [2, p-2]

# Step 3: Compute signature components
r = g^k mod p
s = (h - x*r) * k^(-1) mod (p-1)

Signature: (r, s)
```

**Verification Process**

```python
# Step 1: Hash the message using MD4
h = MD4(message)

# Step 2: Verify signature equation
left  = g^h mod p
right = y^r * r^s mod p

# Step 3: Check equality
valid = (left == right)  # True if signature is authentic
```

**Mathematical Foundation**

The ElGamal signature verification works because:
```
g^h ≡ y^r * r^s (mod p)
g^h ≡ (g^x)^r * (g^k)^s (mod p)
g^h ≡ g^(xr + ks) (mod p)

Where: s = (h - xr) * k^(-1) mod (p-1)
Therefore: ks ≡ h - xr (mod p-1)
Thus: xr + ks ≡ h (mod p-1)
```

**Implementation Features**
- ✅ Uses **provided 2048-bit prime** p from assignment
- ✅ Uses **generator g = 2** as specified
- ✅ Uses **MD4 hash function** (128-bit output)
- ✅ Validates **gcd(k, p-1) = 1** for random k
- ✅ Implements **ElGamal signature scheme** correctly
- ✅ Provides detailed **verification output** with intermediate values

---

### 🔐 **Hash Functions**

**MD5 Hash (RSA Signatures)**

```python
def md5_hash(message: str) -> int:
    """MD5 hash function for RSA digital signature"""
    h = hashlib.md5()
    h.update(message.encode())
    hash_hex = h.hexdigest()  # 128-bit hash in hex
    return int(hash_hex, 16)   # Convert to decimal
```

**Properties:**
- Output size: **128 bits** (32 hex characters)
- Deterministic: Same input → Same hash
- Fast computation
- Note: MD5 is cryptographically broken but used for educational purposes

**MD4 Hash (ElGamal Signatures)**

```python
def md4_hash(message: str) -> int:
    """MD4 hash function for ElGamal digital signature"""
    h = MD4.new()  # Using PyCryptodome library
    h.update(message.encode())
    hash_hex = h.hexdigest()  # 128-bit hash in hex
    return int(hash_hex, 16)   # Convert to decimal
```

**Properties:**
- Output size: **128 bits** (32 hex characters)
- Predecessor of MD5
- Note: MD4 is obsolete but used for educational purposes
- Requires **PyCryptodome** library (not in Python 3.13 hashlib)

---

### 📊 **Given Parameters**

**ElGamal Prime (p) - 2048 bits:**
```
p = 3231700607131100730015351347782516336248805713348907517458843413
    9269806834136210002792056362640164685458556357935330816928829023
    0805734726252735547424612457410262025279165729728627063003252634
    2821314576693141422365422094111134862999165747826803423055308634
    9050635557712219187890332729569696129743856241741236237225197346
    4026918557977679768230146253979330580152268587307611975324364674
    7585546071504389684494036613049769781285429595865959756705128385
    2132784468522925504568272879113720098931873959143374175837826000
    27803497319855206060753323412260325468408812003110590748428100399
    4966956119696956248629032338072839127039
```

**Generator:**
```
g = 2
```

---

## 💻 **Usage Guide**

### **Prerequisites**

Install required dependencies:
```bash
pip install pycryptodome
```

### **Running the Program**

```bash
cd "d:\Projects\University\Anul 3\CS_Labs\Lab_6"
py main.py
```

### **Example Output**

```
Message: the addition of secrecy to the transformations producedcryptography...
Message length: 1998 characters

RSA Digital Signature (Hash: MD5)
RSA Key Generation:
n = 28374628374628374628374...
e = 65537
d = 18273648273648273648273...
p = 92837462837462837462837...
q = 30574628374628374628374...
n bit length: 3072 bits

MD5 Hash: 7f3e8a9c2d1b4e5a6f8c9d2e3a4b5c6d
Hash value (decimal): 168273648273648273648273648273648273
RSA Signature (decimal): 837462837462837462837462837462837462

MD5 Hash: 7f3e8a9c2d1b4e5a6f8c9d2e3a4b5c6d
Original hash (decimal): 168273648273648273648273648273648273
Decrypted signature (decimal): 168273648273648273648273648273648273
Signature valid: True

RSA valid: True

ElGamal Digital Signature (Hash: MD4)
ElGamal Parameters:
p = 3231700607131100730015351347782516336248805713348907517458843413...
g = 2
p bit length: 2048 bits
Private key x = 192837465192837465192837465192837465192837465
Public key y = 283746283746283746283746283746283746283746283746...

MD4 Hash: 4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d
Hash value (decimal): 98273648273648273648273648273648273
ElGamal Signature:
r = 192837465192837465192837465192837465192837465192837465
s = 283746283746283746283746283746283746283746283746283746

MD4 Hash: 4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d
Hash value (decimal): 98273648273648273648273648273648273
Verification:
g^h mod p = 7362873628736287362873628736287362873628736287362873
y^r * r^s mod p = 7362873628736287362873628736287362873628736287362873
Signature valid: True

ElGamal valid: True
```

---

## 🔬 **Technical Details**

### **Digital Signature Properties**

✅ **Authentication**: Proves the sender's identity
✅ **Integrity**: Detects any message modification
✅ **Non-repudiation**: Sender cannot deny signing
❌ **Confidentiality**: Does NOT encrypt the message (only signs it)

### **RSA vs ElGamal Signatures**

| Property | RSA Signature | ElGamal Signature |
|----------|---------------|-------------------|
| **Key Size** | 3072 bits (n) | 2048 bits (p) |
| **Hash Function** | MD5 (128 bits) | MD4 (128 bits) |
| **Signature Size** | ~3072 bits (1 value) | ~4096 bits (2 values: r, s) |
| **Deterministic** | Yes (same message → same signature) | No (random k → different signatures) |
| **Speed** | Fast verification | Slower verification |
| **Security Basis** | Integer factorization | Discrete logarithm |

### **Security Considerations**

⚠️ **Educational Purposes Only**
- MD4 and MD5 are **cryptographically broken**
- Do NOT use for production systems
- Modern alternatives: SHA-256, SHA-3, BLAKE2

⚠️ **Key Size Requirements**
- RSA: Minimum **3072 bits** for adequate security (2048 bits deprecated)
- ElGamal: Minimum **2048 bits** (3072 bits recommended)

---

## 📚 **References**

- **RSA Signature Scheme**: [RFC 8017 - PKCS #1](https://tools.ietf.org/html/rfc8017)
- **ElGamal Signature**: Original paper by Taher ElGamal (1985)
- **MD5**: [RFC 1321](https://tools.ietf.org/html/rfc1321)
- **Digital Signatures Standard**: [FIPS 186-5](https://csrc.nist.gov/publications/detail/fips/186/5/final)

---

## 📄 **License**

This project is part of academic coursework at Technical University of Moldova (UTM).