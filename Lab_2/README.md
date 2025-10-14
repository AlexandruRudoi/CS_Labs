# Cryptanalysis of Monoalphabetic Ciphers & Frequency Analysis

### **Course**: Cryptography and Security

### **Author**: Alexandru Rudoi

📑 **[👉 Read the Full Report](https://github.com/AlexandruRudoi/CS_Labs/blob/main/Lab_2/CS_Lab2_Report.pdf)**

---

## 📖 **Overview**

This project demonstrates the application of frequency-analysis techniques for breaking monoalphabetic substitution ciphers. The laboratory work focuses on understanding statistical cryptanalysis methods and includes:

- **Symbol Frequency Analysis**: Computing letter frequencies in intercepted ciphertext.
- **Statistical Comparison**: Aligning ciphertext patterns with English language distribution.
- **Iterative Decryption**: Progressive plaintext recovery using linguistic patterns.
- **Cryptographic Vulnerability Assessment**: Understanding weaknesses in classical ciphers.

---

## 🎯 **Objectives**

- Apply **frequency analysis techniques** to break monoalphabetic substitution ciphers.
- Compare **ciphertext letter distributions** with empirical English frequencies.
- Use **linguistic patterns** (digraphs, trigraphs, common words) to guide decryption.
- **Reconstruct the original message** and recover the substitution key.
- Understand **statistical vulnerabilities** in classical cryptographic systems.

---

## 🔧 **Implementation Details**

### 📊 **Frequency Analysis Attack Methodology**

The cryptanalysis process leverages statistical properties of natural language to break monoalphabetic substitution ciphers:

**Core Principle**: Monoalphabetic ciphers preserve letter frequency patterns from the underlying language.

### 🎯 **Attack Strategy**

1. **Letter Frequency Computation**: Calculate occurrence rates for each ciphertext symbol.
2. **Statistical Alignment**: Match high-frequency ciphertext letters with common English letters (E, T, A, O, I, N).
3. **Pattern Recognition**: Identify linguistic structures:
   - **Common digraphs**: TH, HE, AN, IN, ER, ON, RE
   - **Common trigraphs**: THE, AND, THA, ENT, ION, TIO
   - **Doubled letters**: SS, EE, TT, OO, FF
   - **Single-letter words**: A, I
4. **Iterative Refinement**: Apply substitutions and validate against English language patterns.

### 📈 **English Letter Frequencies (Reference)**

```
E: 12.70%    T: 9.06%     A: 8.17%     O: 7.51%     I: 6.97%
N: 6.75%     S: 6.33%     H: 6.09%     R: 5.99%     D: 4.25%
L: 4.03%     C: 2.78%     U: 2.76%     M: 2.41%     W: 2.36%
F: 2.23%     G: 2.02%     Y: 1.97%     P: 1.93%     B: 1.29%
V: 0.98%     K: 0.77%     J: 0.15%     X: 0.15%     Q: 0.10%    Z: 0.07%
```

### 🔑 **My Variant (25 → 2)**

**Assigned Ciphertext**:

```
WQV TOOXWXNG NC PVHIVHF WN WQV WITGPCNIZTWXNGP UINODHVOHIFUWNJITUQF...
[Full ciphertext from variant 25→2]
```

---

## 🔬 **Step-by-Step Cryptanalysis Process**

### **Step 1: Initial Frequency Analysis**

- Computed letter frequencies in the ciphertext
- Identified most frequent symbols: **V** (likely E), **W** (likely T)
- **Initial mapping**: `V→e, W→t`

### **Step 2: Pattern Recognition - "THE"**

- Located frequent 3-letter pattern: `tQe`
- Recognized as common English word "THE"
- **Added mapping**: `Q→h`

### **Step 3: Short Words & Single Letters**

- Analyzed 2-letter patterns: `tN` (to), `Xt` (it)
- **Added mappings**: `N→o, X→i`
- Single letter `T` identified as "a": `T→a`

### **Step 4: High-Frequency Words**

- Common words: `oI` (or), `oCC` (off), `Xt` (is)
- **Added mappings**: `I→r, C→f, P→s`

### **Step 5: Contextual Vocabulary**

- Domain-specific words: `aOOitioG` (addition), `trDe` (true)
- **Added mappings**: `D→u, O→d, G→n`

### **Step 6: Final Resolution**

- Remaining substitutions from clear word patterns
- **Complete mapping**: All 26 letters successfully recovered

### 🔐 **Final Recovered Key**

```
Cipher:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Plaintext: b q f u x y n c r g v k z o d s h w l a p e t i j m
```

### 📜 **Recovered Plaintext (First Paragraph)**

```
the addition of secrecy to the transformations produced
cryptography. true, it was more of a game than anything else—it sought
to delay comprehension for only the shortest possible time, not the
longest—and the cryptanalysis was, likewise, just a puzzle. egypt's was
thus a quasi cryptology in contrast to the deadly serious science of today.
```

---

## 🛠️ **Tools & Resources Used**

### **Online Cryptanalysis Tool**

- **[Frequency Analysis - Breaking the Code](https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html)**
- Interactive tool for computing letter frequencies and testing substitutions
- Visual frequency charts for pattern comparison

### **Analysis Methodology**

1. **Paste ciphertext** into the frequency analysis tool
2. **Generate frequency chart** comparing ciphertext vs English distributions
3. **Apply initial substitutions** based on frequency matching
4. **Iteratively refine** using linguistic patterns and word recognition
5. **Validate results** against English language structure

---

## 🏁 **How to Analyze Your Own Ciphertext**

1. **Access the analysis tool**:

   ```
   https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html
   ```

2. **Input your ciphertext** (letters only, spaces and punctuation preserved)

3. **Start with frequency analysis**:

   - Match highest frequency letters with E, T, A, O, I
   - Look for single-letter words (A, I)
   - Identify common short words (THE, AND, TO, IT)

4. **Apply substitutions incrementally**:

   - Test each hypothesis
   - Validate against emerging word patterns
   - Refine based on linguistic intuition

5. **Complete the decryption**:
   - Fill remaining letters using context
   - Verify the complete plaintext makes sense

### **Example Workflow**

```
Original: WQV TOOXWXNG NC PVHIVHF...
Step 1:   the aOOXtXNG NC seHreHF...  (V→e, W→t, P→s, H→c)
Step 2:   the addition of secrecy...   (remaining letters)
```

---

## 🔍 **Key Features & Insights**

- ✅ **Statistical Analysis**: Comprehensive frequency distribution comparison
- ✅ **Pattern Recognition**: Systematic identification of linguistic structures
- ✅ **Iterative Refinement**: Progressive substitution validation and correction
- ✅ **Linguistic Intuition**: Human-guided decision making for ambiguous cases
- ✅ **Complete Recovery**: Successful reconstruction of both plaintext and cipher key
- ✅ **Vulnerability Assessment**: Understanding monoalphabetic cipher weaknesses

### 🛡️ **Security Analysis**

- **Key Space**: 26! ≈ 4.0 × 10²⁶ possible permutations (theoretical)
- **Practical Vulnerability**: Easily broken with frequency analysis
- **Text Length Dependency**: Longer texts provide more statistical data
- **Language Dependency**: Requires knowledge of underlying language patterns

### 📊 **Success Factors**

1. **Sufficient text length** (>500 characters) for reliable frequency analysis
2. **Preserved word boundaries** (spaces maintained) for pattern recognition
3. **Domain vocabulary** (cryptography context) provided semantic clues
4. **Systematic approach** combining statistics with linguistic knowledge

---

## 🎓 **Conclusion**

This laboratory work demonstrated the fundamental vulnerability of monoalphabetic substitution ciphers to frequency analysis attacks. Key learning outcomes include:

- **Statistical cryptanalysis** is highly effective against classical ciphers
- **Human intuition** remains crucial for resolving linguistic ambiguities
- **Pattern recognition** accelerates the decryption process significantly
- **Modern cryptography** must address these statistical vulnerabilities

The successful decryption of the assigned variant showcased how frequency analysis, combined with systematic linguistic pattern recognition, can completely break monoalphabetic substitution ciphers. This reinforces the historical transition from classical to modern cryptographic methods that resist statistical analysis.

**Recovered Message Topic**: The text discusses the historical development of cryptography, from ancient civilizations (Egypt, China, India, Mesopotamia) through medieval times, highlighting how cryptographic knowledge evolved across different cultures and periods.

---

## 📚 **References**

- **Course Materials** – _Cryptography and Security_, UTM FCIM, 2025
- **Interactive Tool** – [Frequency Analysis: Breaking the Code](https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html)
- **William Stallings** – _Cryptography and Network Security: Principles and Practice_
- **Historical Context** – Analysis of cryptographic development across ancient civilizations
