# Playfair Cipher - Polyalphabetic Cipher Implementation

### **Course**: Cryptography and Security

### **Author**: Alexandru Rudoi

📑 **[👉 Read the Full Report](https://github.com/AlexandruRudoi/CS_Labs/blob/main/Lab_3/docs/CS_Lab3_Report.pdf)**

---

## 📖 **Overview**

This project implements the **Playfair cipher**, a classical polyalphabetic substitution cipher that encrypts digraphs (pairs of letters) instead of single characters. The laboratory work demonstrates:

- **Matrix-based encryption**: Key-dependent 5×5 (or custom) matrix construction.
- **Digraph substitution**: Processing text in pairs for enhanced security.
- **Multi-alphabet support**: Romanian, English, Russian, and custom alphabets.
- **Object-oriented design**: Clean, modular architecture with separation of concerns.
- **Interactive interface**: User-friendly console application for encryption/decryption.

---

## 🎯 **Objectives**

- Implement the **Playfair cipher** algorithm with matrix-based substitution.
- Support **multiple alphabet configurations** (Romanian, English, Russian, custom).
- Handle **digraph encryption rules**: same row, same column, rectangle.
- Create a **flexible architecture** that adapts to different alphabet sizes.
- Develop an **interactive user interface** for practical cipher operations.
- Demonstrate **classical cryptography techniques** and their limitations.

---

## 🔧 **Implementation Details**

### 🏗️ **Architecture Overview**

The implementation follows a **clean architecture pattern** with distinct layers:

```
src/
├── playfair.py              # Main facade - coordinates all components
├── core/                    # Core cryptographic logic
│   ├── cryptographer.py     # Encryption/decryption algorithms
│   ├── matrix.py           # Matrix construction and operations
│   └── validator.py        # Input validation
├── alphabet/               # Alphabet configurations
│   ├── config.py          # AlphabetConfig class
│   └── configs.py         # Predefined alphabet factory
├── ui/                    # User interface
│   └── interface.py       # Interactive console UI
└── utils/                 # Helper utilities
    └── helpers.py         # Matrix calculations, text preprocessing
```

### 🔐 **Playfair Cipher Algorithm**

#### **Matrix Construction**
1. Remove duplicate letters from the key
2. Fill matrix with key letters first
3. Append remaining alphabet letters in order
4. One letter is excluded as separator (handles duplicate pairs)

#### **Encryption Rules**

For each pair of letters (a, b):

1. **Same Row**: Replace with letters to the right (wrap around)
   ```
   Row: [A B C D E]
   BE → CD
   ```

2. **Same Column**: Replace with letters below (wrap around)
   ```
   Column: [A F K P U]
   FK → KP
   ```

3. **Rectangle**: Swap with opposite corners
   ```
   A B C     If encrypting BD:
   D E F  →  B→E, D→C  →  EC
   G H I
   ```

#### **Text Preprocessing**
- Convert to uppercase
- Insert separator between duplicate letters (AA → AKA)
- Pad with separator if odd length

### 📊 **Supported Alphabets**

#### **Romanian (30 letters)**
- **Alphabet**: `AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ`
- **Separator**: `K` (least frequent in Romanian)
- **Matrix**: 5×6

#### **English (25 letters)**
- **Alphabet**: `ABCDEFGHIKLMNOPQRSTUVWXYZ` (J excluded)
- **Separator**: `J`
- **Matrix**: 5×5

#### **Russian (32 letters)**
- **Alphabet**: `АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ` (Ё excluded)
- **Separator**: `Ё`
- **Matrix**: 4×8 or optimal rectangular

#### **Custom Alphabets**
- Define your own alphabet
- Automatic or manual separator selection
- Dynamic matrix dimension calculation

---

## 💻 **Usage Guide**

### **Running the Application**

```cmd
cd d:\Projects\University\Anul 3\CS_Labs\Lab_3
python main.py
```

### **Main Menu Options**

```
==================================================
     CIFRUL PLAYFAIR
==================================================
1. Criptare
2. Decriptare
3. Afișare matrice
4. Schimbare alfabet
5. Informații despre alfabet
6. Ieșire
==================================================
```

### **Example Workflow**

#### **Encryption Example**

```
Alegeți opțiunea: 1
Introduceți cheia: SECURITATE
Introduceți textul de criptat: CRIPTOGRAFIE

Textul original: CRIPTOGRAFIE
Criptograma: DESQUPITBSHKF

Doriți să vedeți matricea folosită? (d/n): d

Matricea Playfair (5×6):
S E C U R I
T A Ă Â B D
F G H Î J L
M N O P Q Ș
Ț V W X Y Z

Litera exclusă din alfabet (folosită ca separator): K
Alfabetul folosit în matrice: AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ
```

#### **Decryption Example**

```
Alegeți opțiunea: 2
Introduceți cheia: SECURITATE
Introduceți criptograma: DESQUPITBSHKF

Criptograma: DESQUPITBSHKF
Textul decriptat: CRIPTOGRAFIE
```

#### **Switching Alphabets**

```
Alegeți opțiunea: 4

--- Selectare Alfabet ---
1. Română (30 litere, separator: K)
2. Engleză (25 litere, separator: J)
3. Rusă (32 litere, separator: Ё)
4. Alfabet personalizat
5. Înapoi la meniul principal

Alegeți opțiunea: 2
Alfabet englez activat.
```

---

## 🔬 **Technical Features**

### ✅ **Core Functionality**

- **Dynamic Matrix Generation**: Automatically calculates optimal matrix dimensions
- **Text Preprocessing**: Handles duplicates and odd-length text
- **Robust Validation**: Validates keys (minimum 7 characters) and input text
- **Separator Handling**: Intelligently manages separator insertion
- **Bidirectional Encryption**: Full encrypt/decrypt functionality

### ✅ **Code Quality**

- **Modular Design**: Each component has a single responsibility
- **Type Hints**: Modern Python typing for better code clarity
- **Error Handling**: Comprehensive exception management
- **Documentation**: Extensive docstrings for all classes and methods
- **Reusability**: Easy to extend with new alphabets or algorithms

### 🏛️ **Design Patterns**

1. **Facade Pattern**: `PlayfairCipher` provides simple interface to complex subsystems
2. **Factory Pattern**: `AlphabetConfigs` creates predefined configurations
3. **Strategy Pattern**: Pluggable alphabet configurations
4. **Dependency Injection**: Components receive dependencies through constructors

---

## 🔍 **Key Components Explained**

### **1. PlayfairCipher (Facade)**

Main entry point coordinating all operations:

```python
cipher = PlayfairCipher(AlphabetConfigs.romanian())
ciphertext = cipher.encrypt("HELLO", "SECRETKEY")
plaintext = cipher.decrypt(ciphertext, "SECRETKEY")
```

### **2. PlayfairMatrix**

Manages matrix construction and lookups:

```python
matrix.create_from_key("PLAYFAIR")
position = matrix.get_position('A')  # Returns (row, col)
char = matrix.get_char_at_position(0, 1)
```

### **3. PlayfairCryptographer**

Core encryption/decryption logic:

```python
encrypted_pair = cryptographer.encrypt_pair("HE")  # "FG"
decrypted_pair = cryptographer.decrypt_pair("FG")  # "HE"
```

### **4. TextPreprocessor**

Prepares text for encryption:

```python
pairs = preprocessor.prepare_text("HELLO")  # ["HE", "LK", "LO"]
# Handles duplicates: "BOOK" → ["BO", "OK", "KO"]
```

### **5. AlphabetValidator**

Ensures input correctness:

```python
validator.validate_key("SECRET")     # Minimum 7 chars
validator.validate_text("HELLO")     # Only alphabet chars
```

---

## 📚 **Algorithm Walkthrough**

### **Encryption Example: "HELLO" with key "PLAYFAIR"**

#### **Step 1: Create Matrix**

```
Key: PLAYFAIR → P L A Y F I R
Add remaining letters: B C D E G H K M N O Q S T U V W X Z

Matrix (5×5):
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
```

#### **Step 2: Preprocess Text**

```
HELLO → HE LK LO  (LL becomes LKL, so pairs: HE LK LO)
```

#### **Step 3: Encrypt Each Pair**

```
HE: H(2,2) E(2,0) → Same row → MG (2,3)(2,1)
LK: L(0,1) K(2,3) → Rectangle → YM (0,3)(2,1)
LO: L(0,1) O(3,1) → Same col → RV (1,1)(4,1)
```

#### **Result**: `MGYMRV`

### **Decryption Process**

Same steps but reverse direction (left, up, swap corners).

---

## 🛡️ **Security Analysis**

### **Strengths**

✅ **Digraph encryption** makes frequency analysis harder  
✅ **Larger key space** than simple substitution ciphers  
✅ **Key-dependent matrix** adds complexity  
✅ **No direct letter-to-letter mapping** preserved

### **Weaknesses**

⚠️ **Vulnerable to known-plaintext attacks**  
⚠️ **Digraph patterns** can still be analyzed statistically  
⚠️ **Deterministic encryption** (same plaintext → same ciphertext)  
⚠️ **No authentication** or integrity protection  
⚠️ **Obsolete for modern security** requirements

### **Historical Context**

- **Invented**: 1854 by Charles Wheatstone
- **Promoted by**: Lord Playfair (hence the name)
- **Used in**: WWI and WWII tactical communications
- **Status today**: Educational/historical interest only

---

## 🚀 **Advantages of This Implementation**

1. **Multi-alphabet support**: Not limited to English
2. **Automatic matrix sizing**: Works with any alphabet length
3. **Clean architecture**: Easy to understand and extend
4. **Type safety**: Python type hints for better IDE support
5. **Interactive UI**: User-friendly console interface
6. **Educational value**: Clear demonstration of classical cryptography

---

## 🎓 **Conclusion**

This laboratory work successfully implemented the Playfair cipher with several enhancements:

- **Flexible alphabet system** supporting Romanian, English, Russian, and custom alphabets
- **Clean object-oriented architecture** with proper separation of concerns
- **Robust input validation** and error handling
- **Interactive user interface** for practical demonstrations
- **Educational focus** on understanding classical cryptography principles

The Playfair cipher represents an important historical step in cryptography, moving from monoalphabetic to polyalphabetic substitution. While not secure by modern standards, it demonstrates key concepts:

- **Digraph processing** increases cipher complexity
- **Key-based transformations** provide variable encryption
- **Matrix-based operations** enable systematic encryption rules

**Modern Relevance**: This implementation serves as an educational tool for understanding:
- Classical cryptography evolution
- Algorithm design patterns
- Software architecture principles
- The importance of modern cryptographic standards

---

## 📚 **References**

- **Course Materials** – _Cryptography and Security_, UTM FCIM, 2025
- **Stallings, W.** – _Cryptography and Network Security: Principles and Practice_
- **Singh, S.** – _The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography_
- **Original Documentation** – _Lucrare de laborator nr. 3. Cifruri polialfabetice.pdf_

---

## 🛠️ **Dependencies**

- **Python 3.8+**
- **No external libraries required** (pure Python implementation)

---

## 📝 **License**

This project is part of academic coursework at Technical University of Moldova (UTM).

