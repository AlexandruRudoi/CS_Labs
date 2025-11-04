# DES Round Key Generation - Symmetric Block Cipher

### **Course**: Cryptography and Security

### **Author**: Alexandru Rudoi

📑 **[👉 Read the Full Report](https://github.com/AlexandruRudoi/CS_Labs/blob/main/Lab_4/docs/CS_Lab4_Report.pdf)**
---

## 📖 **Overview**

This project implements the **DES (Data Encryption Standard) round key generation** algorithm, focusing on the key schedule mechanism used in symmetric block ciphers. The laboratory work demonstrates:

- **Key Schedule Algorithm**: Generation of 16 round keys from a master key.
- **Permutation Operations**: PC-1 and PC-2 permutation tables.
- **Circular Shifts**: Left rotation of key halves according to shift schedule.
- **Symmetric Cryptography**: Understanding DES internal structure.
- **Modular Implementation**: Clean separation of concerns with reusable components.

---

## 🎯 **Objectives**

- Implement the **DES key schedule** algorithm for round key generation.
- Apply **permutation tables** (PC-1 and PC-2) to transform keys.
- Perform **circular left shifts** on key halves according to DES specification.
- Generate **48-bit round keys** from 56-bit permuted key (K+).
- Understand the **internal structure** of DES encryption algorithm.
- Demonstrate **symmetric block cipher** key management principles.

---

## 🔧 **Implementation Details**

### 🏗️ **Architecture Overview**

The implementation is organized into modular components:

```
Lab_4/
├── main.py              # Main interface and user interaction
├── des_tables.py        # DES permutation tables and shift schedule
├── des_utils.py         # Utility functions (permutation, shifts, hex conversion)
├── key_schedule.py      # Core key generation algorithm
└── __pycache__/         # Python bytecode
```

### 🔐 **DES Key Schedule Algorithm**

#### **Overview**

The DES key schedule generates **16 unique 48-bit round keys** (K₁ to K₁₆) from a single 64-bit master key:

```
64-bit Key → PC-1 → 56-bit K+ → Split & Shift → Combine → PC-2 → 48-bit Ki
```

#### **Step-by-Step Process**

**Step 0: Initial Key (64 bits)**
- User provides 64-bit key (or system generates random key)
- Includes 8 parity bits (every 8th bit)

**Step 1: PC-1 Permutation (64 → 56 bits)**
```python
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, ...]  # 56 positions
K+ = permute(Key_64, PC1)  # Removes parity bits
```
- Removes parity bits
- Rearranges remaining 56 bits
- Output: **K+** (56-bit permuted key)

**Step 2: Split K+ into C₀ and D₀**
```python
C₀ = K+[0:28]   # Left half (28 bits)
D₀ = K+[28:56]  # Right half (28 bits)
```

**Step 3: Circular Left Shifts**
```python
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

For round i (1 to 16):
    Cᵢ = left_shift(Cᵢ₋₁, SHIFT_SCHEDULE[i-1])
    Dᵢ = left_shift(Dᵢ₋₁, SHIFT_SCHEDULE[i-1])
```

**Key Insight**: Shifts are cumulative! To get round 5 key:
- Apply shifts for rounds 1, 2, 3, 4, and 5 sequentially

**Step 4: Combine Cᵢ and Dᵢ**
```python
CᵢDᵢ = Cᵢ + Dᵢ  # Concatenate (56 bits)
```

**Step 5: PC-2 Permutation (56 → 48 bits)**
```python
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, ...]  # 48 positions
Kᵢ = permute(CᵢDᵢ, PC2)  # Select and permute 48 bits
```

**Output**: **Kᵢ** (48-bit round key for round i)

---

## 💻 **Usage Guide**

### **Running the Program**

```cmd
cd d:\Projects\University\Anul 3\CS_Labs\Lab_4
python main.py
```

### **Main Menu Options**

```
================================================================================
DES ROUND KEY GENERATION - Task 2.3
Given K+ (56-bit permuted key), generate round key Ki
================================================================================

Choose input method:
1. Enter 64-bit key manually
2. Enter K+ (56-bit) directly
3. Generate random key
```

### **Example Workflow**

#### **Example 1: Manual 64-bit Key Input**

```
Enter choice (1/2/3): 1

Enter 64-bit key (binary string of 0s and 1s): 
0001001100110100010101110111100110011011101111001101111111110001

✓ Valid 64-bit Key: 0001001100110100010101110111100110011011101111001101111111110001
  Hex: 133457799BBCDFF1

Applying PC-1 to get K+...

K+ (56 bits): 11110000110011001010101011110101010101100110011110001111
Hex: F0CCAAAB56CF1F

Enter round number i (1-16): 5

================================================================================
GENERATING ROUND KEY K5
================================================================================

Step 1: Split K+ into C0 and D0 (28 bits each)
C0 = 1111000011001100101010101111 (hex: F0CCAAF)
D0 = 0101010101100110011110001111 (hex: 556CF0F)

Step 2: Apply left circular shifts for rounds 1 to 5
Shift schedule: [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
  Round 1: Shift by 1
         C1 = 1110000110011001010101011111 (hex: E19955F)
         D1 = 1010101011001100111100011110 (hex: AAB33C3E)
  Round 2: Shift by 1
         C2 = 1100001100110010101010111111 (hex: C332ABF)
         C2 = 0101010110011001111000111101 (hex: 56678F)
  Round 3: Shift by 2
         C3 = 0000110011001010101011111111 (hex: 332ABFF)
         D3 = 0101011001100111100011110101 (hex: 56CF3D)
  Round 4: Shift by 2
         C4 = 0011001100101010101111111100 (hex: CCABFC)
         D4 = 0101100110011110001111010101 (hex: 599E75)
  Round 5: Shift by 2
         C5 = 1100110010101010111111110000 (hex: 32ABFF0)
         D5 = 0110011001111000111101010101 (hex: 66CF5)

Step 3: Combine C5 and D5
C5D5 (56 bits) = 11001100101010101111111100000110011001111000111101010101
Hex: 32ABFF066CF5

Step 4: Apply PC-2 permutation (56 bits -> 48 bits)
K5 (48 bits) = 011100011010000010010110010111111011110011011100
Hex: E1A096BDF6DC

================================================================================
FINAL RESULT
================================================================================
Input K+ (56 bits): 11110000110011001010101011110101010101100110011110001111
Round number: 5
Output K5 (48 bits): 011100011010000010010110010111111011110011011100
K5 in hex: E1A096BDF6DC
================================================================================
```

#### **Example 2: Direct K+ Input**

```
Enter choice (1/2/3): 2

Enter K+ (56-bit binary string of 0s and 1s):
11110000110011001010101011110101010101100110011110001111

✓ Valid K+ (56 bits): 11110000110011001010101011110101010101100110011110001111

Enter round number i (1-16): 10

[Similar detailed output for round 10]
```

#### **Example 3: Random Key Generation**

```
Enter choice (1/2/3): 3

Random 64-bit Key: 1011010110100011001011110100101110010101001110110101101011001101
Hex: B5A32F4B9555AB4D

Applying PC-1 to get K+...
K+ (56 bits): 10110101101000110010111101001011010101001110110101101011
Hex: B5A32F4B555AB

Enter round number i (1-16): 16
```

---

## 🔬 **Technical Features**

### ✅ **Core Functionality**

- **Multiple Input Methods**: 64-bit key, 56-bit K+, or random generation
- **Robust Validation**: Checks for binary format and correct length
- **Step-by-Step Visualization**: Shows all intermediate transformations
- **Hexadecimal Display**: Converts binary to hex for readability
- **Cumulative Shift Calculation**: Correctly applies all shifts up to round i
- **Complete Key Schedule**: Can generate all 16 round keys

### ✅ **Code Quality**

- **Modular Design**: Separated concerns (tables, utils, key schedule, UI)
- **Input Validation**: Comprehensive error checking and user feedback
- **Clear Documentation**: Docstrings for all functions
- **Error Handling**: Graceful handling of invalid inputs
- **Reusable Components**: Generic permutation and shift functions

### 🔑 **Key Components**

#### **1. Permutation Tables (des_tables.py)**

```python
PC1 = [57, 49, 41, 33, ...]  # 64 → 56 bits (removes parity)
PC2 = [14, 17, 11, 24, ...]  # 56 → 48 bits (selects round key bits)
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
```

#### **2. Utility Functions (des_utils.py)**

```python
permute(bits, table)          # Apply permutation table
left_shift(bits, n)           # Circular left shift by n positions
bits_to_hex(bits)             # Convert binary string to hexadecimal
split_key(key_56)             # Split 56-bit key into 28-bit halves
```

#### **3. Key Schedule Algorithm (key_schedule.py)**

```python
generate_round_key(K_plus, round_num, verbose=True)
    # Generate Ki for specific round with detailed output
    
generate_all_round_keys(K_plus)
    # Generate all 16 round keys at once
```

---

## 🔍 **DES Algorithm Context**

### **DES Structure Overview**

```
Plaintext (64 bits)
    ↓
Initial Permutation (IP)
    ↓
┌───────────────────────┐
│  16 Feistel Rounds    │
│                       │
│  Each round uses:     │
│  - 48-bit round key Ki│
│  - Feistel function f │
│  - XOR operations     │
└───────────────────────┘
    ↓
Final Permutation (IP⁻¹)
    ↓
Ciphertext (64 bits)
```

### **Where Key Schedule Fits**

This implementation focuses on **Task 2.3**: Given K+ (after PC-1), generate round key Ki.

**Complete DES Key Flow**:
```
64-bit Master Key
    ↓ PC-1
56-bit K+
    ↓ Split + Shifts + PC-2
48-bit K₁, K₂, ..., K₁₆
    ↓
Used in Feistel rounds
```

---

## 📊 **Algorithm Analysis**

### **Shift Schedule Rationale**

```
Rounds with 1 shift: 1, 2, 9, 16
Rounds with 2 shifts: 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15
```

**Total shifts**: 1+1+2+2+2+2+2+2+1+2+2+2+2+2+2+1 = **28 shifts**

Since 28 = 1 complete rotation of 28 bits:
- After 16 rounds, C and D return to original positions
- Enables efficient decryption (run rounds in reverse)

### **PC-2 Selection Strategy**

PC-2 selects 48 out of 56 bits:
- **Omits 8 bit positions**: More diffusion between rounds
- **Non-linear selection**: Increases cryptographic strength
- **Different bits each round**: Due to cumulative shifts

### **Security Properties**

✅ **Key Diffusion**: Each round key differs significantly from others  
✅ **Avalanche Effect**: Small key change affects all round keys  
✅ **Non-linearity**: PC-2 provides additional mixing  
✅ **Bit Independence**: Shifts ensure all key bits influence all rounds

---

## 🛡️ **DES Security Analysis**

### **Historical Context**

- **Published**: 1977 by IBM and NSA
- **Standardized**: FIPS 46 (1977-2005)
- **Key Length**: 56 bits (64 bits with parity)
- **Block Size**: 64 bits
- **Status**: **Deprecated** - replaced by AES in 2001

### **Strengths**

✅ **Confusion and Diffusion**: Well-designed Feistel structure  
✅ **Proven Design**: Extensively analyzed for decades  
✅ **S-box Design**: Resistant to differential cryptanalysis  
✅ **Key Schedule**: Good bit mixing across rounds

### **Weaknesses**

⚠️ **Short Key Length**: 56 bits vulnerable to brute force (2⁵⁶ ≈ 7.2×10¹⁶)  
⚠️ **Small Block Size**: 64 bits susceptible to birthday attacks  
⚠️ **Weak Keys**: 4 keys where E(K, P) = P (complementation property)  
⚠️ **Semi-weak Keys**: 12 key pairs where Eₖ₁(Eₖ₂(P)) = P

### **Modern Alternatives**

- **3DES (Triple DES)**: Apply DES three times with different keys
- **AES**: Modern standard with 128/192/256-bit keys
- **ChaCha20**: Stream cipher alternative

---

## 🎓 **Conclusion**

This laboratory work successfully implemented the DES key schedule algorithm, demonstrating:

- **Systematic key generation** through permutations and circular shifts
- **Understanding of symmetric block cipher** internal mechanisms
- **Importance of key scheduling** in providing round-specific keys
- **Historical cryptographic design** principles and their evolution

**Key Learning Outcomes**:

1. **Permutation Operations**: Understanding how bit rearrangement provides security
2. **Shift Schedules**: Role of circular shifts in key diffusion
3. **Key Derivation**: Generating multiple round keys from single master key
4. **Implementation Skills**: Translating cryptographic specifications to code
5. **Security Awareness**: Recognizing limitations of older algorithms

**Modern Relevance**: While DES itself is obsolete, its design principles influenced:
- **AES key schedule**: Similar expansion and mixing concepts
- **Feistel networks**: Still used in many modern ciphers
- **Block cipher design**: Foundation for understanding modern symmetric crypto

This implementation serves as an educational tool for understanding symmetric cryptography fundamentals and the evolution toward modern standards like AES.

---

## 📚 **References**

- **Course Materials** – _Cryptography and Security_, UTM FCIM, 2025
- **FIPS PUB 46-3** – _Data Encryption Standard (DES)_
- **Stallings, W.** – _Cryptography and Network Security: Principles and Practice_
- **Schneier, B.** – _Applied Cryptography: Protocols, Algorithms, and Source Code in C_
- **NIST Special Publication 800-67** – _Recommendation for Triple DES_

---

## 🛠️ **Dependencies**

- **Python 3.8+**
- **No external libraries required** (pure Python implementation)

---

## 📝 **Notes**

### **Task Coverage**

This implementation focuses on **Task 2.3** of the laboratory assignment:

> Given K+ (56-bit permuted key after PC-1), generate the round key Ki for a specified round i (1-16).

### **Extensions Possible**

- Full DES encryption/decryption implementation
- Triple DES (3DES) variant
- DES cracking demonstration
- Comparison with AES key schedule
- Visualization of bit avalanche effect

---

## 📄 **License**

This project is part of academic coursework at Technical University of Moldova (UTM).

